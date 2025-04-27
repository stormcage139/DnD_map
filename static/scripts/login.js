document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const messageElement = document.getElementById('message');

    if (password !== confirmPassword) {
        messageElement.textContent = 'Пароли не совпадают!';
        return;
    }

    // Здесь можно добавить код для отправки данных на сервер

    messageElement.textContent = 'Регистрация успешна!';
    messageElement.style.color = 'green';
});