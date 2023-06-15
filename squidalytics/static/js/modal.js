document.querySelectorAll('.open-modal-button').forEach(function(el) {
    el.addEventListener('click', function() {
        this.nextElementSibling.classList.add('is-active');
    });
});

document.querySelectorAll('.modal-close').forEach(function(el) {
    el.addEventListener('click', function() {
        this.parentElement.classList.remove('is-active');
    });
});

document.querySelectorAll('.modal-background').forEach(function(el) {
    el.addEventListener('click', function() {
        this.parentElement.classList.remove('is-active');
    });
});
