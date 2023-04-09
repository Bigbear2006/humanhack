function checkAnswers() {
    var score = 0;

    if (document.querySelector('input[name="q1"]:checked').value == "b") {
        score++;
    }

    if (document.querySelector('input[name="q2"]:checked').value == "a") {
        score++;
    }

    var checkboxes = document.querySelectorAll('input[name="q3"]:checked');
    if (checkboxes.length == 2) {
        var values = [];
        for (var i = 0; i < checkboxes.length; i++) {
            values.push(checkboxes[i].value);
        }
        if (values.indexOf("a") !== -1 && values.indexOf("b") !== -1) {
            score++;
        }
    }

    if (document.querySelector('input[name="q4"]:checked').value == "a") {
        score++;
    }

    if (document.querySelector('input[name="q5"]:checked').value == "b") {
        score++;
    }

    alert("Вы набрали " + score + " баллов из 5");
}