const ScienceCurriculum = (function() {
    let currentQuestions = [];

    function randomItem(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    function shuffle(arr) {
        return [...arr].sort(() => Math.random() - 0.5);
    }

    function createQ(id, level, domain, title, type, scenarioText, diag, subQData) {
        const subQuestions = subQData.map(sq => {
            const opts = sq.options;
            const correctOpt = opts[0];
            const shuffled = shuffle(opts);
            return {
                part: sq.part,
                prompt: sq.prompt,
                options: shuffled,
                correctIndex: shuffled.indexOf(correctOpt),
                hint: sq.hint,
                explanation: sq.explanation
            };
        });
        return { id, level, domain, type, title, scenarioText, diagramSvg: diag, subQuestions };
    }

    function generateExam() {
        const qs = [];
        
        // Level 1: Needs & Food Groups
        const foods = ["Rice", "Bread", "Noodles"];
        const proteins = ["Meat", "Fish", "Eggs"];
        const vitamins = ["Fruits", "Vegetables", "Salad"];

        qs.push(createQ(1, 1, 'needs', "Basic Needs", 'single', null, null, [{
            part: "", prompt: "What are the four basic needs for humans and animals to survive?",
            options: ["Food, Water, Air, Habitat", "Food, Juice, Clothes, Car", "Water, Sun, Toys, House", "Air, Meat, Sleep, Dirt"],
            hint: "We need these to breathe, drink, eat, and live safely.",
            explanation: "Food, Water, Air, and a Habitat (shelter) are essential for life."
        }]));
        qs.push(createQ(2, 1, 'needs', "Energy Foods", 'single', null, null, [{
            part: "", prompt: `Which food gives us carbohydrates for energy?`,
            options: [randomItem(foods), randomItem(proteins), randomItem(vitamins), "Water"],
            hint: "This food group includes grains.",
            explanation: "Carbohydrates like rice, bread, and noodles give us energy."
        }]));
        qs.push(createQ(3, 1, 'needs', "Growth and Protection", 'single', null, null, [{
            part: "", prompt: `Which food group helps our body grow strong?`,
            options: ["Proteins (like " + randomItem(proteins) + ")", "Vitamins (like " + randomItem(vitamins) + ")", "Carbohydrates (like " + randomItem(foods) + ")", "Fats and Sugars"],
            hint: "Muscles need this to grow.",
            explanation: "Proteins help our body grow and repair itself."
        }]));
        
        // Level 2: Animal Diets & Care
        const herb = randomItem(["Cow", "Sheep", "Horse", "Rabbit"]);
        const carn = randomItem(["Tiger", "Lion", "Shark", "Eagle"]);
        
        qs.push(createQ(4, 2, 'animals', "Animal Diets: Herbivores", 'single', null, null, [{
            part: "", prompt: `A ${herb} eats only plants. What do we call this type of animal?`,
            options: ["Herbivore", "Carnivore", "Omnivore", "Insectivore"],
            hint: "The word starts with 'Herb' which means plant.",
            explanation: "Herbivores are animals that eat only plants."
        }]));
        qs.push(createQ(5, 2, 'animals', "Animal Diets: Carnivores", 'single', null, null, [{
            part: "", prompt: `A ${carn} eats only other animals. What do we call this type of animal?`,
            options: ["Carnivore", "Herbivore", "Omnivore", "Frugivore"],
            hint: "The word starts with 'Carni' which relates to flesh/meat.",
            explanation: "Carnivores eat meat from other animals."
        }]));
        qs.push(createQ(6, 2, 'animals', "Animal Care", 'single', null, null, [{
            part: "", prompt: `What is the best way to care for a pet animal?`,
            options: ["Provide fresh water, correct food, and a clean home", "Give it only water and keep it in a small box", "Feed it human junk food and ignore it", "Let it find its own food every day"],
            hint: "Pets rely on us for their basic needs.",
            explanation: "Animals need a balanced diet, clean water, and a safe habitat."
        }]));

        // Level 3: Life Cycles
        qs.push(createQ(7, 3, 'cycles', "Butterfly Life Cycle", 'single', null, null, [{
            part: "", prompt: `What is the correct order of a butterfly's life cycle?`,
            options: ["Egg -> Caterpillar -> Chrysalis -> Adult", "Egg -> Chrysalis -> Caterpillar -> Adult", "Caterpillar -> Egg -> Adult -> Chrysalis", "Adult -> Caterpillar -> Egg -> Chrysalis"],
            hint: "It hatches, crawls, wraps itself, and then flies.",
            explanation: "A butterfly starts as an egg, becomes a caterpillar, transforms in a chrysalis, and emerges as an adult."
        }]));
        qs.push(createQ(8, 3, 'cycles', "Frog Life Cycle", 'single', null, null, [{
            part: "", prompt: `What comes after the egg stage in a frog's life cycle?`,
            options: ["Tadpole (with gills)", "Froglet (with small legs)", "Adult Frog (with lungs)", "Chrysalis"],
            hint: "It swims like a fish before growing legs.",
            explanation: "A tadpole hatches from the egg and breathes with gills."
        }]));
        qs.push(createQ(9, 3, 'cycles', "Protecting Life Cycles", 'single', null, null, [{
            part: "", prompt: `How can we help protect animal life cycles?`,
            options: ["By not destroying their breeding habitats", "By taking wild eggs home", "By removing plants they eat", "By polluting the water they live in"],
            hint: "Animals need safe places to lay eggs and raise their young.",
            explanation: "Protecting habitats ensures animals can safely breed and grow."
        }]));

        // Level 4: Thermal & States of Matter
        qs.push(createQ(10, 4, 'thermal', "States of Matter", 'single', null, null, [{
            part: "", prompt: `What are the three states of matter?`,
            options: ["Solid, Liquid, Gas", "Ice, Water, Steam", "Hard, Soft, Bouncy", "Hot, Cold, Warm"],
            hint: "One keeps its shape, one flows, one fills the air.",
            explanation: "Matter exists as Solid, Liquid, or Gas."
        }]));
        qs.push(createQ(11, 4, 'thermal', "Thermal Changes", 'single', null, null, [{
            part: "", prompt: `What happens to chocolate or ice when we heat it?`,
            options: ["It melts into a liquid", "It freezes into a solid", "It disappears", "It becomes harder"],
            hint: "Heat adds energy and makes it flow.",
            explanation: "Heating causes solid chocolate or ice to melt into a liquid."
        }]));
        qs.push(createQ(12, 4, 'thermal', "Reversible and Irreversible Changes", 'single', null, null, [{
            part: "", prompt: `Which of these is an irreversible change (cannot be changed back)?`,
            options: ["Cooking an egg or burning wood", "Melting ice into water", "Freezing water into ice", "Melting chocolate"],
            hint: "Once it's done, you can't get the original back.",
            explanation: "Cooking an egg changes it permanently; it cannot become a raw egg again."
        }]));

        // Level 5: Forces, Friction & Magnets (Scenarios)
        const angles = shuffle([15, 45]);
        qs.push(createQ(13, 5, 'forces', "Pip's Ramp & Gravity", 'scenario', `Pip is testing a toy car on two ramps. Ramp A is at ${angles[0]} degrees, and Ramp B is at ${angles[1]} degrees.`, `<svg width="200" height="100"><polygon points="10,90 190,90 10,20" fill="#ccc"/></svg>`, [
            { part: "a", prompt: "Which force pulls the car down the ramp?", options: ["Gravity", "Friction", "Magnetism", "Wind"], hint: "It's the force that pulls things towards the Earth.", explanation: "Gravity pulls objects downward." },
            { part: "b", prompt: "Which ramp will make the car roll faster?", options: [`The ${Math.max(angles[0], angles[1])} degree ramp`, `The ${Math.min(angles[0], angles[1])} degree ramp`, "Both will be the same", "Neither"], hint: "Steeper ramps make things go faster.", explanation: "A steeper angle (higher degrees) allows gravity to accelerate the car more." }
        ]));

        const surfaces = shuffle(["Tile", "Sandpaper"]);
        qs.push(createQ(14, 5, 'forces', "Surface Friction Investigation", 'scenario', `We push a toy car with the same force on a ${surfaces[0]} floor and a ${surfaces[1]} track.`, `<svg width="200" height="50"><rect x="10" y="20" width="180" height="10" fill="#a8a8a8"/></svg>`, [
            { part: "a", prompt: "On which surface will the car stop first (shortest distance)?", options: ["Sandpaper", "Tile", "Ice", "Glass"], hint: "Rough surfaces grip the wheels more.", explanation: "Sandpaper has high friction, which slows the car down quickly." },
            { part: "b", prompt: "What do we call the force that slows the car down on the surface?", options: ["Friction", "Gravity", "Magnetism", "Push"], hint: "It happens when two surfaces rub together.", explanation: "Friction opposes motion when surfaces are in contact." }
        ]));

        const items = shuffle(["iron nail", "plastic ruler", "steel paperclip", "wooden pencil"]);
        qs.push(createQ(15, 5, 'forces', "Magnet Workshop", 'scenario', `We are testing materials with a bar magnet. We have an ${items[0]}, a ${items[1]}, a ${items[2]}, and a ${items[3]}.`, `<svg width="200" height="80"><rect x="50" y="30" width="100" height="20" fill="red"/><rect x="100" y="30" width="50" height="20" fill="blue"/></svg>`, [
            { part: "a", prompt: "Which items will be attracted to the magnet?", options: ["iron nail and steel paperclip", "plastic ruler and wooden pencil", "iron nail and wooden pencil", "steel paperclip and plastic ruler"], hint: "Magnets attract ferrous metals.", explanation: "Iron and steel are magnetic metals." },
            { part: "b", prompt: "What happens if we put the North pole of two magnets together?", options: ["They repel (push away)", "They attract (pull together)", "They stick and don't move", "They melt"], hint: "Like poles push apart.", explanation: "Two North poles (or two South poles) will repel each other." }
        ]));

        currentQuestions = qs;
        return qs;
    }

    function evaluateExam(userAnswers, optionalQuestions = null) {
        const questions = optionalQuestions || currentQuestions;
        
        const domainScores = {
            needs: { correct: 0, total: 3, label: "Needs & Food Groups", labId: "nutrition" },
            animals: { correct: 0, total: 3, label: "Animal Diets & Care", labId: "nutrition" },
            cycles: { correct: 0, total: 3, label: "Life Cycles", labId: "lifecycle" },
            thermal: { correct: 0, total: 3, label: "States of Matter & Heat", labId: "thermal" },
            forces: { correct: 0, total: 3, label: "Forces, Friction & Magnets", labId: "friction" }
        };
        
        let totalScore = 0;

        userAnswers.forEach(ua => {
            const q = questions.find(question => question.id === ua.qIndex) || questions[ua.qIndex - 1];
            if (!q) return;

            let points = 0;
            if (Array.isArray(ua.answer)) {
                let correctParts = 0;
                ua.answer.forEach((ans, idx) => {
                    if (q.subQuestions[idx] && ans === q.subQuestions[idx].correctIndex) {
                        correctParts++;
                    }
                });
                
                // Award 1 point if all parts are correct
                if (correctParts === q.subQuestions.length) {
                    points = 1;
                }
            } else {
                if (q.subQuestions[0] && ua.answer === q.subQuestions[0].correctIndex) {
                    points = 1;
                }
            }
            
            ua.isCorrect = points > 0;
            ua.pointsEarned = points;
            
            domainScores[q.domain].correct += points;
            totalScore += points;
        });

        let weakestDomain = null;
        let lowestPercentage = 1.0; // max possible is 1.0
        
        for (const [key, data] of Object.entries(domainScores)) {
            const percentage = data.correct / data.total;
            if (percentage < lowestPercentage) {
                lowestPercentage = percentage;
                weakestDomain = key;
            }
        }
        
        // If everything is perfect, no weakest domain
        if (totalScore === 15) {
            weakestDomain = null;
        }

        return {
            totalScore,
            domainScores,
            weakestDomain
        };
    }

    return {
        generateExam,
        evaluateExam
    };
})();

if (typeof window !== 'undefined') {
    window.ScienceCurriculum = ScienceCurriculum;
}
