// main.js
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Aquí se puede agregar la lógica para manejar el inicio de sesión
            const formData = new FormData(loginForm);
            fetch('/login', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/user_profile';
                } else {
                    alert(data.message);
                }
            });
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Aquí se puede agregar la lógica para manejar el registro
            const formData = new FormData(registerForm);
            fetch('/register', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/login';
                } else {
                    alert(data.message);
                }
            });
        });
    }
});