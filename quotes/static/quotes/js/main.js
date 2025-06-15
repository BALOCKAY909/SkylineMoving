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

    // Hide thank you message on input/textarea focus
    var thankYou = document.getElementById('thankyou-message');
    if (thankYou) {
        document.querySelectorAll('input, textarea').forEach(function(el) {
            el.addEventListener('focus', function() {
                thankYou.style.display = 'none';
            });
        });
    }
}); 

// Carousel functionality
let currentSlideIndex = 0;
let autoSlideInterval;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-item');
    const indicators = document.querySelectorAll('.indicator');
    
    // Hide all slides
    slides.forEach(slide => slide.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));
    
    // Show current slide
    if (slides[index]) {
        slides[index].classList.add('active');
        indicators[index].classList.add('active');
    }
}

function changeSlide(direction) {
    const slides = document.querySelectorAll('.carousel-item');
    currentSlideIndex += direction;
    
    if (currentSlideIndex >= slides.length) {
        currentSlideIndex = 0;
    } else if (currentSlideIndex < 0) {
        currentSlideIndex = slides.length - 1;
    }
    
    showSlide(currentSlideIndex);
    
    // Reset auto-rotation when manually changed
    resetAutoSlide();
}

function currentSlide(index) {
    currentSlideIndex = index - 1;
    showSlide(currentSlideIndex);
    
    // Reset auto-rotation when manually changed
    resetAutoSlide();
}

function nextSlide() {
    const slides = document.querySelectorAll('.carousel-item');
    currentSlideIndex++;
    if (currentSlideIndex >= slides.length) {
        currentSlideIndex = 0;
    }
    console.log('Auto-advancing to slide:', currentSlideIndex + 1);
    showSlide(currentSlideIndex);
}

function startAutoSlide() {
    console.log('Starting auto-slide with 5 second intervals');
    autoSlideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    startAutoSlide();
}

// Initialize carousel when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing carousel...');
    const slides = document.querySelectorAll('.carousel-item');
    const indicators = document.querySelectorAll('.indicator');
    
    console.log('Found slides:', slides.length);
    console.log('Found indicators:', indicators.length);
    
    if (slides.length > 0) {
        // Ensure only first slide is active initially
        slides.forEach((slide, index) => {
            slide.classList.remove('active');
            slide.style.display = 'none';
            if (index === 0) {
                slide.classList.add('active');
                slide.style.display = 'block';
                console.log('Set first slide as active');
            }
        });
        
        indicators.forEach((indicator, index) => {
            indicator.classList.remove('active');
            if (index === 0) {
                indicator.classList.add('active');
            }
        });
        
        showSlide(0);
        startAutoSlide();
        console.log('Carousel initialized successfully');
        
        // Pause auto-rotation when hovering over carousel
        const carousel = document.querySelector('.carousel');
        if (carousel) {
            carousel.addEventListener('mouseenter', function() {
                clearInterval(autoSlideInterval);
            });
            
            carousel.addEventListener('mouseleave', function() {
                startAutoSlide();
            });
        }
    } else {
        console.log('No carousel slides found!');
    }
});