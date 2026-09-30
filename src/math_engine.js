window.MathEngine = (function() {
    function randInt(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
    function shuffle(arr) { return arr.sort(() => Math.random() - 0.5); }

    // Simpler Sequences
    function genArithmeticSequence(id) {
        let start = randInt(10, 50);
        let steps = [5, 10, 50, 100];
        let step = steps[randInt(0, steps.length - 1)];
        let seq = [start, start+step, start+2*step, start+3*step];
        let next = start+4*step;
        return {
            id, type: "patterns", category: "Patterns",
            visualPrompt: "What number comes next? (Look at the pattern!)",
            visualDisplay: seq.join(", ") + ", <span style='color:#ec4899;'>?</span>",
            audioPrompt: "Look at the pattern on screen. What number comes next?",
            options: shuffle([next.toString(), (next+step).toString(), (next-step).toString(), (next+1).toString()]),
            correctAnswer: next.toString()
        };
    }

    // Place value remains
    function genPlaceValueNumToWords(id) {
        return { id, type: "place_value", category: "Numbers", visualPrompt: "What is this number in words?", visualDisplay: "45,208", audioPrompt: "Look at the number on screen. How do you write this in English words?", options: ["Forty-five thousand, two hundred and eight", "Four thousand, two hundred and eight", "Forty-five thousand, twenty-eight", "Four hundred and fifty-two, eight"], correctAnswer: "Forty-five thousand, two hundred and eight" };
    }
    function genPlaceValueWordsToNum(id) {
        return { id, type: "place_value", category: "Numbers", visualPrompt: "Find the standard number for:", visualDisplay: "Seventy-three thousand, eight hundred and forty-two", audioPrompt: "Look at the words on screen. Which number matches?", options: ["73,842", "73,482", "7,384", "730,842"], correctAnswer: "73,842" };
    }
    function genExpandedForm(id) {
        return { id, type: "place_value", category: "Numbers", visualPrompt: "Find the standard number for this sum:", visualDisplay: "50,000 + 4,000 + 600 + 30 + 9", audioPrompt: "Combine the expanded numbers to find the standard number.", options: ["54,639", "54,693", "5,463", "50,469"], correctAnswer: "54,639" };
    }

    // Addition / Subtraction (up to 99,999)
    function genAddition(id) {
        let a = randInt(10000, 80000);
        let b = randInt(1000, 15000);
        let ans = a + b;
        return {
            id, type: "vertical_math", category: "Addition",
            visualPrompt: "Solve this addition problem:",
            visualDisplay:   \n+ ,
            audioPrompt: "Add the columns vertically.",
            options: shuffle([ans.toString(), (ans+10).toString(), (ans-100).toString(), (ans+1000).toString()]),
            correctAnswer: ans.toString()
        };
    }
    function genSubtraction(id) {
        let a = randInt(50000, 99999);
        let b = randInt(10000, 40000);
        let ans = a - b;
        return {
            id, type: "vertical_math", category: "Subtraction",
            visualPrompt: "Solve this subtraction problem:",
            visualDisplay:   \n- ,
            audioPrompt: "Subtract the numbers carefully.",
            options: shuffle([ans.toString(), (ans+10).toString(), (ans-10).toString(), (ans+100).toString()]),
            correctAnswer: ans.toString()
        };
    }

    // Simplified Multiplication (up to 2-digit by 2-digit)
    function genMultiplication(id) {
        let a = randInt(10, 50);
        let b = randInt(2, 12);
        let ans = a * b;
        return {
            id, type: "multi_div", category: "Operations",
            visualPrompt: "Multiply the numbers:",
            visualDisplay: ${a} ?  = <span style='color:#ec4899;'>?</span>,
            audioPrompt: "What is the product of these numbers?",
            options: shuffle([ans.toString(), (ans+a).toString(), (ans-b).toString(), (ans+10).toString()]),
            correctAnswer: ans.toString()
        };
    }

    // Simplified Division (2-digit dividend by 1-digit divisor)
    function genDivision(id) {
        let b = randInt(2, 9);
        let ans = randInt(2, 11);
        let a = b * ans;
        return {
            id, type: "multi_div", category: "Operations",
            visualPrompt: "Divide the numbers:",
            visualDisplay: ${a} ?  = <span style='color:#ec4899;'>?</span>,
            audioPrompt: "Divide the numbers to find the answer.",
            options: shuffle([ans.toString(), (ans+1).toString(), (ans-1).toString(), (ans+2).toString()]),
            correctAnswer: ans.toString()
        };
    }

    return {
        generateExam: function() {
            let exam = [];
            // Just push simplified ones for now (15 questions)
            for(let i=1; i<=3; i++) exam.push(genPlaceValueNumToWords(i));
            for(let i=4; i<=6; i++) exam.push(genArithmeticSequence(i));
            for(let i=7; i<=9; i++) exam.push(genAddition(i));
            for(let i=10; i<=11; i++) exam.push(genSubtraction(i));
            for(let i=12; i<=13; i++) exam.push(genMultiplication(i));
            for(let i=14; i<=15; i++) exam.push(genDivision(i));
            return exam;
        },
        validateAnswer: function(qObj, ans) {
            return qObj.correctAnswer === ans;
        }
    };
})();
