# 🦁 Safari Math Quest Academy

Interactive, gamified MEP Mathematics & Science educational game suite for Thai English Program students (Prathomsuksa 2 & 3). Designed strictly to Ministry of Education Thailand curriculum standards with vibrant Thai tropical Safari aesthetics, tactile responsive controls, audio narration, and printable high-definition certificates.

---

## 🎮 Direct Play Links (GitHub Pages)

* **🧪 Primary 3 Science Quest (Professor Pip's Einstein Quantum Lab, Food Groups, Life Cycles, Thermal Physics, Forces & Magnets):**  
  👉 **`https://landsmiles-blip.github.io/safari-math-quest/science/`**

* **👑 Primary 3 Math Quest (Numbers to 99,999, Place Value, Brackets & Operations, Word Problems):**  
  👉 **`https://landsmiles-blip.github.io/safari-math-quest/p3/`**

* **🐊 Primary 2 Math Quest (Numbers to 999, Odd/Even Ending Rules, Greedy Gator Comparisons, Multiplication):**  
  👉 **`https://landsmiles-blip.github.io/safari-math-quest/p2/`**

* **🧭 Safari Math Quest Academy Portal (All Grades Hub):**  
  👉 **`https://landsmiles-blip.github.io/safari-math-quest/`**

---

## 🌟 Game Structure & Educational Architecture

Every game in the Safari Academy implements a proven 2-mode educational mastery loop:

### 1. Mode 1: Training Grounds & Discovery Labs (Classroom Learning)
* **5 Pedagogical Focus Camps/Labs**: Tailored hands-on interactive simulations for each curriculum domain.
* **Natural Voice Narration**: Zero-dependency Web Audio API and natural soft English speech synthesis (`CA.spk`) supporting ESL students.
* **Dynamic Scenario Rotation**: Automatically rotates new real-world examples and varied scenarios across visits to maintain deep cognitive engagement.
* **Linear Lab Progression**: 1-tap "Next Lab ➔" sequencing guides young scholars smoothly from Camp/Lab 1 through 5.
* **First-Play Lock**: Mode 2 (Exam Challenge) is strictly locked until all 5 training camps/labs are completed and stamped on the player's passport.

### 2. Mode 2: Exam Challenge (Curriculum Assessment)
* **15 Graded Questions**: Rigorous, randomized questions dynamically generated across all 5 curriculum domains (exactly 3 questions per domain).
* **Strict Zero-Clue Visual Protection**: Diagrams in Mode 2 show only neutral physical apparatus and sequence markers (`Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4`), with dual-layer CSS suppression (`#sc-exam .disp-pill { display: none !important; }`) ensuring visuals never leak answer clues.
* **Exam Window Lockdown Mode**:
  - Fullscreen enforcement (`requestFullscreen`) on exam start.
  - History manipulation traps the browser back button (`popstate`).
  - Native browser leave confirmation dialog (`beforeunload`).
  - Fullscreen exit and window blur warning overlay (`#lockdown-overlay`) requiring return to fullscreen.
  - Zero exit buttons inside the exam screen until all 15 questions are answered.

### 3. Remediation Loop ("Bronze is Not Acceptable")
* **Gold Master Tier (14–15 / 15)**: Full Gold Lion Crown, celebratory fanfare, confetti explosion, and Gold Honors Certificate.
* **Silver Ranger Tier (11–13 / 15)**: Instant 1-tap "Retry Missed Questions ⚡" to turn mistakes into immediate mastery.
* **Bronze Remediation Tier (< 11 / 15)**: Reset stamps (`G.camps = []`) and automatic routing back to Discovery Labs to complete laboratory training before taking the exam again.

### 4. High-Definition Wallpaper Certificate
* **Canvas Resolution**: `1200 x 848` at 300 DPI.
* **Authentic Royal Embellishments**: Golden guilloché border, corner rosettes, smiling royal lion crest, official 32-point gold embossed seal, 15 dynamic domain stars, and 3D extruded gold student name.
* **Export Options**: 1-click PNG image download and seamless borderless print CSS for classroom display or desktop wallpaper.

---

## 📚 Subject Modules

### 🔬 Primary 3 Science Quest
* **Theme**: Professor Pip's Einstein Quantum Research Lab (vibranium fusion core, glowing condenser tubes, holographic chalkboard equations).
* **Lab 1: Living Needs Lab 🥗** — Food Groups (Carbohydrates, Proteins, Vitamins/Minerals, Fats, Water) and essential life requirements.
* **Lab 2: Safari Diets Diner 🐯** — Herbivores, Carnivores, and Omnivores with high-detail animal illustrations.
* **Lab 3: Life Cycle Studio 🦋** — Complete 4-stage and 5-stage life cycles (Chicken, Butterfly, Frog, Plant, Human).
* **Lab 4: The Thermal Lab 🍫** — Reversible vs. Irreversible state changes (melting chocolate in pan, freezing ice, cooking egg, baking bread).
* **Lab 5: Forces & Magnets Lab 🧲** — Pushes vs. Pulls, downward inclined ramp experiments with friction rug on the floor, and magnetic polarity.

### 👑 Primary 3 Mathematics Quest
* **Camp 1: Savannah Place Value 🌴** — Numbers up to 99,999, digit positions, and expanded notation.
* **Camp 2: River Nile Comparisons 🐊** — Greedy Gator symbol comparison (`>`, `<`, `=`) and 4-number ordering.
* **Camp 3: Baobab Tree Column Math 🌳** — 4-digit addition and subtraction with regrouping.
* **Camp 4: Cheetah Speed Multiplication & Division 🐆** — Multi-digit multiplication and long division with remainders.
* **Camp 5: Elephant Waterhole Combined Operations 🐘** — Order of operations (PEMDAS/BODMAS) with brackets and story problems.

### 🐊 Primary 2 Mathematics Quest
* **Camp 1: Gator Swamp Counting 🐊** — Numbers up to 999 and place value.
* **Camp 2: Zebra Stripes Odd & Even 🦓** — Unit digit ending rules (`0, 2, 4, 6, 8` vs. `1, 3, 5, 7, 9`).
* **Camp 3: Hippo Lagoon Comparisons 🦛** — 3-digit comparisons with Gator jaws.
* **Camp 4: Lion Pride Column Addition & Subtraction 🦁** — 3-digit column math with regrouping.
* **Camp 5: Monkey Jungle Multiplication 🐒** — 1-digit multiplication arrays and repeated addition.

---

## 💻 Technical Architecture
* **Single-File Architecture**: Each quest is 100% self-contained in a single zero-dependency HTML file.
* **Web Audio API**: Real-time synthesized acoustic tones (sine/triangle waves for positive chimes, low square waves for buzzer, harmonic chords for fanfare).
* **Cross-Device Ready**: Fully responsive across mobile touch devices (iOS/Android), tablets, Chromebooks, and widescreen interactive classroom whiteboards.
