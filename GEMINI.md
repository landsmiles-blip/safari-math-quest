# Workspace Rule: Aesthetic & Architecture Preservation for Subject Expansions

## Invariant Directives:
1. **Visual Theme Continuity**:
   All MEP educational games and subject adaptations (e.g., Math, Science, English) must strictly preserve the approved Thai tropical Safari aesthetic:
   - Sky gradient: `linear-gradient(180deg, #023e8a 0%, #0096c7 20%, #48cae4 42%, #90e0ef 60%, #74c69d 70%, #52b788 80%, #2d6a4f 92%, #1b4332 100%)`.
   - Cheerful smiling sun with rosy cheeks, fluffy felt clouds, twinkling stars, layered ground, palm trees, and animated safari animals (`🦁`, `🐘`, `🦋`, `🌸`).
   - Typography: `Fredoka One` for bold golden titles, `Nunito` (weights 700/800/900) for high legibility.
   - Button styles: Rounded pill tactile buttons with 3D drop-shadows (`.btn`, `.bg`, `.by`, `.bb`, `.bpk`, `.bpu`, `.bo`, `.btn-gold`).

2. **Game Architecture & Screen Hierarchy**:
   All games must preserve the proven 2-mode progression:
   - **Name Modal**: Personalized student identification with lion mascot.
   - **Top Bar**: Game title, passport stamp indicator, and player name pill.
   - **Start Screen**: Hero crown & title + 2 mode cards:
     - **Mode 1: Training Grounds**: 5 topical practice camps with interactive classroom lessons, SVG diagrams, teaching guides, audio read-aloud, and passport star stamps.
     - **Mode 2: Exam Challenge**: 15 graded questions covering curriculum standards with progressive difficulty.
   - **Remediation Invariant**: "Bronze is not acceptable" — any score below 12 marks triggers a targeted remediation card that identifies the student's weakest camp and provides a 1-tap direct retrain button.
   - **Certificate Invariant**: High-definition A4 landscape Canvas certificate (`1200 x 848` at 300 DPI) with golden guilloché border, corner rosettes, smiling royal lion crest, official 32-point gold embossed seal, 15 dynamic domain stars, 3D extruded gold student name, 1-click PNG download, and borderless print CSS.


3. **Audio & Narration Invariant**:
   - Audio must use the zero-dependency Web Audio API synthesizer for positive chimes, error buzzes, and fanfare.
   - Voice narration must use natural soft female English speech synthesis (`CA.spk`).

4. **Science Subject Expansion & Laboratory Invariants**:
   - **Mode 1 Name & Identity**: Designated as **Professor Pip's Einstein Discovery Lab** (or Discovery Labs), themed as an energetic, euphoric science lab with Professor Pip in scientist goggles/lab coat, bubbling flasks, and neon accents.
   - **Linear Lab Progression**: Each completed lab must offer a direct 1-tap "Next Lab ➔" button to guide the student sequentially from Lab 1 to 5.
   - **First-Play Lock**: Exam Mode is strictly locked until all 5 Discovery Labs are completed.
   - **Dynamic Examples**: Mode 1 labs must rotate dynamic, varied real-world examples across multiple plays.
   - **Accurate Life Cycles**:
     - Chicken: Egg ➔ Hatchling ➔ Chick ➔ Chicken
     - Butterfly: Egg ➔ Caterpillar (larva) ➔ Pupa ➔ Butterfly
     - Frog: Egg ➔ Tadpole (gills) ➔ Froglet ➔ Adult Frog (lungs)
     - Human: Baby (Infant) ➔ Child ➔ Adolescent ➔ Adult ➔ Old Person
     - Plant: Seed ➔ Sprout ➔ Seedling ➔ Adult Plant
   - **Card & Diagram Layout**: Dual-card structure with generous breathing room, distinct concept pills, dual-item representation (e.g., both bread and a rice bowl), and non-clipping background elements.
   - **Physical Apparatus Accuracy**: Ramp incline experiments must slope downward toward the flat floor, with friction materials (rough towels, rugs, sandpaper) placed flat on the floor at the bottom/exit of the ramp, matching school examination standards.
   - **Exam Mode Zero-Spoiler Invariant**: In Mode 2 (Exam Challenge), visual diagrams must NEVER display `.disp-pill` concept badges or answer spoiler text inside the graphics (e.g., no 'Carbohydrate', 'Protein', 'Carnivore', 'Push', 'Melting', 'Irreversible', or stage names). In chronological life cycles, label only with neutral sequence markers (`Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4`). Dual-layer CSS protection (`#sc-exam .disp-pill { display: none !important; }`) and SVG `isExam = true` flags must be enforced across all questions.
   - **Large-Scale Scientific Visuals**: Graphics in the spotlight box must utilize abundant card space (60–80% container height) rather than appearing as small dots in an empty void.
   - **Full Quantum Science Lab Aesthetic**: The science visual theme must feel like a geeky, high-energy research lab featuring a pulsating vibranium nuclear fusion reactor, big glowing glass condensers with coiled spirals, cybernetic grids, and glowing holographic chalkboard equations ($E=mc^2$, $F=ma$, $\Delta Q = mc\Delta T$, $F_g = G\frac{m_1 m_2}{r^2}$).
