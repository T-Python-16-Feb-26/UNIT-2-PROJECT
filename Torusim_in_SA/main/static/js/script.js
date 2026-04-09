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
