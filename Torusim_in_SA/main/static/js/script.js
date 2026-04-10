document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".city-tab");
    const sections = document.querySelectorAll(".city-info-section");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 160;
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute("id");
            }
        });

        tabs.forEach(tab => {
            tab.classList.remove("active");
            if (tab.getAttribute("href") === "#" + current) {
                tab.classList.add("active");
            }
        });
    });
});


    (function () {
        const savedTheme = localStorage.getItem("theme");
        const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        const currentTheme = savedTheme ? savedTheme : (prefersDark ? "dark" : "light");

        document.documentElement.setAttribute("data-bs-theme", currentTheme);

        window.addEventListener("DOMContentLoaded", function () {
            const themeToggle = document.getElementById("themeToggle");
            const themeIcon = document.getElementById("themeIcon");

            function updateIcon(theme) {
                if (!themeIcon) return;
                themeIcon.textContent = theme === "dark" ? "light_mode" : "dark_mode";
            }

            updateIcon(currentTheme);

            if (themeToggle) {
                themeToggle.addEventListener("click", function () {
                    const html = document.documentElement;
                    const newTheme = html.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
                    html.setAttribute("data-bs-theme", newTheme);
                    localStorage.setItem("theme", newTheme);
                    updateIcon(newTheme);
                });
            }
        });
    })();
