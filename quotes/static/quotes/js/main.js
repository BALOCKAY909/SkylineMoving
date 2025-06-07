// Placeholder for future JavaScript functionality 

document.addEventListener('DOMContentLoaded', function() {
    function showError(el) {
        if (el.nextElementSibling && el.nextElementSibling.classList.contains('error-message')) {
            el.nextElementSibling.remove();
        }
        let error = document.createElement('div');
        error.className = 'error-message';
        error.style.color = '#d32f2f';
        error.style.fontSize = '0.95em';
        error.style.marginTop = '-1em';
        error.style.marginBottom = '1em';
        if (!el.value) {
            error.innerText = 'Please fill out this field.';
        } else if (el.name === 'phone') {
            error.innerText = 'Enter a valid US phone number.';
        } else if (el.name === 'email') {
            error.innerText = 'Enter a valid email';
        } else {
            error.innerText = el.validationMessage;
        }
        el.classList.add('input-error');
        el.parentNode.insertBefore(error, el.nextSibling);
    }

    document.querySelectorAll('input, textarea').forEach(function(el) {
        el.addEventListener('blur', function() {
            if (!el.value) {
                showError(el);
            } else if (el.name === 'phone') {
                var phonePattern = /^(\+1\s?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}$/;
                if (!phonePattern.test(el.value)) {
                    showError(el);
                } else {
                    el.classList.remove('input-error');
                    if (el.nextElementSibling && el.nextElementSibling.classList.contains('error-message')) {
                        el.nextElementSibling.remove();
                    }
                }
            } else if (el.name === 'email') {
                var emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
                if (!emailPattern.test(el.value) || !el.value.endsWith('.com')) {
                    showError(el);
                } else {
                    el.classList.remove('input-error');
                    if (el.nextElementSibling && el.nextElementSibling.classList.contains('error-message')) {
                        el.nextElementSibling.remove();
                    }
                }
            } else if (!el.checkValidity()) {
                showError(el);
            } else {
                el.classList.remove('input-error');
                if (el.nextElementSibling && el.nextElementSibling.classList.contains('error-message')) {
                    el.nextElementSibling.remove();
                }
            }
        });
        el.addEventListener('input', function() {
            el.classList.remove('input-error');
            if (el.nextElementSibling && el.nextElementSibling.classList.contains('error-message')) {
                el.nextElementSibling.remove();
            }
        });
    });

    // Prevent form submission if any field is invalid
    var form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            var valid = true;
            document.querySelectorAll('input, textarea').forEach(function(el) {
                if (!el.value) {
                    showError(el);
                    valid = false;
                } else if (el.name === 'phone') {
                    var phonePattern = /^(\+1\s?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}$/;
                    if (!phonePattern.test(el.value)) {
                        showError(el);
                        valid = false;
                    }
                } else if (el.name === 'email') {
                    var emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
                    if (!emailPattern.test(el.value) || !el.value.endsWith('.com')) {
                        showError(el);
                        valid = false;
                    }
                } else if (!el.checkValidity()) {
                    showError(el);
                    valid = false;
                }
            });
            if (!valid) {
                e.preventDefault();
            }
        });
    }
}); 