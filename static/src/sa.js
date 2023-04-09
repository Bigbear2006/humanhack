const form = document.getElementById("quiz-form");
form.addEventListener("submit", (event) => {event.preventDefault();
    const answers = {
        "q1": "a",
        "q2": ["a", "b"],
        "q3": "c",
    };

    let score = 0;
    for (let key in answers) {
        if (Array.isArray(answers[key])) {let isCorrect = true;
            const selectedAnswers = Array.from(document.getElementsByName(key)).map((input) => input.checked);
            isCorrect = selectedAnswers.length === answers[key].length && selectedAnswers.every((answer) => answer);
            if (isCorrect) {
                score++;
            }
        } else {const selectedAnswer = document.querySelector(`input[name=${key}]:checked`).value;
            if (selectedAnswer === answers[key]) {
                score++;
            }
        }
    }

    alert(`Вы набрали ${score} баллов из ${Object.keys(answers).length} возможных`);
});