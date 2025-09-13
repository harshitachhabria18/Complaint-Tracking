// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.nav-menu') && !e.target.closest('.hamburger')) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
    
    // Simple form validation for demonstration
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simple validation
            const inputs = form.querySelectorAll('input[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'var(--error)';
                    isValid = false;
                } else {
                    input.style.borderColor = '';
                }
            });
            
            if (isValid) {
                alert('Form submission would be handled by backend logic.');
                form.reset();
            }
        });
    });
    
    // Add focus styles to form elements
    const formElements = document.querySelectorAll('input, select, textarea');
    formElements.forEach(el => {
        el.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        el.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
});