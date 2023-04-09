const form = document.getElementById("quizForm");
const resultsContainer = document.getElementById("results");

const correctAnswers = ["a", ["a", "c"], "a"];

form.addEventListener("submit", e => {
    e.preventDefault();

    let score = 0;

    const userAnswers = [form.question1.value, [form.question2a.checked, form.question2b.checked, form.question2c.checked], form.question3.value];

    userAnswers.forEach((answer, index) => {
        if (Array.isArray(answer)) {
            answer.forEach(ans => {
                if (correctAnswers[index].includes(ans)) {
                    score += 1/correctAnswers[index].length;
                }
            })
        } else if (answer === correctAnswers[index]) {
            score++;
        }
    });

    resultsContainer.innerHTML = `<h3>Вы набрали ${score} из ${correctAnswers.length} баллов.</h3>`;
});