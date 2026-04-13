/* ============================= */
/* 🌙 DARK MODE + INIT FUNCTION */
/* ============================= */

function initTheme() {
    const htmlElement = document.documentElement;
    const themeToggler = document.getElementById('themeToggler');
    const themeIcon = document.getElementById('themeIcon');

    if (!themeToggler || !htmlElement) return;

    function updateIcon(theme) {
        if (theme === 'dark') {
            themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
        } else {
            themeIcon.classList.replace('bi-sun-fill', 'bi-moon-stars-fill');
        }
    }

    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-bs-theme', savedTheme);
    updateIcon(savedTheme);

    themeToggler.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        htmlElement.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);

        document.body.classList.toggle("dark-mode", newTheme === 'dark');
    });
}


/* ============================= */
/* 🚀 MAIN LOAD */
/* ============================= */

document.addEventListener("DOMContentLoaded", function () {

    initTheme();

    /* ============================= */
    /* 🎞️ CAROUSEL */
    /* ============================= */
    const jazanCarousel = document.querySelector('#jazanCarousel');
    if (jazanCarousel) {
        new bootstrap.Carousel(jazanCarousel, {
            interval: 4000,
            ride: 'carousel',
            pause: 'hover'
        });
    }

    /* ============================= */
    /* 🔢 COUNTER */
    /* ============================= */
    const counters = document.querySelectorAll('.counter, [id^="count"]');
    let started = false;

    function startCounter() {
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target') ||
                (counter.id === 'count1' ? 250000 :
                 counter.id === 'count2' ? 50000 :
                 counter.id === 'count3' ? 12 : 0);

            let count = 0;
            const duration = 2000;
            const increment = target / (duration / 20);

            const updateCounter = () => {
                if (count < target) {
                    count += increment;
                    counter.innerText = Math.ceil(count).toLocaleString();
                    setTimeout(updateCounter, 20);
                } else {
                    counter.innerText = target.toLocaleString() + "+";
                }
            };
            updateCounter();
        });
    }

    window.addEventListener("scroll", () => {
        const statsSection = document.querySelector(".stats, .bg-dark");
        if (!statsSection || started) return;

        const sectionTop = statsSection.offsetTop;
        const scrollPos = window.scrollY + window.innerHeight;

        if (scrollPos > sectionTop + 100) {
            startCounter();
            started = true;
        }
    });

    /* ============================= */
    /* 🖼️ BEFORE / AFTER SLIDER */
    /* ============================= */
    const slider = document.getElementById('growthSlider');
    const beforeImg = document.querySelector('.p-growth-img-before');
    const beforeText = document.querySelector('.before-text');
    const afterText = document.querySelector('.after-text');
    const sliderLine = document.getElementById('sliderLine');

    if (slider && beforeImg) {
        beforeImg.style.clipPath = `polygon(0 0, 50% 0, 50% 100%, 0% 100%)`;

        slider.addEventListener('input', (e) => {
            const val = e.target.value;
            beforeImg.style.clipPath = `polygon(0 0, ${val}% 0, ${val}% 100%, 0% 100%)`;

            if (sliderLine) sliderLine.style.left = `${val}%`;
            if (beforeText) beforeText.style.opacity = val > 50 ? "0.8" : "0";
            if (afterText) afterText.style.opacity = val < 50 ? "0.8" : "0";
        });
    }

    /* ============================= */
    /* ✨ ANIMATIONS */
    /* ============================= */
    const scrollItems = document.querySelectorAll('.bento-item, .nema-item-wrapper, .timeline-row, .p-growth-timeline-item, .reveal');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    scrollItems.forEach((item, index) => {
        item.style.opacity = "0";
        item.style.transform = "translateY(30px)";
        item.style.transition = "all 0.6s ease";
        item.style.transitionDelay = `${(index % 4) * 100}ms`;
        observer.observe(item);
    });

    /* ============================= */
    /* 🗺️ MAP */
    /* ============================= */
    const mapElement = document.getElementById("map");

    if (mapElement) {
        const map = L.map('map', { scrollWheelZoom: false })
            .setView([23.8859, 45.0792], 5);

        L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
            maxZoom: 20
        }).addTo(map);

        const imageUrl = '/static/images/ksa-map.svg';
        const imageBounds = [[32.14, 34.48], [16.38, 55.66]];

        L.imageOverlay(imageUrl, imageBounds, { opacity: 0.6 }).addTo(map);

        const locations = [
            { pos: [24.7136, 46.6753], text: "منطقة الرياض", url: "/regions/riyadh/" },
            { pos: [21.4858, 39.1925], text: "منطقة مكة", url: "/regions/makkah/" },
            { pos: [16.8892, 42.5511], text: "جازان", url: "/regions/jazan/" }
        ];

        locations.forEach(loc => {
            const marker = L.marker(loc.pos).addTo(map);
            marker.bindPopup(`
                <div class="text-center">
                    <h6>${loc.text}</h6>
                    <a href="${loc.url}" class="btn btn-success btn-sm">استكشف</a>
                </div>
            `);
        });

        setTimeout(() => {
            map.invalidateSize();
        }, 500);
    }

});