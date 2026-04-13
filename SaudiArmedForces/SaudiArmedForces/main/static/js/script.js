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

    if (window.innerWidth <= 768 && dropdown && dropdownLink) {
        dropdownLink.addEventListener("click", function (e) {
            e.preventDefault();
            dropdown.classList.toggle("active");
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

        videos.forEach((video, i) => {
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
    const items = document.querySelectorAll(".reveal-up, .reveal-drop, .reveal-rise, .reveal-card");

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