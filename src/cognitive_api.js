/**
 * Safari Math Quest - Cognitive API
 * Implementation of Web Speech API audio prompt, Web Audio API chimes,
 * and untimed canvas scratchpad drawing logic.
 */

(function (window) {
    'use strict';

    // Shared AudioContext instance (lazy initialization)
    let audioCtx = null;
    let speechTimer = null;

    /**
     * Get or initialize the AudioContext safely across browser vendors.
     * Resumes the context if suspended by browser autoplay policy.
     * @returns {AudioContext|null}
     */
    function getAudioContext() {
        try {
            if (!audioCtx) {
                const AudioContextClass = window.AudioContext || window.webkitAudioContext;
                if (AudioContextClass) {
                    audioCtx = new AudioContextClass();
                }
            }
            if (audioCtx && audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        } catch (err) {
            console.warn('AudioContext initialization failed:', err);
            return null;
        }
    }

    /**
     * Play audio prompt using Web Speech API (speechSynthesis).
     * Requirements:
     * - Delays 700ms before speaking
     * - Rate: 0.84 (relaxed pacing for cognitive processing)
     * - Pitch: 1.05 (friendly, engaging tone)
     * 
     * @param {string} text - Text to be spoken
     */
    function playAudioPrompt(text) {
        if (!('speechSynthesis' in window)) {
            console.warn('Web Speech API is not supported in this environment.');
            return;
        }

        // Cancel pending timers and ongoing speech
        if (speechTimer) {
            clearTimeout(speechTimer);
            speechTimer = null;
        }
        try {
            window.speechSynthesis.cancel();
        } catch (e) {
            // Ignore cancel errors
        }

        if (!text || typeof text !== 'string' || text.trim() === '') {
            return;
        }

        speechTimer = setTimeout(function () {
            try {
                const utterance = new SpeechSynthesisUtterance(text.trim());
                utterance.rate = 0.84;
                utterance.pitch = 1.05;
                utterance.lang = 'en-US';

                // Try to find a high quality English voice if voices are loaded
                const voices = window.speechSynthesis.getVoices();
                if (voices && voices.length > 0) {
                    const preferredVoice = voices.find(function (v) {
                        return v.lang.startsWith('en') && (
                            v.name.includes('Natural') ||
                            v.name.includes('Google') ||
                            v.name.includes('Samantha') ||
                            v.name.includes('Jenny') ||
                            v.default
                        );
                    }) || voices.find(function (v) {
                        return v.lang.startsWith('en');
                    });

                    if (preferredVoice) {
                        utterance.voice = preferredVoice;
                    }
                }

                window.speechSynthesis.speak(utterance);
            } catch (err) {
                console.warn('Speech synthesis speak error:', err);
            }
        }, 700);
    }

    /**
     * Stop any pending or active speech synthesis prompt.
     */
    function stopAudioPrompt() {
        if (speechTimer) {
            clearTimeout(speechTimer);
            speechTimer = null;
        }
        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
            } catch (e) {}
        }
    }

    /**
     * Play an uplifting C-E-G major triad chime using Web Audio API.
     * Frequencies:
     * - C5: ~523.25 Hz
     * - E5: ~659.25 Hz
     * - G5: ~783.99 Hz
     */
    function playSuccessChime() {
        const ctx = getAudioContext();
        if (!ctx) return;

        const now = ctx.currentTime;
        // C-E-G frequencies (C5, E5, G5) with an optional root C4 anchor for richness
        const chordNotes = [
            { freq: 523.25, delay: 0.00, duration: 0.65 }, // C5
            { freq: 659.25, delay: 0.08, duration: 0.65 }, // E5
            { freq: 783.99, delay: 0.16, duration: 0.80 }, // G5
            { freq: 1046.50, delay: 0.24, duration: 0.90 } // C6 (sparkling accent)
        ];

        chordNotes.forEach(function (note) {
            try {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();

                osc.type = 'triangle'; // Warm, marimba-like bell tone
                osc.frequency.setValueAtTime(note.freq, now + note.delay);

                // Smooth attack and exponential decay envelope
                gain.gain.setValueAtTime(0.0001, now + note.delay);
                gain.gain.linearRampToValueAtTime(0.18, now + note.delay + 0.02);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + note.delay + note.duration);

                osc.connect(gain);
                gain.connect(ctx.destination);

                osc.start(now + note.delay);
                osc.stop(now + note.delay + note.duration + 0.05);
            } catch (err) {
                console.warn('Error playing success note:', err);
            }
        });
    }

    /**
     * Play a gentle descending 261Hz to 220Hz chime using Web Audio API.
     * 261Hz (C4) down to 220Hz (A3).
     */
    function playErrorChime() {
        const ctx = getAudioContext();
        if (!ctx) return;

        const now = ctx.currentTime;
        const duration = 0.40;

        try {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = 'sine'; // Soft, warm sine tone so it's not jarring

            // Descending frequency glide: 261 Hz down to 220 Hz
            osc.frequency.setValueAtTime(261, now);
            osc.frequency.exponentialRampToValueAtTime(220, now + duration * 0.75);

            // Envelope: gentle attack, sustain, smooth decay
            gain.gain.setValueAtTime(0.0001, now);
            gain.gain.linearRampToValueAtTime(0.22, now + 0.03);
            gain.gain.setValueAtTime(0.20, now + duration * 0.4);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.start(now);
            osc.stop(now + duration + 0.05);
        } catch (err) {
            console.warn('Error playing error chime:', err);
        }
    }

    /**
     * Helper to compute accurate canvas coordinates across mouse and touch events,
     * accounting for CSS scaling and bounding rect.
     */
    function getCanvasCoordinates(e, canvas) {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / (rect.width || 1);
        const scaleY = canvas.height / (rect.height || 1);

        let clientX = 0;
        let clientY = 0;

        if (e.touches && e.touches.length > 0) {
            clientX = e.touches[0].clientX;
            clientY = e.touches[0].clientY;
        } else if (e.changedTouches && e.changedTouches.length > 0) {
            clientX = e.changedTouches[0].clientX;
            clientY = e.changedTouches[0].clientY;
        } else {
            clientX = e.clientX;
            clientY = e.clientY;
        }

        return {
            x: (clientX - rect.left) * scaleX,
            y: (clientY - rect.top) * scaleY
        };
    }

    /**
     * Initialize scratchpad drawing logic on a canvas element for untimed math calculation.
     * Supports mousedown, mousemove, mouseup, mouseleave, touchstart, touchmove, touchend, touchcancel.
     * 
     * @param {string|HTMLCanvasElement} canvasId - Canvas DOM element ID or canvas element instance
     * @returns {object|null} Scratchpad controls { clear, setStrokeStyle, setLineWidth }
     */
    function initScratchpad(canvasId) {
        const canvas = typeof canvasId === 'string' ? document.getElementById(canvasId) : canvasId;
        if (!canvas || !canvas.getContext) {
            console.warn('initScratchpad: canvas element not found or invalid:', canvasId);
            return null;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) return null;

        // Auto-initialize canvas dimensions if not set
        if (!canvas.width || !canvas.height) {
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width || 600;
            canvas.height = rect.height || 400;
        }

        // Default drawing styling: high contrast, legible math pencil/pen style
        let strokeColor = '#1e3a8a'; // Deep blue / ink color
        let lineWidth = 3.5;

        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;

        function startDrawing(e) {
            isDrawing = true;
            const pos = getCanvasCoordinates(e, canvas);
            lastX = pos.x;
            lastY = pos.y;

            // Draw a subtle dot on initial click/tap
            ctx.save();
            ctx.fillStyle = strokeColor;
            ctx.beginPath();
            ctx.arc(lastX, lastY, lineWidth / 2, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }

        function draw(e) {
            if (!isDrawing) return;
            const pos = getCanvasCoordinates(e, canvas);

            ctx.save();
            ctx.strokeStyle = strokeColor;
            ctx.lineWidth = lineWidth;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            ctx.restore();

            lastX = pos.x;
            lastY = pos.y;
        }

        function stopDrawing() {
            isDrawing = false;
        }

        // Mouse event listeners
        canvas.addEventListener('mousedown', function (e) {
            startDrawing(e);
        });

        canvas.addEventListener('mousemove', function (e) {
            draw(e);
        });

        canvas.addEventListener('mouseup', function () {
            stopDrawing();
        });

        canvas.addEventListener('mouseleave', function () {
            stopDrawing();
        });

        // Touch event listeners (prevent scrolling on scratchpad)
        canvas.addEventListener('touchstart', function (e) {
            e.preventDefault();
            startDrawing(e);
        }, { passive: false });

        canvas.addEventListener('touchmove', function (e) {
            e.preventDefault();
            draw(e);
        }, { passive: false });

        canvas.addEventListener('touchend', function (e) {
            e.preventDefault();
            stopDrawing();
        }, { passive: false });

        canvas.addEventListener('touchcancel', function (e) {
            stopDrawing();
        });

        // Clear helper
        function clear() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        const controller = {
            clear: clear,
            setStrokeStyle: function (color) {
                strokeColor = color;
            },
            setLineWidth: function (width) {
                lineWidth = width;
            },
            getCanvas: function () {
                return canvas;
            },
            getContext: function () {
                return ctx;
            }
        };

        // Attach controller to canvas for convenience
        canvas._scratchpad = controller;

        return controller;
    }

    /**
     * Clear the scratchpad canvas by element or ID.
     * @param {string|HTMLCanvasElement} canvasId
     */
    function clearScratchpad(canvasId) {
        const canvas = typeof canvasId === 'string' ? document.getElementById(canvasId) : canvasId;
        if (canvas) {
            if (canvas._scratchpad) {
                canvas._scratchpad.clear();
            } else {
                const ctx = canvas.getContext('2d');
                if (ctx) ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
        }
    }

    // Expose CognitiveAPI on window object
    window.CognitiveAPI = {
        playAudioPrompt: playAudioPrompt,
        stopAudioPrompt: stopAudioPrompt,
        playSuccessChime: playSuccessChime,
        playErrorChime: playErrorChime,
        initScratchpad: initScratchpad,
        clearScratchpad: clearScratchpad,
        getAudioContext: getAudioContext
    };

})(typeof window !== 'undefined' ? window : this);
