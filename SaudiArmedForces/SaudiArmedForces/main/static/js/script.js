let currentSlide = 0;

document.addEventListener("DOMContentLoaded", function () {
    const slides = document.getElementById("slides");
    const dots = document.querySelectorAll(".dot");
    const slideItems = document.querySelectorAll(".slide");
    const cards = document.querySelectorAll(".reveal-card");

    const totalSlides = slideItems.length;

    function updateSlider() {
        if (!slides) return;

        slides.style.transform = `translateX(-${currentSlide * 100}%)`;

        dots.forEach((dot, index) => {
            dot.classList.toggle("active", index === currentSlide);
        });
    }

    window.moveSlide = function (direction) {
        if (totalSlides === 0) return;

        currentSlide += direction;

        if (currentSlide < 0) {
            currentSlide = totalSlides - 1;
        } else if (currentSlide >= totalSlides) {
            currentSlide = 0;
        }

        updateSlider();
    };

    window.goToSlide = function (index) {
        if (totalSlides === 0) return;

        currentSlide = index;
        updateSlider();
    };

    window.scrollToTop = function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    };

    updateSlider();

    if (cards.length > 0) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.35
        });

        cards.forEach((card) => observer.observe(card));
    }
});

// 
document.addEventListener("DOMContentLoaded", function () {
    const revealSections = document.querySelectorAll(".reveal-section");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
            }
        });
    }, {
        threshold: 0.25
    });

    revealSections.forEach((section) => {
        observer.observe(section);
    });
});
// 
document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(".reveal-up, .reveal-drop, .reveal-rise");

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.2
    });

    items.forEach((item) => {
        observer.observe(item);
    });
});

document.querySelector('.learn-more').addEventListener('click', function() {
    alert('Redirecting to more details...');
});

