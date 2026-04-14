// nav
document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");
    const dropdown = document.querySelector(".dropdown");
    const dropdownLink = dropdown ? dropdown.querySelector("a") : null;

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            menuToggle.classList.toggle("active");
            navLinks.classList.toggle("active");
        });
    }

    if (dropdown && dropdownLink) {
        dropdownLink.addEventListener("click", function (e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle("active");
            }
        });
    }
});

// home video slider
let currentSlide = 0;

document.addEventListener("DOMContentLoaded", function () {
    const slides = document.getElementById("slides");
    const videos = document.querySelectorAll(".slide video");
    const dots = document.querySelectorAll(".dot");

    if (!slides || videos.length === 0) return;

    const totalSlides = videos.length;

    function updateDots(index) {
        dots.forEach((dot, i) => {
            dot.classList.toggle("active", i === index);
        });
    }

    function showSlide(index) {
        slides.style.transform = `translateX(-${index * 100}%)`;

        videos.forEach((video) => {
            video.pause();
            video.currentTime = 0;
            video.muted = true;
        });

        updateDots(index);
        videos[index].play().catch(() => {});
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    window.goToSlide = function (index) {
        currentSlide = index;
        showSlide(currentSlide);
    };

    window.moveSlide = function (direction) {
        currentSlide += direction;

        if (currentSlide < 0) {
            currentSlide = totalSlides - 1;
        } else if (currentSlide >= totalSlides) {
            currentSlide = 0;
        }

        showSlide(currentSlide);
    };

    videos.forEach((video) => {
        video.addEventListener("ended", nextSlide);
    });

    dots.forEach((dot, index) => {
        dot.addEventListener("click", function () {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });

    showSlide(currentSlide);
});

// scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// reveal sections
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

// reveal items
document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(
        ".reveal, .naval-reveal, .missile-reveal, .reveal-up, .reveal-drop, .reveal-rise, .reveal-card, .reveal-left, .reveal-right"
    );

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                if (
                    entry.target.classList.contains("reveal") ||
                    entry.target.classList.contains("naval-reveal") ||
                    entry.target.classList.contains("missile-reveal")
                ) {
                    entry.target.classList.add("active");
                } else {
                    entry.target.classList.add("is-visible");
                }

                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15
    });

    items.forEach((item) => {
        observer.observe(item);
    });
});