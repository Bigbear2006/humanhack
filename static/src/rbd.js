function validateAnswers() {
    var answer1 = document.querySelector('input[name="answer1"]:checked').value;
    var answer2 = document.querySelector('input[name="answer2"]:checked').value;
    var answer3 = document.querySelector('input[name="answer3"]:checked').value;

    if (answer1 === 'a' && answer2 === 'b' && answer3 === 'b') {
        alert('Все ответы верные!');
        return true;
    } else {
        alert('Один или несколько ответов неверные!');
        return false;
    }
}