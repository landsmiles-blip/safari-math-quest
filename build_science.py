"""
Builder script to assemble the complete standalone safari_science_quest.html
Combines:
- HTML structure with all screens and accessible semantic elements
- src/science/styles.css
- src/science/science_audio_ui.js
- src/science/science_curriculum.js
- src/science/interactive_labs.js
- src/science/wallpaper_certificate.js
- Master App Controller script (ScienceApp)
"""
import os

BASE_DIR = r"c:\GridLock\The safari Quest"
SRC_DIR = os.path.join(BASE_DIR, "src", "science")

with open(os.path.join(SRC_DIR, "styles.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

with open(os.path.join(SRC_DIR, "science_audio_ui.js"), "r", encoding="utf-8") as f:
    audio_js = f.read()

with open(os.path.join(SRC_DIR, "science_curriculum.js"), "r", encoding="utf-8") as f:
    curriculum_js = f.read()

with open(os.path.join(SRC_DIR, "interactive_labs.js"), "r", encoding="utf-8") as f:
    labs_js = f.read()

with open(os.path.join(SRC_DIR, "wallpaper_certificate.js"), "r", encoding="utf-8") as f:
    cert_js = f.read()

app_controller_js = """
/* ==========================================================================
   MASTER APPLICATION CONTROLLER: ScienceApp
   Coordinates State, Screen Transitions, Lab Completion, Exam Engine,
   Speech Narration, Remediation Loop, and Wallpaper Certificate.
   ========================================================================== */

window.ScienceApp = (function() {
  'use strict';

  const STORAGE_KEYS = {
    PLAYER: 'safari_sci_player',
    BADGES: 'safari_sci_badges',
    FIRST_PLAY: 'safari_sci_first_play_done',
    MUTED: 'safari_sci_muted'
  };

  const LAB_DATA = {
    magnet: {
      title: "Magnetic Physics & Sorting Workshop",
      icon: "🧲",
      concepts: ["Magnetic Poles", "Attract & Repel", "Ferrous Metals"],
      pipHint: "Welcome to the Magnet Lab! Drag opposite poles together to see attraction, and like poles to see repulsion. Then use the horseshoe magnet to collect all magnetic items!"
    },
    friction: {
      title: "Pip's Ramp & Friction Runway",
      icon: "🏎️",
      concepts: ["Gravity", "Incline Angle", "Surface Friction"],
      pipHint: "Adjust the ramp incline and choose different track surfaces like Ice or Sandpaper! Launch the car and observe how friction slows down the wheels."
    },
    thermal: {
      title: "Thermal Transformation Station",
      icon: "🌡️",
      concepts: ["States of Matter", "Melting & Freezing", "Reversible vs Irreversible"],
      pipHint: "Slide the thermal pad to heat or freeze items! Observe reversible phase changes with chocolate and ice, and permanent chemical change when frying an egg."
    },
    nutrition: {
      title: "Bio-Nutrition & Animal Feeder",
      icon: "🥗",
      concepts: ["Carbohydrates", "Proteins", "Vitamins & Diets"],
      pipHint: "Sort healthy foods into their correct pods: Carbs for energy, Protein for growth, and Vitamins for immunity! Then feed our herbivore, carnivore, and omnivore guests."
    },
    lifecycle: {
      title: "Life Cycle Astrolabe Wheel",
      icon: "🔄",
      concepts: ["Metamorphosis", "Egg & Larva", "Animal Conservation"],
      pipHint: "Arrange the developmental stages in clockwise order for Butterfly, Frog, and Chicken! Complete the circle to watch the living transformation cycle."
    }
  };

  const state = {
    playerName: localStorage.getItem(STORAGE_KEYS.PLAYER) || "Junior Explorer",
    currentScreen: "start",
    currentLabId: null,
    badges: {
      magnet: false,
      friction: false,
      thermal: false,
      nutrition: false,
      lifecycle: false
    },
    firstPlayCompleted: false,
    exam: {
      questions: [],
      currentQIndex: 0,
      currentSubIndex: 0,
      currentAnswers: [],
      userAnswers: [],
      totalScore: 0,
      domainScores: {},
      weakestDomain: null
    }
  };

  function loadSavedState() {
    try {
      const savedBadges = localStorage.getItem(STORAGE_KEYS.BADGES);
      if (savedBadges) {
        state.badges = Object.assign(state.badges, JSON.parse(savedBadges));
      }
      state.firstPlayCompleted = localStorage.getItem(STORAGE_KEYS.FIRST_PLAY) === 'true';
      const savedMute = localStorage.getItem(STORAGE_KEYS.MUTED) === 'true';
      if (window.ScienceAudioUI) {
        window.ScienceAudioUI.setMuted(savedMute);
      }
    } catch (e) {
      console.warn("Could not load localStorage state", e);
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEYS.PLAYER, state.playerName);
      localStorage.setItem(STORAGE_KEYS.BADGES, JSON.stringify(state.badges));
      localStorage.setItem(STORAGE_KEYS.FIRST_PLAY, state.firstPlayCompleted ? 'true' : 'false');
      if (window.ScienceAudioUI) {
        localStorage.setItem(STORAGE_KEYS.MUTED, window.ScienceAudioUI.isMuted() ? 'true' : 'false');
      }
    } catch (e) {}
  }

  function getBadgeCount() {
    return Object.values(state.badges).filter(Boolean).length;
  }

  function showScreen(screenId) {
    state.currentScreen = screenId;
    const screens = ['start', 'hub', 'lab', 'exam', 'remediation', 'certificate'];
    screens.forEach(id => {
      const el = document.getElementById('screen-' + id);
      if (el) {
        if (id === screenId) {
          el.style.display = (id === 'start' || id === 'hub' || id === 'lab' || id === 'exam' || id === 'remediation' || id === 'certificate') ? 'flex' : 'block';
        } else {
          el.style.display = 'none';
        }
      }
    });

    // Update Header
    const header = document.getElementById('main-header');
    if (header) {
      header.style.display = (screenId === 'start') ? 'none' : 'flex';
      const nameChip = document.getElementById('header-player-name');
      if (nameChip) nameChip.textContent = state.playerName;
      const starCounter = document.getElementById('header-stars');
      if (starCounter) starCounter.textContent = `${getBadgeCount()} / 5 Badges`;
    }

    if (screenId === 'hub') {
      renderHub();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function renderHub() {
    // Render 5 badge slots
    const badgeSlots = document.querySelectorAll('.badge-slot');
    badgeSlots.forEach(slot => {
      const bKey = slot.getAttribute('data-badge');
      if (state.badges[bKey]) {
        slot.classList.add('unlocked');
        const statusText = slot.querySelector('.badge-status-text');
        if (statusText) statusText.textContent = "Earned 🏅";
      } else {
        slot.classList.remove('unlocked');
        const statusText = slot.querySelector('.badge-status-text');
        if (statusText) statusText.textContent = "Locked 🔒";
      }
    });

    // Render 5 lab station cards
    const labCards = document.querySelectorAll('.lab-station-card');
    labCards.forEach(card => {
      const lKey = card.getAttribute('data-lab');
      const badgeElem = card.querySelector('.lab-status-badge');
      if (badgeElem) {
        if (state.badges[lKey]) {
          badgeElem.className = 'lab-status-badge status-complete';
          badgeElem.textContent = "Mastered 🌟";
        } else {
          badgeElem.className = 'lab-status-badge status-ready';
          badgeElem.textContent = "Open Lab 🔬";
        }
      }
    });

    // Render Exam Launch Banner
    const examBanner = document.getElementById('exam-launch-banner');
    const examBtn = document.getElementById('btn-launch-exam');
    const examSubtitle = document.getElementById('exam-banner-subtitle');
    const allBadgesCollected = getBadgeCount() === 5;
    const isExamReady = allBadgesCollected || state.firstPlayCompleted;

    if (isExamReady) {
      if (examBanner) {
        examBanner.classList.remove('locked');
        examBanner.classList.add('unlocked');
      }
      if (examSubtitle) examSubtitle.textContent = "All 5 Discovery Labs Mastered! Step into the Exam Hall to earn your 15-Star National Diploma!";
      if (examBtn) {
        examBtn.disabled = false;
        examBtn.className = "btn btn-lime";
        examBtn.innerHTML = "Take 15-Mark National Exam 🏆";
      }
    } else {
      if (examBanner) {
        examBanner.classList.add('locked');
        examBanner.classList.remove('unlocked');
      }
      if (examSubtitle) examSubtitle.textContent = `First-Time Prerequisite: Complete all 5 Discovery Labs to unlock the Exam! (${getBadgeCount()}/5 Completed)`;
      if (examBtn) {
        examBtn.disabled = true;
        examBtn.className = "btn btn-glass";
        examBtn.innerHTML = `Exam Locked 🔒 (${getBadgeCount()}/5 Labs)`;
      }
    }
  }

  function openLab(labId) {
    if (!LAB_DATA[labId]) return;
    state.currentLabId = labId;
    const info = LAB_DATA[labId];

    const titleElem = document.getElementById('lab-title-text');
    if (titleElem) titleElem.textContent = `${info.icon} ${info.title}`;

    const hintElem = document.getElementById('pip-hint-text');
    if (hintElem) hintElem.textContent = info.pipHint;

    const badgeElem = document.getElementById('lab-badge-indicator');
    if (badgeElem) {
      badgeElem.textContent = state.badges[labId] ? "Badge Earned ⭐" : "Badge In Progress 🧪";
      badgeElem.className = state.badges[labId] ? "badge-pill earned" : "badge-pill";
    }

    showScreen('lab');

    // Mount interactive simulation
    if (window.InteractiveLabs) {
      window.InteractiveLabs.mountLab('lab-mount-point', labId);
    }

    if (window.playSound) window.playSound('bubble');
    if (window.speakText) {
      window.speakText(info.pipHint);
    }
  }

  function onLabCompleted(labId) {
    if (!state.badges[labId]) {
      state.badges[labId] = true;
      saveState();

      if (window.playSound) window.playSound('badge');
      if (window.ScienceAudioUI && window.ScienceAudioUI.spawnSparks) {
        window.ScienceAudioUI.spawnSparks(window.innerWidth / 2, window.innerHeight / 2, '#39ff14');
      }

      const badgeElem = document.getElementById('lab-badge-indicator');
      if (badgeElem) {
        badgeElem.textContent = "Badge Earned ⭐";
        badgeElem.className = "badge-pill earned";
      }

      const allEarned = getBadgeCount() === 5;
      if (allEarned && !state.firstPlayCompleted) {
        state.firstPlayCompleted = true;
        saveState();
        setTimeout(() => {
          alert("🎉 OUTSTANDING! You have mastered all 5 Discovery Labs!\nThe Grade 3 National Science Exam is now UNLOCKED!");
          if (window.speakText) {
            window.speakText("Outstanding work! You have mastered all five discovery labs. The Grade 3 National Science Exam is now unlocked!");
          }
          showScreen('hub');
        }, 1200);
      } else {
        setTimeout(() => {
          alert(`🌟 Congratulations! You earned the ${LAB_DATA[labId] ? LAB_DATA[labId].title : 'Lab'} Badge!`);
        }, 600);
      }
    }
  }

  // EXAM CONTROLLER
  function startExam() {
    if (getBadgeCount() < 5 && !state.firstPlayCompleted) {
      alert("Please complete all 5 Discovery Labs first before attempting the Exam!");
      return;
    }

    if (!window.ScienceCurriculum) {
      alert("Science Curriculum Engine is loading. Please wait a moment.");
      return;
    }

    state.exam.questions = window.ScienceCurriculum.generateExam();
    state.exam.currentQIndex = 0;
    state.exam.currentSubIndex = 0;
    state.exam.currentAnswers = [];
    state.exam.userAnswers = [];
    state.exam.totalScore = 0;

    showScreen('exam');
    if (window.playSound) window.playSound('heatFlame');
    renderCurrentQuestion();
  }

  function renderCurrentQuestion() {
    const q = state.exam.questions[state.exam.currentQIndex];
    if (!q) {
      finishExam();
      return;
    }

    // Update beaker liquid and progress bar
    const progressPct = ((state.exam.currentQIndex) / 15) * 100;
    const beakerFill = document.getElementById('beaker-fill');
    if (beakerFill) beakerFill.style.height = `${Math.max(15, progressPct)}%`;
    const progBar = document.getElementById('exam-progress-bar');
    if (progBar) progBar.style.width = `${progressPct}%`;
    const counterText = document.getElementById('exam-q-counter');
    if (counterText) counterText.textContent = `Question ${state.exam.currentQIndex + 1} of 15`;

    // Level Badge
    const levelBadge = document.getElementById('exam-level-badge');
    if (levelBadge) {
      levelBadge.className = `level-badge level-${q.level}`;
      levelBadge.textContent = `Level ${q.level} • ${q.domain.toUpperCase()}`;
    }

    // Scenario title & narrative
    const scenarioCard = document.getElementById('scenario-card');
    const titleElem = document.getElementById('scenario-title');
    const narrElem = document.getElementById('scenario-narrative');
    const diagElem = document.getElementById('scenario-diagram');

    if (titleElem) titleElem.textContent = q.title;

    if (q.type === 'scenario' && q.scenarioText) {
      if (narrElem) {
        narrElem.textContent = q.scenarioText;
        narrElem.style.display = 'block';
      }
    } else {
      if (narrElem) narrElem.style.display = 'none';
    }

    if (q.diagramSvg && q.diagramSvg.trim()) {
      if (diagElem) {
        diagElem.innerHTML = q.diagramSvg;
        diagElem.style.display = 'flex';
      }
    } else {
      if (diagElem) diagElem.style.display = 'none';
    }

    // Sub-question prompt
    const subQ = q.subQuestions[state.exam.currentSubIndex];
    const promptElem = document.getElementById('subq-prompt');
    const partTag = subQ.part ? `[Part ${subQ.part.toUpperCase()}] ` : "";
    if (promptElem) promptElem.textContent = `${partTag}${subQ.prompt}`;

    // Read question with soft female voice
    if (window.speakText) {
      const readText = (q.type === 'scenario' && state.exam.currentSubIndex === 0 && q.scenarioText) 
        ? `${q.scenarioText}. ${subQ.prompt}` 
        : subQ.prompt;
      window.speakText(readText);
    }

    // Render 4 Options
    const optionsGrid = document.getElementById('exam-options-grid');
    if (optionsGrid) {
      optionsGrid.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D'];
      subQ.options.forEach((optText, idx) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.innerHTML = `
          <span class="option-letter">${letters[idx]}</span>
          <span class="option-text">${optText}</span>
        `;
        btn.onclick = () => handleOptionClick(btn, idx, subQ, q);
        optionsGrid.appendChild(btn);
      });
    }

    // Hide explanation box
    const expBox = document.getElementById('explanation-box');
    if (expBox) expBox.style.display = 'none';
  }

  function handleOptionClick(clickedBtn, chosenIndex, subQ, q) {
    // Disable all options
    const allBtns = document.querySelectorAll('.option-btn');
    allBtns.forEach(b => b.disabled = true);

    const isCorrect = (chosenIndex === subQ.correctIndex);

    if (isCorrect) {
      clickedBtn.classList.add('correct');
      if (window.playSound) window.playSound('correct');
      if (window.ScienceAudioUI && window.ScienceAudioUI.spawnSparks) {
        const rect = clickedBtn.getBoundingClientRect();
        window.ScienceAudioUI.spawnSparks(rect.left + rect.width / 2, rect.top + rect.height / 2, '#39ff14');
      }
    } else {
      clickedBtn.classList.add('incorrect');
      if (window.playSound) window.playSound('wrong');
      // Highlight the correct one
      allBtns.forEach((b, idx) => {
        if (idx === subQ.correctIndex) {
          b.classList.add('correct');
        }
      });
    }

    // Save sub-answer
    state.exam.currentAnswers.push(chosenIndex);

    // Show Explanation Box
    const expBox = document.getElementById('explanation-box');
    const expText = document.getElementById('explanation-text');
    const nextBtn = document.getElementById('btn-next-question');

    if (expText) {
      expText.innerHTML = `<strong>${isCorrect ? "Correct! 🌟" : "Good Try! 💡"}</strong> ${subQ.explanation}`;
    }
    if (expBox) expBox.style.display = 'flex';

    if (nextBtn) {
      const hasMoreSubQ = (state.exam.currentSubIndex < q.subQuestions.length - 1);
      nextBtn.textContent = hasMoreSubQ ? "Next Part ➡️" : "Next Question 🚀";
      nextBtn.onclick = () => {
        if (hasMoreSubQ) {
          state.exam.currentSubIndex++;
          renderCurrentQuestion();
        } else {
          // Record full answer for this question
          state.exam.userAnswers.push({
            qIndex: q.id,
            answer: (q.subQuestions.length > 1) ? [...state.exam.currentAnswers] : state.exam.currentAnswers[0]
          });
          state.exam.currentAnswers = [];
          state.exam.currentSubIndex = 0;
          state.exam.currentQIndex++;
          renderCurrentQuestion();
        }
      };
    }
  }

  function finishExam() {
    const evaluation = window.ScienceCurriculum.evaluateExam(state.exam.userAnswers, state.exam.questions);
    state.exam.totalScore = evaluation.totalScore;
    state.exam.domainScores = evaluation.domainScores;
    state.exam.weakestDomain = evaluation.weakestDomain;

    if (evaluation.totalScore >= 12) {
      // SUCCESS: GOLD / SILVER CERTIFICATE!
      showScreen('certificate');
      if (window.playSound) window.playSound('fanfare');
      if (window.speakText) {
        window.speakText(`Sensational achievement, ${state.playerName}! You scored ${evaluation.totalScore} out of 15 marks. Your Official Junior Scientist Diploma is ready!`);
      }
      renderCertificateScreen(evaluation);
    } else {
      // BRONZE: "BRONZE IS NOT ACCEPTABLE!" REMEDIATION LOOP
      showScreen('remediation');
      if (window.playSound) window.playSound('wrong');
      renderRemediationScreen(evaluation);
    }
  }

  function renderRemediationScreen(evaluation) {
    const scoreText = document.getElementById('bronze-score-text');
    if (scoreText) scoreText.textContent = `You scored ${evaluation.totalScore} / 15 Marks`;

    const weakestKey = evaluation.weakestDomain || 'forces';
    const weakestData = evaluation.domainScores[weakestKey] || { label: "Forces, Friction & Magnets", labId: "friction" };

    const diagText = document.getElementById('diagnostic-message');
    if (diagText) {
      diagText.textContent = `For an MEP Junior Scientist, Bronze is not acceptable! You did very well in other areas, but you made errors in ${weakestData.label}. Return to the laboratory now to review the principles and sharpen your score!`;
    }

    if (window.speakText) {
      window.speakText(`Bronze is not acceptable for an MEP Junior Scientist! You scored ${evaluation.totalScore} marks. Head back to the ${weakestData.label} lab now to master this concept!`);
    }

    // Render domain breakdown bars
    const meterList = document.getElementById('remediation-domain-meters');
    if (meterList) {
      meterList.innerHTML = '';
      for (const [key, d] of Object.entries(evaluation.domainScores)) {
        const row = document.createElement('div');
        const isWeakest = (key === weakestKey);
        row.className = isWeakest ? 'domain-meter-row weakest' : 'domain-meter-row';
        const pct = Math.round((d.correct / d.total) * 100);
        row.innerHTML = `
          <span class="domain-label">${d.label}</span>
          <div class="domain-score-bar">
            <div class="domain-bar-fill" style="width: ${pct}%"></div>
          </div>
          <span class="domain-ratio">${d.correct} / ${d.total}</span>
        `;
        meterList.appendChild(row);
      }
    }

    // Retrain button
    const retrainBtn = document.getElementById('btn-remediation-retrain');
    if (retrainBtn) {
      retrainBtn.innerHTML = `🔬 Practice at ${weakestData.label} Lab`;
      retrainBtn.onclick = () => {
        openLab(weakestData.labId || 'friction');
      };
    }
  }

  function renderCertificateScreen(evaluation) {
    const canvas = document.getElementById('certificate-canvas');
    if (!canvas || !window.WallpaperCertificate) return;

    const today = new Date();
    const dateStr = today.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });

    window.WallpaperCertificate.renderCertificate(canvas, {
      studentName: state.playerName,
      score: evaluation.totalScore,
      domainScores: evaluation.domainScores,
      date: dateStr
    });

    const downloadBtn = document.getElementById('btn-download-wallpaper');
    if (downloadBtn) {
      downloadBtn.onclick = () => {
        if (window.playSound) window.playSound('bubble');
        const filename = `Junior_Scientist_${state.playerName.replace(/\\s+/g, '_')}_A4_Wallpaper.png`;
        window.WallpaperCertificate.downloadWallpaper(canvas, filename);
      };
    }

    const printBtn = document.getElementById('btn-print-cert');
    if (printBtn) {
      printBtn.onclick = () => {
        if (window.playSound) window.playSound('bubble');
        window.WallpaperCertificate.printCertificate(canvas);
      };
    }
  }

  function init() {
    loadSavedState();

    // Start Screen Enter Button
    const enterBtn = document.getElementById('btn-enter-lab');
    const nameInput = document.getElementById('player-name-input');
    if (nameInput) {
      nameInput.value = state.playerName;
      nameInput.addEventListener('input', (e) => {
        state.playerName = e.target.value.trim() || "Junior Explorer";
        saveState();
      });
    }

    if (enterBtn) {
      enterBtn.addEventListener('click', () => {
        if (window.ScienceAudioUI) window.ScienceAudioUI.initAudio();
        if (window.playSound) window.playSound('bubble');
        showScreen('hub');
      });
    }

    // Audio Mute Toggle Button
    const muteBtn = document.getElementById('btn-toggle-audio');
    if (muteBtn) {
      muteBtn.addEventListener('click', () => {
        if (window.ScienceAudioUI) {
          const isMuted = window.ScienceAudioUI.toggleMute();
          muteBtn.textContent = isMuted ? "🔇" : "🔊";
          saveState();
        }
      });
    }

    // Lab Station click listeners
    const labCards = document.querySelectorAll('.lab-station-card');
    labCards.forEach(card => {
      card.addEventListener('click', () => {
        const labId = card.getAttribute('data-lab');
        openLab(labId);
      });
    });

    // Back to Hub Buttons
    const backBtns = document.querySelectorAll('.btn-back-to-hub');
    backBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        if (window.playSound) window.playSound('bubble');
        showScreen('hub');
      });
    });

    // Launch Exam Button
    const launchExamBtn = document.getElementById('btn-launch-exam');
    if (launchExamBtn) {
      launchExamBtn.addEventListener('click', () => {
        startExam();
      });
    }

    // Retake Exam Button
    const retakeBtn = document.getElementById('btn-retake-exam');
    if (retakeBtn) {
      retakeBtn.addEventListener('click', () => {
        startExam();
      });
    }

    // Render Mascots on Start Screen
    if (window.ScienceAudioUI) {
      const leoContainer = document.getElementById('mascot-leo-container');
      if (leoContainer) leoContainer.innerHTML = window.ScienceAudioUI.renderMascotLeo('happy', 90);
      const pipContainer = document.getElementById('mascot-pip-container');
      if (pipContainer) pipContainer.innerHTML = window.ScienceAudioUI.renderMascotPip('float', 90);

      const pipHintAvatar = document.getElementById('pip-hint-avatar');
      if (pipHintAvatar) pipHintAvatar.innerHTML = window.ScienceAudioUI.renderMascotPip('happy', 60);

      const diagMascot = document.getElementById('diagnostic-mascot-avatar');
      if (diagMascot) diagMascot.innerHTML = window.ScienceAudioUI.renderMascotLeo('shocked', 90);
    }

    // Start on start screen
    showScreen('start');
  }

  return {
    init,
    showScreen,
    openLab,
    onLabCompleted,
    startExam,
    state
  };
})();

document.addEventListener('DOMContentLoaded', () => {
  window.ScienceApp.init();
});
"""

html_shell = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>🔬 Safari Science Quest Academy • MEP Primary 3</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
{css_content}
  </style>
</head>
<body>

  <!-- Cybernetic Grid & Particle Canvas Background -->
  <div id="bg-canvas"></div>

  <!-- Persistent Top Header / Status Bar -->
  <header class="app-header" id="main-header" style="display: none;">
    <div class="header-left">
      <div class="lab-logo-badge">
        <span class="beaker-icon">🧪</span>
        <span>Safari Science Academy</span>
      </div>
      <span class="player-id-chip">
        <span>👨‍🔬</span>
        <span id="header-player-name">Junior Explorer</span>
      </span>
    </div>
    <div class="header-right">
      <span class="star-counter" id="header-stars">0 / 5 Badges</span>
      <button class="btn btn-icon btn-glass" id="btn-toggle-audio" title="Toggle Sound & Speech">🔊</button>
      <button class="btn btn-glass btn-back-to-hub" title="Return to Discovery Hub">🏠 Hub</button>
    </div>
  </header>

  <!-- Main Container -->
  <main class="app-container">

    <!-- SCREEN 1: START SCREEN -->
    <section id="screen-start">
      <div class="hero-science-badge">🔬⚡</div>
      <h1 class="start-title">Safari Science Quest</h1>
      <p class="start-subtitle">
        Mini English Program • Primary 3 Interactive Discovery Lab & Examination Challenge
      </p>

      <!-- Mascots Showcase -->
      <div class="mascot-stage">
        <div class="mascot-card">
          <div id="mascot-leo-container"></div>
          <span class="mascot-name">Professor Leo</span>
          <span class="mascot-role">Chief Scientist</span>
        </div>
        <div class="mascot-card">
          <div id="mascot-pip-container"></div>
          <span class="mascot-name">Pip</span>
          <span class="mascot-role">Robotic Lab Assistant</span>
        </div>
      </div>

      <!-- Terminal Name Input -->
      <div class="glass-card terminal-card">
        <div class="terminal-header">
          <span>// LAB_SECURITY_GATE: AUTH_REQUIRED</span>
          <span>ONLINE 🟢</span>
        </div>
        <div class="name-input-group">
          <label for="player-name-input">STUDENT CADET IDENTIFIER:</label>
          <input type="text" id="player-name-input" class="lab-input" placeholder="Enter Your Name..." autocomplete="off">
        </div>
        <button class="btn btn-cyan" id="btn-enter-lab" style="width: 100%;">
          Enter Science Academy 🚀
        </button>
      </div>
    </section>

    <!-- SCREEN 2: HUB SCREEN (5 LABS + 5 BADGES + EXAM LAUNCH) -->
    <section id="screen-hub" style="display: none;">
      <div class="hub-hero">
        <h2>🔬 The Discovery Laboratory</h2>
        <p>Explore all 5 hands-on experimental stations, conduct live tests, and collect your 5 Lab Badges!</p>
      </div>

      <!-- 5 Discovery Lab Cards -->
      <div class="labs-grid">
        <!-- Lab 1: Magnets -->
        <div class="glass-card lab-station-card" data-lab="magnet">
          <div class="lab-card-top">
            <div class="lab-station-icon">🧲</div>
            <span class="lab-status-badge status-ready">Open Lab 🔬</span>
          </div>
          <div class="lab-station-info">
            <h3>1. Magnetic Physics & Sorting</h3>
            <p>Test bar magnet poles (N-S attract, N-N repel) and sweep a horseshoe magnet to sort ferrous metals from non-magnetic materials!</p>
            <div class="concept-pills">
              <span class="concept-pill">Poles N & S</span>
              <span class="concept-pill">Attract / Repel</span>
              <span class="concept-pill">Iron & Steel</span>
            </div>
          </div>
          <button class="btn btn-cyan" style="width: 100%;">Enter Magnet Lab ⚡</button>
        </div>

        <!-- Lab 2: Friction -->
        <div class="glass-card lab-station-card" data-lab="friction">
          <div class="lab-card-top">
            <div class="lab-station-icon">🏎️</div>
            <span class="lab-status-badge status-ready">Open Lab 🔬</span>
          </div>
          <div class="lab-station-info">
            <h3>2. Pip's Ramp & Friction Runway</h3>
            <p>Tilt the ramp angle (15°, 30°, 45°) and launch Pip's toy car across Ice, Tile, Wood, Carpet, and Sandpaper to measure friction!</p>
            <div class="concept-pills">
              <span class="concept-pill">Gravity Force</span>
              <span class="concept-pill">Ramp Slope</span>
              <span class="concept-pill">Stopping Distance</span>
            </div>
          </div>
          <button class="btn btn-amber" style="width: 100%;">Enter Friction Runway 🏁</button>
        </div>

        <!-- Lab 3: Thermal -->
        <div class="glass-card lab-station-card" data-lab="thermal">
          <div class="lab-card-top">
            <div class="lab-station-icon">🌡️</div>
            <span class="lab-status-badge status-ready">Open Lab 🔬</span>
          </div>
          <div class="lab-station-info">
            <h3>3. Thermal Transformation Station</h3>
            <p>Slide the heat/cool pad to melt chocolate and ice, freeze water, and fry an egg to discover reversible vs irreversible changes!</p>
            <div class="concept-pills">
              <span class="concept-pill">Solid / Liquid / Gas</span>
              <span class="concept-pill">Melting & Freezing</span>
              <span class="concept-pill">Reversible Changes</span>
            </div>
          </div>
          <button class="btn btn-magenta" style="width: 100%;">Enter Thermal Station 🔥</button>
        </div>

        <!-- Lab 4: Nutrition -->
        <div class="glass-card lab-station-card" data-lab="nutrition">
          <div class="lab-card-top">
            <div class="lab-station-icon">🥗</div>
            <span class="lab-status-badge status-ready">Open Lab 🔬</span>
          </div>
          <div class="lab-station-info">
            <h3>4. Bio-Nutrition & Animal Feeder</h3>
            <p>Sort foods into Carbohydrates (Energy), Proteins (Growth), and Vitamins (Health), then feed our Herbivore, Carnivore, and Omnivore guests!</p>
            <div class="concept-pills">
              <span class="concept-pill">Carbs / Protein / Vit</span>
              <span class="concept-pill">Herbivore / Carnivore</span>
              <span class="concept-pill">Basic Needs</span>
            </div>
          </div>
          <button class="btn btn-lime" style="width: 100%;">Enter Nutrition Pods 🥦</button>
        </div>

        <!-- Lab 5: Life Cycles -->
        <div class="glass-card lab-station-card" data-lab="lifecycle">
          <div class="lab-card-top">
            <div class="lab-station-icon">🔄</div>
            <span class="lab-status-badge status-ready">Open Lab 🔬</span>
          </div>
          <div class="lab-station-info">
            <h3>5. Life Cycle Astrolabe Wheel</h3>
            <p>Sequence the circular metamorphic stages for Butterfly, Frog, and Chicken. Lock all 4 sockets to trigger the metamorphosis animation!</p>
            <div class="concept-pills">
              <span class="concept-pill">Butterfly Metamorphosis</span>
              <span class="concept-pill">Tadpole & Froglet</span>
              <span class="concept-pill">Protect Habitats</span>
            </div>
          </div>
          <button class="btn btn-cyan" style="width: 100%;">Enter Astrolabe Wheel 🦋</button>
        </div>
      </div>

      <!-- 5 Badge Vault Section -->
      <div class="badge-vault-section">
        <div class="badge-vault-header">
          <h3>🏅 Junior Scientist Badge Vault</h3>
          <span style="color: var(--text-secondary); font-size: 0.9rem;">
            Earn all 5 badges to unlock the National Science Examination!
          </span>
        </div>
        <div class="badge-slots-row">
          <div class="badge-slot" data-badge="magnet">
            <div class="badge-ring">
              <span class="badge-slot-icon">🧲</span>
            </div>
            <span class="badge-slot-label">Magnetism</span>
            <span class="badge-status-text" style="font-size:0.75rem; color:var(--text-muted);">Locked 🔒</span>
          </div>
          <div class="badge-slot" data-badge="friction">
            <div class="badge-ring">
              <span class="badge-slot-icon">🏎️</span>
            </div>
            <span class="badge-slot-label">Friction</span>
            <span class="badge-status-text" style="font-size:0.75rem; color:var(--text-muted);">Locked 🔒</span>
          </div>
          <div class="badge-slot" data-badge="thermal">
            <div class="badge-ring">
              <span class="badge-slot-icon">🌡️</span>
            </div>
            <span class="badge-slot-label">Thermal</span>
            <span class="badge-status-text" style="font-size:0.75rem; color:var(--text-muted);">Locked 🔒</span>
          </div>
          <div class="badge-slot" data-badge="nutrition">
            <div class="badge-ring">
              <span class="badge-slot-icon">🥗</span>
            </div>
            <span class="badge-slot-label">Nutrition</span>
            <span class="badge-status-text" style="font-size:0.75rem; color:var(--text-muted);">Locked 🔒</span>
          </div>
          <div class="badge-slot" data-badge="lifecycle">
            <div class="badge-ring">
              <span class="badge-slot-icon">🔄</span>
            </div>
            <span class="badge-slot-label">Life Cycles</span>
            <span class="badge-status-text" style="font-size:0.75rem; color:var(--text-muted);">Locked 🔒</span>
          </div>
        </div>
      </div>

      <!-- Exam Launch Banner -->
      <div class="exam-launch-banner locked" id="exam-launch-banner">
        <div class="exam-banner-left">
          <span class="exam-banner-icon">🏆</span>
          <div class="exam-banner-text">
            <h3>Mode 2: The 15-Mark National Science Exam</h3>
            <p id="exam-banner-subtitle">
              First-Time Prerequisite: Complete all 5 Discovery Labs to unlock the Exam!
            </p>
          </div>
        </div>
        <button class="btn btn-glass" id="btn-launch-exam" disabled>
          Exam Locked 🔒
        </button>
      </div>
    </section>

    <!-- SCREEN 3: LAB STAGE SCREEN (MICRO-LAB WORKBENCH) -->
    <section id="screen-lab" style="display: none;">
      <div class="lab-stage-header">
        <button class="btn btn-glass btn-back-to-hub">← Back to Hub</button>
        <div class="lab-title-group">
          <h2 id="lab-title-text">Lab Station</h2>
        </div>
        <span class="badge-pill" id="lab-badge-indicator">Badge In Progress 🧪</span>
      </div>

      <!-- Pip's Dialogue & Guidance Bubble -->
      <div class="pip-dialogue-bubble">
        <div class="pip-avatar" id="pip-hint-avatar"></div>
        <div class="pip-bubble-content">
          <div class="pip-bubble-title">PIP'S EXPERIMENT LAB BRIEFING</div>
          <div class="pip-bubble-text" id="pip-hint-text">
            Experiment with the apparatus below!
          </div>
        </div>
      </div>

      <!-- Workbench Mount Point for InteractiveLabs -->
      <div id="lab-mount-point" class="lab-workbench"></div>
    </section>

    <!-- SCREEN 4: EXAM SCREEN -->
    <section id="screen-exam" style="display: none;">
      <div class="exam-header-bar">
        <span class="level-badge level-1" id="exam-level-badge">Level 1 • Needs</span>
        <button class="btn btn-glass btn-back-to-hub">Exit Exam ✕</button>
      </div>

      <!-- Liquid Beaker Progress Bar -->
      <div class="exam-beaker-progress-container">
        <div class="beaker-meter">
          <div class="beaker-liquid" id="beaker-fill"></div>
        </div>
        <div class="progress-bar-track">
          <div class="progress-bar-fill" id="exam-progress-bar"></div>
        </div>
        <span class="question-counter-text" id="exam-q-counter">Question 1 of 15</span>
      </div>

      <!-- Scenario Card & Diagram -->
      <div class="glass-card scenario-card" id="scenario-card">
        <h3 class="scenario-title" id="scenario-title">Question Title</h3>
        <p class="scenario-narrative" id="scenario-narrative" style="display: none;"></p>
        <div class="exam-diagram-container" id="scenario-diagram" style="display: none;"></div>

        <!-- Subquestion Prompt -->
        <div class="subquestion-container">
          <div class="subquestion-prompt-row">
            <span class="subquestion-prompt" id="subq-prompt">Prompt text...</span>
          </div>

          <!-- 4 Options Grid -->
          <div class="options-grid" id="exam-options-grid"></div>

          <!-- Explanation Box -->
          <div class="explanation-box" id="explanation-box" style="display: none;">
            <span class="explanation-title">Scientific Rationale:</span>
            <span class="explanation-text" id="explanation-text">Explanation...</span>
            <button class="btn btn-cyan" id="btn-next-question" style="align-self: flex-end; margin-top: 10px;">
              Next Question 🚀
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- SCREEN 5: REMEDIATION SCREEN ("BRONZE IS NOT ACCEPTABLE!") -->
    <section id="screen-remediation" style="display: none;">
      <div class="bronze-alert-banner">
        <h2>⚠️ BRONZE IS NOT ACCEPTABLE!</h2>
        <p id="bronze-score-text">You scored 9 / 15 Marks</p>
      </div>

      <div class="diagnostic-mascot-box">
        <div id="diagnostic-mascot-avatar"></div>
        <div class="diagnostic-text">
          <h3>PROFESSOR LEO'S DIAGNOSTIC REPORT:</h3>
          <p id="diagnostic-message">
            Bronze is not acceptable for an MEP Junior Scientist! You need to review your poorest domain before retrying the exam.
          </p>
        </div>
      </div>

      <div class="glass-card domain-breakdown-card">
        <h3>📊 Domain Score Breakdown:</h3>
        <div class="domain-meter-list" id="remediation-domain-meters"></div>
      </div>

      <div class="remediation-actions">
        <button class="btn btn-magenta" id="btn-remediation-retrain">
          🔬 Retrain at Weakest Lab Now
        </button>
        <button class="btn btn-glass btn-back-to-hub">
          Return to Hub 🏠
        </button>
      </div>
    </section>

    <!-- SCREEN 6: CERTIFICATE SCREEN -->
    <section id="screen-certificate" style="display: none;">
      <div>
        <h2 style="font-size: clamp(1.8rem, 4vw, 2.5rem); margin-bottom: 6px;">
          🎉 NATIONAL DIPLOMA OF SCIENTIFIC EXCELLENCE
        </h2>
        <p style="color: var(--hyper-cyan); font-weight: 700; font-size: 1.1rem;">
          Official Royal Thai MEP Primary 3 Junior Scientist Credential
        </p>
      </div>

      <!-- High-Res Wallpaper Canvas -->
      <div class="cert-showcase-container">
        <canvas id="certificate-canvas" width="2400" height="1696"></canvas>
      </div>

      <!-- Action Toolbar -->
      <div class="cert-action-toolbar">
        <button class="btn btn-amber" id="btn-download-wallpaper">
          📥 Download HD Wallpaper (.png)
        </button>
        <button class="btn btn-cyan" id="btn-print-cert">
          🖨️ Print Certificate (A4)
        </button>
        <button class="btn btn-lime" id="btn-retake-exam">
          🔄 Retake Exam
        </button>
        <button class="btn btn-glass btn-back-to-hub">
          Return to Hub 🏠
        </button>
      </div>
    </section>

  </main>

  <!-- JAVASCRIPT MODULES INLINED FOR 100% OFFLINE / STANDALONE FUNCTIONALITY -->
  <script>
{audio_js}
  </script>
  <script>
{curriculum_js}
  </script>
  <script>
{labs_js}
  </script>
  <script>
{cert_js}
  </script>
  <script>
{app_controller_js}
  </script>
</body>
</html>
"""

output_path = os.path.join(BASE_DIR, "safari_science_quest.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_shell)

print(f"Successfully generated standalone {output_path} ({len(html_shell)} bytes)")
