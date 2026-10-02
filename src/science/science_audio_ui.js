/**
 * MEP Primary 3 Science Quest: Audio Engine & Procedural SFX Synthesizer
 * File: science_audio_ui.js
 * 
 * Provides:
 * 1. Zero-dependency procedural Web Audio API sound synthesis:
 *    - bubble: Organic chemistry beaker bubbling
 *    - magnetClack: Sharp metallic magnetic snap
 *    - repelPulse: Deep sci-fi magnetic repulsion forcefield pulse
 *    - carZoom: Toy car friction rolling & skidding
 *    - heatFlame: Bunsen burner thermal ignition surge & hiss
 *    - freezeChime: Crystalline icy shimmer chime
 *    - correct: Cheerful celebratory double chime
 *    - wrong: Soft friendly buzzy wobble (not harsh)
 *    - fanfare: Grand triumphant brass exam completion fanfare
 * 2. Speech Synthesis Engine:
 *    - Primary 3 student-tailored soft female voice (pitch 1.05, rate 0.92)
 *    - Auto-voice resolution (Google US English female, Microsoft Zira / Jenny, Apple Samantha)
 * 3. Mascot & UI Particle Visual Helpers:
 *    - Professor Leo & Pip the Gear Bot animated SVGs
 *    - Kinetic electric sparks & bubbling beakers
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.ScienceAudioUI = factory();
    // Expose convenient globals for easy access across all modules
    root.playSound = root.ScienceAudioUI.playSound.bind(root.ScienceAudioUI);
    root.speakText = root.ScienceAudioUI.speakText.bind(root.ScienceAudioUI);
  }
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  // Audio Context management (lazy initialization on user gesture)
  let audioCtx = null;
  let isAudioMuted = false;
  let masterVolume = 0.85;
  let speechDebounceTimer = null;
  let cachedVoices = [];
  let preferredVoice = null;
  let isSpeaking = false;

  /**
   * Initializes or resumes the AudioContext on user interaction.
   * Required for modern browser autoplay policies.
   */
  function getAudioContext() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume().catch(() => {});
    }
    return audioCtx;
  }

  // Auto-unlock on first document interaction
  if (typeof window !== 'undefined' && typeof document !== 'undefined') {
    const unlockAudio = () => {
      const ctx = getAudioContext();
      if (ctx && ctx.state === 'running') {
        document.removeEventListener('pointerdown', unlockAudio);
        document.removeEventListener('keydown', unlockAudio);
      }
    };
    document.addEventListener('pointerdown', unlockAudio, { passive: true });
    document.addEventListener('keydown', unlockAudio, { passive: true });
  }

  /* -------------------------------------------------------------
     SPEECH SYNTHESIS ENGINE
  ------------------------------------------------------------- */
  const FEMALE_VOICE_NAMES = [
    'zira', 'jenny', 'aria', 'samantha', 'victoria', 'karen',
    'fiona', 'moira', 'tessa', 'veena', 'female', 'woman',
    'catherine', 'susan', 'linda', 'hazel', 'stephanie', 'ava',
    'allison', 'serena', 'sangeeta', 'google us english female', 'google us english'
  ];

  const MALE_VOICE_NAMES = [
    'david', 'mark', 'guy', 'george', 'james', 'male', 'richard',
    'sean', 'stefan', 'paul', 'brian', 'daniel', 'alex'
  ];

  function refreshVoices() {
    if (!('speechSynthesis' in window)) return;
    try {
      const list = window.speechSynthesis.getVoices();
      if (!list || !list.length) return;
      cachedVoices = list;

      // Filter for English voices first
      const enPool = list.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
      const candidates = enPool.length > 0 ? enPool : list;

      // 1. Look for known soft friendly female voices
      let chosen = candidates.find(v => {
        const nm = v.name.toLowerCase();
        return FEMALE_VOICE_NAMES.some(fn => nm.includes(fn));
      });

      // 2. If not found, exclude strictly male names
      if (!chosen) {
        chosen = candidates.find(v => {
          const nm = v.name.toLowerCase();
          return !MALE_VOICE_NAMES.some(mn => nm.includes(mn));
        });
      }

      preferredVoice = chosen || candidates[0];
    } catch (e) {
      console.warn('ScienceAudioUI: Error refreshing voices', e);
    }
  }

  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    refreshVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.onvoiceschanged = refreshVoices;
    }
  }

  /**
   * Reads text aloud with warm, friendly female voice tuned for Primary 3 learners.
   * @param {string} text - Text to speak
   * @param {object} [options] - Optional { immediate, pitch, rate, onEnd }
   */
  function speakText(text, options = {}) {
    if (!('speechSynthesis' in window) || !text || isAudioMuted) return;

    const {
      immediate = false,
      pitch = 1.05,
      rate = 0.92,
      onEnd = null
    } = options;

    if (speechDebounceTimer) {
      clearTimeout(speechDebounceTimer);
      speechDebounceTimer = null;
    }

    try {
      if (window.speechSynthesis.paused) window.speechSynthesis.resume();
      window.speechSynthesis.cancel();
    } catch (e) {}

    const executeSpeak = () => {
      try {
        if (window.speechSynthesis.paused) window.speechSynthesis.resume();
        const utterance = new SpeechSynthesisUtterance(text.trim());
        utterance.rate = rate;
        utterance.pitch = pitch;
        utterance.lang = 'en-US';

        if (!preferredVoice && cachedVoices.length === 0) {
          refreshVoices();
        }
        if (preferredVoice) {
          utterance.voice = preferredVoice;
        }

        utterance.onstart = () => { isSpeaking = true; };
        utterance.onend = () => {
          isSpeaking = false;
          if (typeof onEnd === 'function') onEnd();
        };
        utterance.onerror = () => {
          isSpeaking = false;
        };

        window.speechSynthesis.speak(utterance);
      } catch (e) {
        isSpeaking = false;
        console.warn('ScienceAudioUI: Speech synthesis failed', e);
      }
    };

    if (immediate) {
      executeSpeak();
    } else {
      speechDebounceTimer = setTimeout(executeSpeak, 180);
    }
  }

  function stopSpeech() {
    if (!('speechSynthesis' in window)) return;
    try {
      if (speechDebounceTimer) {
        clearTimeout(speechDebounceTimer);
        speechDebounceTimer = null;
      }
      window.speechSynthesis.cancel();
      isSpeaking = false;
    } catch (e) {}
  }

  /* -------------------------------------------------------------
     PROCEDURAL WEB AUDIO SYNTHESIZER
  ------------------------------------------------------------- */

  // Helper to generate a buffer of white noise
  function createNoiseBuffer(ctx, duration = 1) {
    const bufferSize = ctx.sampleRate * duration;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    return buffer;
  }

  // Helper for simple tone envelope
  function playTone(freq, delay, duration, type = 'sine', vol = 0.2, pitchRamp = null) {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime + delay;

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);
    if (pitchRamp) {
      osc.frequency.exponentialRampToValueAtTime(pitchRamp, now + duration);
    }

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(vol * masterVolume, now + 0.015);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now);
    osc.stop(now + duration + 0.05);
  }

  /**
   * Sound 1: Beaker Bubbling ('bubble')
   * Generates multiple asynchronous organic liquid pops
   */
  function soundBubble() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;

    const bubbleCount = 4 + Math.floor(Math.random() * 3);
    for (let i = 0; i < bubbleCount; i++) {
      const delay = i * 0.055 + Math.random() * 0.04;
      const startF = 380 + Math.random() * 260;
      const endF = startF * (1.8 + Math.random() * 0.8);
      const dur = 0.06 + Math.random() * 0.04;
      const now = ctx.currentTime + delay;

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      const filter = ctx.createBiquadFilter();

      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(startF * 1.2, now);
      filter.Q.value = 6;

      osc.type = 'sine';
      osc.frequency.setValueAtTime(startF, now);
      osc.frequency.exponentialRampToValueAtTime(endF, now + dur);

      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.linearRampToValueAtTime(0.18 * masterVolume, now + 0.01);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + dur);

      osc.connect(filter);
      filter.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + dur + 0.02);
    }
  }

  /**
   * Sound 2: Magnet Snap Clack ('magnetClack')
   * Sharp transient attack with metallic resonance ping
   */
  function soundMagnetClack() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;

    // 1. Sharp impulse transient
    const noiseBuffer = createNoiseBuffer(ctx, 0.05);
    const noiseSource = ctx.createBufferSource();
    noiseSource.buffer = noiseBuffer;
    const noiseFilter = ctx.createBiquadFilter();
    noiseFilter.type = 'highpass';
    noiseFilter.frequency.setValueAtTime(2200, now);
    const noiseGain = ctx.createGain();
    noiseGain.gain.setValueAtTime(0.4 * masterVolume, now);
    noiseGain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);

    noiseSource.connect(noiseFilter);
    noiseFilter.connect(noiseGain);
    noiseGain.connect(ctx.destination);
    noiseSource.start(now);

    // 2. Metallic clack body (dual square/triangle mix)
    [1200, 1850, 2400].forEach((freq, idx) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = idx === 0 ? 'triangle' : 'sine';
      osc.frequency.setValueAtTime(freq, now);
      osc.frequency.exponentialRampToValueAtTime(freq * 0.45, now + 0.08);

      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.linearRampToValueAtTime((0.25 / (idx + 1)) * masterVolume, now + 0.003);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.12);

      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.14);
    });

    // 3. Metallic ring decay
    playTone(940, 0.01, 0.18, 'triangle', 0.12);
  }

  /**
   * Sound 3: Magnetic Repulsion Pulse ('repelPulse')
   * Deep sci-fi forcefield pulse with tremolo resistance
   */
  function soundRepelPulse() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;
    const dur = 0.55;

    // Bass forcefield pitch swoop
    const osc = ctx.createOscillator();
    const lfo = ctx.createOscillator();
    const lfoGain = ctx.createGain();
    const filter = ctx.createBiquadFilter();
    const gain = ctx.createGain();

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(140, now);
    osc.frequency.exponentialRampToValueAtTime(52, now + dur);

    // 16Hz tremolo wobble for magnetic resistance
    lfo.type = 'sine';
    lfo.frequency.setValueAtTime(16, now);
    lfoGain.gain.setValueAtTime(0.5, now);
    lfo.connect(gain.gain);

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(320, now);
    filter.frequency.exponentialRampToValueAtTime(160, now + dur);
    filter.Q.value = 4.5;

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(0.32 * masterVolume, now + 0.04);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + dur);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now);
    lfo.start(now);
    osc.stop(now + dur + 0.05);
    lfo.stop(now + dur + 0.05);

    // Sub-bass thump
    playTone(60, 0, dur * 0.8, 'sine', 0.28, 38);
  }

  /**
   * Sound 4: Toy Car Zoom & Friction ('carZoom')
   * Rolling wheels on texture ramping speed, then skidding stop
   */
  function soundCarZoom() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;
    const dur = 0.75;

    // 1. Friction rolling noise
    const noiseBuffer = createNoiseBuffer(ctx, dur);
    const noise = ctx.createBufferSource();
    noise.buffer = noiseBuffer;

    const bpf = ctx.createBiquadFilter();
    bpf.type = 'bandpass';
    bpf.Q.value = 3.5;
    bpf.frequency.setValueAtTime(320, now);
    bpf.frequency.linearRampToValueAtTime(1100, now + dur * 0.45);
    bpf.frequency.exponentialRampToValueAtTime(450, now + dur);

    const noiseGain = ctx.createGain();
    noiseGain.gain.setValueAtTime(0.001, now);
    noiseGain.gain.linearRampToValueAtTime(0.24 * masterVolume, now + 0.1);
    noiseGain.gain.exponentialRampToValueAtTime(0.001, now + dur);

    noise.connect(bpf);
    bpf.connect(noiseGain);
    noiseGain.connect(ctx.destination);
    noise.start(now);

    // 2. Whirring motor gearbox pitch sweep
    const motor = ctx.createOscillator();
    const motorGain = ctx.createGain();
    motor.type = 'triangle';
    motor.frequency.setValueAtTime(180, now);
    motor.frequency.exponentialRampToValueAtTime(540, now + dur * 0.4);
    motor.frequency.exponentialRampToValueAtTime(220, now + dur);

    motorGain.gain.setValueAtTime(0.001, now);
    motorGain.gain.linearRampToValueAtTime(0.14 * masterVolume, now + 0.08);
    motorGain.gain.exponentialRampToValueAtTime(0.001, now + dur);

    motor.connect(motorGain);
    motorGain.connect(ctx.destination);
    motor.start(now);
    motor.stop(now + dur + 0.02);
  }

  /**
   * Sound 5: Thermal Burner Surge & Hiss ('heatFlame')
   * Bunsen burner ignition surge followed by hot gas roar
   */
  function soundHeatFlame() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;
    const dur = 0.85;

    // 1. Gas flame turbulence noise
    const noiseBuffer = createNoiseBuffer(ctx, dur);
    const noise = ctx.createBufferSource();
    noise.buffer = noiseBuffer;

    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.Q.value = 2.0;
    filter.frequency.setValueAtTime(250, now);
    filter.frequency.linearRampToValueAtTime(1400, now + 0.25);
    filter.frequency.exponentialRampToValueAtTime(650, now + dur);

    const gain = ctx.createGain();
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(0.35 * masterVolume, now + 0.08);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + dur);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);
    noise.start(now);

    // 2. Low-frequency combustion rumble
    playTone(75, 0, dur * 0.9, 'sine', 0.22, 50);
  }

  /**
   * Sound 6: Delicate Icy Crystal Chime ('freezeChime')
   * Shimmering high crystalline bell harmonics
   */
  function soundFreezeChime() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;

    // Pentatonic icy bell ladder (E6, B6, D7, G7, B7)
    const pitches = [1318.5, 1975.5, 2349.3, 3136.0, 3951.1];
    pitches.forEach((freq, idx) => {
      const delay = idx * 0.042;
      const dur = 0.65 + idx * 0.08;
      const noteTime = now + delay;

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, noteTime);

      gain.gain.setValueAtTime(0.0001, noteTime);
      gain.gain.linearRampToValueAtTime((0.15 / (idx * 0.3 + 1)) * masterVolume, noteTime + 0.008);
      gain.gain.exponentialRampToValueAtTime(0.0001, noteTime + dur);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(noteTime);
      osc.stop(noteTime + dur + 0.02);
    });
  }

  /**
   * Sound 7: Cheerful Double High Chime ('correct')
   * Encouraging major triad reward chime
   */
  function soundCorrect() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;

    // G5 (784Hz) -> C6 (1046.5Hz) -> E6 (1318.5Hz) sparkle
    playTone(784.0, 0.0, 0.25, 'triangle', 0.22);
    playTone(1046.5, 0.09, 0.55, 'sine', 0.25);
    playTone(1318.5, 0.18, 0.65, 'sine', 0.20);
    playTone(2093.0, 0.24, 0.75, 'sine', 0.12);
  }

  /**
   * Sound 8: Soft Buzzy Wobble ('wrong')
   * Gentle, kid-friendly "boing-wobble" error prompt
   */
  function soundWrong() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;
    const dur = 0.42;

    const osc = ctx.createOscillator();
    const lfo = ctx.createOscillator();
    const lfoGain = ctx.createGain();
    const gain = ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(240, now);
    osc.frequency.exponentialRampToValueAtTime(160, now + dur);

    // 7.5Hz vibrato wobble
    lfo.type = 'sine';
    lfo.frequency.setValueAtTime(7.5, now);
    lfoGain.gain.setValueAtTime(22, now);
    lfo.connect(osc.frequency);

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(0.24 * masterVolume, now + 0.03);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + dur);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now);
    lfo.start(now);
    osc.stop(now + dur + 0.05);
    lfo.stop(now + dur + 0.05);
  }

  /**
   * Sound 9: Grand Brass Celebratory Fanfare ('fanfare')
   * Triumphant brass sequence with overtone shimmer for exam completion
   */
  function soundFanfare() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    const now = ctx.currentTime;

    // Brass notes sequence: C5, E5, G5, C6 (chord hold + shimmer)
    const melody = [
      { f: 523.25, d: 0.00, dur: 0.16 }, // C5
      { f: 659.25, d: 0.14, dur: 0.16 }, // E5
      { f: 783.99, d: 0.28, dur: 0.18 }, // G5
      { f: 1046.5, d: 0.44, dur: 0.85 }  // C6
    ];

    melody.forEach(note => {
      const noteTime = now + note.d;
      // Dual oscillator for brassy fullness
      ['sawtooth', 'triangle'].forEach((type, tIdx) => {
        const osc = ctx.createOscillator();
        const filter = ctx.createBiquadFilter();
        const gain = ctx.createGain();

        osc.type = type;
        osc.frequency.setValueAtTime(note.f, noteTime);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(600, noteTime);
        filter.frequency.linearRampToValueAtTime(2200, noteTime + 0.04);
        filter.frequency.exponentialRampToValueAtTime(800, noteTime + note.dur);

        gain.gain.setValueAtTime(0.0001, noteTime);
        gain.gain.linearRampToValueAtTime((tIdx === 0 ? 0.16 : 0.22) * masterVolume, noteTime + 0.025);
        gain.gain.exponentialRampToValueAtTime(0.0001, noteTime + note.dur);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);

        osc.start(noteTime);
        osc.stop(noteTime + note.dur + 0.05);
      });
    });

    // Final grand harmony sustain chord: C4, G4, E5, G5, C6 + chime sparkles
    const chordTime = now + 0.44;
    const chordPitches = [261.63, 392.00, 659.25, 783.99, 1046.5, 1318.5];
    chordPitches.forEach((freq, idx) => {
      playTone(freq, 0.44 + idx * 0.02, 1.25, 'triangle', 0.14);
    });

    // Sparkle chimes cascading at the peak
    [2093, 2637, 3136, 4186].forEach((f, idx) => {
      playTone(f, 0.72 + idx * 0.08, 0.7, 'sine', 0.1);
    });
  }

  // Extra Tactile SFX for sleek lab interaction
  function soundClick() {
    playTone(1200, 0, 0.03, 'sine', 0.15, 600);
  }

  function soundLaserScan() {
    const ctx = getAudioContext();
    if (!ctx || isAudioMuted) return;
    playTone(1800, 0, 0.18, 'sawtooth', 0.14, 280);
  }

  function soundBadgeUnlock() {
    playTone(523.25, 0, 0.25, 'triangle', 0.18);
    playTone(659.25, 0.08, 0.3, 'triangle', 0.2);
    playTone(1046.5, 0.16, 0.6, 'sine', 0.25);
    playTone(1567.98, 0.26, 0.8, 'sine', 0.18);
  }

  function soundDialTick() {
    playTone(1600, 0, 0.025, 'square', 0.08, 1100);
  }

  /**
   * Main dispatch method for all procedural sound effects.
   * @param {string} soundName
   * @param {object} [options]
   */
  function playSound(soundName, options = {}) {
    try {
      getAudioContext();
      switch (soundName) {
        case 'bubble':
          soundBubble();
          break;
        case 'magnetClack':
          soundMagnetClack();
          break;
        case 'repelPulse':
          soundRepelPulse();
          break;
        case 'carZoom':
          soundCarZoom();
          break;
        case 'heatFlame':
          soundHeatFlame();
          break;
        case 'freezeChime':
          soundFreezeChime();
          break;
        case 'correct':
          soundCorrect();
          break;
        case 'wrong':
          soundWrong();
          break;
        case 'fanfare':
          soundFanfare();
          break;
        // Helpful aliases & extras
        case 'click':
        case 'tap':
          soundClick();
          break;
        case 'laser':
        case 'scan':
          soundLaserScan();
          break;
        case 'badge':
        case 'unlock':
          soundBadgeUnlock();
          break;
        case 'dial':
          soundDialTick();
          break;
        default:
          console.warn(`ScienceAudioUI: Unknown sound key "${soundName}"`);
      }
    } catch (e) {
      console.warn('ScienceAudioUI: Error playing sound', e);
    }
  }

  /* -------------------------------------------------------------
     MASCOT & VISUAL SPARK GENERATORS
  ------------------------------------------------------------- */

  /**
   * Generates Professor Leo SVG markup.
   * Professor Leo: Wise lion scientist in lab coat and electric cyan goggles.
   * @param {string} [mood='happy'] - 'happy' | 'talking' | 'thinking' | 'remediate'
   * @param {number} [size=96]
   * @returns {string} SVG HTML string
   */
  function renderMascotLeo(mood = 'happy', size = 96) {
    const isWorry = mood === 'remediate';
    const mouthPath = isWorry
      ? 'M42,66 Q50,60 58,66'
      : 'M40,62 Q50,72 60,62';

    return `
    <svg class="mascot-svg mascot-leo mood-${mood}" viewBox="0 0 100 100" width="${size}" height="${size}" aria-label="Professor Leo">
      <defs>
        <radialGradient id="leoMane" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#f59e0b"/>
          <stop offset="85%" stop-color="#b45309"/>
          <stop offset="100%" stop-color="#78350f"/>
        </radialGradient>
        <radialGradient id="leoFace" cx="50%" cy="40%" r="50%">
          <stop offset="0%" stop-color="#fed7aa"/>
          <stop offset="100%" stop-color="#fba863"/>
        </radialGradient>
        <linearGradient id="coatGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc"/>
          <stop offset="100%" stop-color="#cbd5e1"/>
        </linearGradient>
        <linearGradient id="goggleGlass" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="rgba(0, 245, 212, 0.85)"/>
          <stop offset="100%" stop-color="rgba(6, 182, 212, 0.45)"/>
        </linearGradient>
      </defs>

      <!-- Fluffy Scientist Lion Mane -->
      <circle cx="50" cy="46" r="38" fill="url(#leoMane)" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.4))"/>
      
      <!-- Ears -->
      <circle cx="20" cy="22" r="10" fill="#b45309"/>
      <circle cx="20" cy="22" r="6" fill="#fba863"/>
      <circle cx="80" cy="22" r="10" fill="#b45309"/>
      <circle cx="80" cy="22" r="6" fill="#fba863"/>

      <!-- Lion Head Face -->
      <circle cx="50" cy="48" r="28" fill="url(#leoFace)"/>

      <!-- Whiskers -->
      <path d="M26,56 L10,54 M26,60 L12,62 M74,56 L90,54 M74,60 L88,62" stroke="#78350f" stroke-width="1.8" stroke-linecap="round"/>

      <!-- Eyes & Expressive Eyebrows -->
      <ellipse cx="38" cy="44" rx="4" ry="5" fill="#1e293b"/>
      <ellipse cx="62" cy="44" rx="4" ry="5" fill="#1e293b"/>
      <circle cx="39.5" cy="42.5" r="1.5" fill="#ffffff"/>
      <circle cx="63.5" cy="42.5" r="1.5" fill="#ffffff"/>

      <!-- White Lab Coat with Gold Badge -->
      <path d="M28,78 C30,70 40,68 50,68 C60,68 70,70 72,78 L78,100 L22,100 Z" fill="url(#coatGrad)"/>
      <path d="M44,68 L50,84 L56,68" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
      <circle cx="62" cy="80" r="3.5" fill="#ffb703" stroke="#b45309" stroke-width="0.8"/>

      <!-- Safety Goggles resting on forehead or eyes -->
      <g class="goggles-group">
        <rect x="25" y="32" width="22" height="15" rx="5" fill="url(#goggleGlass)" stroke="#00f5d4" stroke-width="2"/>
        <rect x="53" y="32" width="22" height="15" rx="5" fill="url(#goggleGlass)" stroke="#00f5d4" stroke-width="2"/>
        <line x1="47" y1="39" x2="53" y2="39" stroke="#00f5d4" stroke-width="2.5"/>
        <path d="M12,40 L25,40 M75,40 L88,40" stroke="#00f5d4" stroke-width="2"/>
        <!-- Goggle shine -->
        <line x1="28" y1="36" x2="34" y2="36" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="56" y1="36" x2="62" y2="36" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
      </g>

      <!-- Snout & Mouth -->
      <ellipse cx="50" cy="56" rx="9" ry="6" fill="#fed7aa"/>
      <polygon points="50,52 46,48 54,48" fill="#78350f"/>
      <path d="${mouthPath}" fill="none" stroke="#78350f" stroke-width="2" stroke-linecap="round"/>
    </svg>
    `.trim();
  }

  /**
   * Generates Pip the Gear Bot SVG markup.
   * Pip: Floating magnetic gear bot with neon hyper-cyan eyes and rotating gear teeth.
   * @param {string} [mood='happy']
   * @param {number} [size=96]
   * @returns {string} SVG HTML string
   */
  function renderMascotPip(mood = 'happy', size = 96) {
    return `
    <svg class="mascot-svg mascot-pip mood-${mood}" viewBox="0 0 100 100" width="${size}" height="${size}" aria-label="Pip the Gear Bot">
      <defs>
        <radialGradient id="pipBody" cx="40%" cy="35%" r="65%">
          <stop offset="0%" stop-color="#38bdf8"/>
          <stop offset="60%" stop-color="#0284c7"/>
          <stop offset="100%" stop-color="#0f172a"/>
        </radialGradient>
        <filter id="neonPipCyan" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>

      <!-- Floating Thrust Ring -->
      <ellipse cx="50" cy="85" rx="16" ry="5" fill="none" stroke="#00f5d4" stroke-width="2.5" opacity="0.75"/>
      <polygon points="44,82 56,82 50,94" fill="#00f5d4" opacity="0.65"/>

      <!-- Pip's Magnetic Antenna with glowing LED sphere -->
      <line x1="50" y1="24" x2="50" y2="10" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
      <circle cx="50" cy="9" r="5" fill="#ffb703" filter="url(#neonPipCyan)"/>

      <!-- Pip Gear Ring Chassis -->
      <g class="gear-ring">
        <circle cx="50" cy="50" r="32" fill="url(#pipBody)" stroke="#38bdf8" stroke-width="2.5"/>
        <!-- Outer Gear Cogs -->
        <rect x="46" y="14" width="8" height="6" rx="2" fill="#0284c7"/>
        <rect x="46" y="80" width="8" height="6" rx="2" fill="#0284c7"/>
        <rect x="14" y="46" width="6" height="8" rx="2" fill="#0284c7"/>
        <rect x="80" y="46" width="6" height="8" rx="2" fill="#0284c7"/>
        <rect x="23" y="23" width="7" height="7" rx="2" transform="rotate(45 26.5 26.5)" fill="#0284c7"/>
        <rect x="70" y="23" width="7" height="7" rx="2" transform="rotate(45 73.5 26.5)" fill="#0284c7"/>
        <rect x="23" y="70" width="7" height="7" rx="2" transform="rotate(45 26.5 73.5)" fill="#0284c7"/>
        <rect x="70" y="70" width="7" height="7" rx="2" transform="rotate(45 73.5 73.5)" fill="#0284c7"/>
      </g>

      <!-- Gloss Visor Screen -->
      <rect x="24" y="34" width="52" height="28" rx="14" fill="#0b1120" stroke="#00f5d4" stroke-width="2"/>

      <!-- Expressive Neon LED Eyes -->
      <ellipse cx="38" cy="48" rx="6" ry="8" fill="#00f5d4" filter="url(#neonPipCyan)"/>
      <ellipse cx="62" cy="48" rx="6" ry="8" fill="#00f5d4" filter="url(#neonPipCyan)"/>
      <circle cx="40" cy="45" r="2" fill="#ffffff"/>
      <circle cx="64" cy="45" r="2" fill="#ffffff"/>

      <!-- Magnetic Side Flappers / Hands -->
      <path d="M16,50 Q10,40 18,34" fill="none" stroke="#f72585" stroke-width="3" stroke-linecap="round"/>
      <path d="M84,50 Q90,40 82,34" fill="none" stroke="#f72585" stroke-width="3" stroke-linecap="round"/>
    </svg>
    `.trim();
  }

  /**
   * Spawns kinetic particle sparks at a click / target coordinate.
   * @param {number} x
   * @param {number} y
   * @param {string} [color='#00f5d4']
   */
  function spawnSparks(x, y, color = '#00f5d4') {
    if (typeof document === 'undefined') return;
    const container = document.body;
    const sparkCount = 8;

    for (let i = 0; i < sparkCount; i++) {
      const spark = document.createElement('div');
      spark.className = 'kinetic-spark';
      spark.style.left = `${x}px`;
      spark.style.top = `${y}px`;
      spark.style.backgroundColor = color;
      spark.style.boxShadow = `0 0 10px ${color}`;

      const angle = (i / sparkCount) * 2 * Math.PI + (Math.random() - 0.5);
      const distance = 30 + Math.random() * 45;
      const dx = Math.cos(angle) * distance;
      const dy = Math.sin(angle) * distance;

      spark.style.setProperty('--dx', `${dx}px`);
      spark.style.setProperty('--dy', `${dy}px`);

      container.appendChild(spark);
      setTimeout(() => {
        if (spark.parentNode) spark.parentNode.removeChild(spark);
      }, 650);
    }
  }

  /* -------------------------------------------------------------
     SETTINGS & VOLUME HELPERS
  ------------------------------------------------------------- */
  function toggleMute() {
    isAudioMuted = !isAudioMuted;
    if (isAudioMuted) {
      stopSpeech();
    }
    return isAudioMuted;
  }

  function setMuted(state) {
    isAudioMuted = Boolean(state);
    if (isAudioMuted) {
      stopSpeech();
    }
  }

  function isMuted() {
    return isAudioMuted;
  }

  function setVolume(v) {
    masterVolume = Math.max(0, Math.min(1, v));
  }

  function getVolume() {
    return masterVolume;
  }

  return {
    // Audio synthesizer
    playSound,
    getAudioContext,
    initAudio: getAudioContext,

    // Speech engine
    speakText,
    stopSpeech,
    isSpeaking: () => isSpeaking,

    // Controls
    toggleMute,
    setMuted,
    isMuted,
    setVolume,
    getVolume,

    // Mascots & Visual helpers
    renderMascotLeo,
    renderMascotPip,
    spawnSparks
  };
});
