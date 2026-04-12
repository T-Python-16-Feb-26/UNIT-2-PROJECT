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


document.addEventListener("DOMContentLoaded", function () {
    const micBtn = document.getElementById("micBtn");
    const searchInput = document.getElementById("searchInput");

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        console.log("Speech recognition is not supported in this browser");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    let isListening = false;

    micBtn.addEventListener("click", function (e) {
        e.preventDefault();

        if (isListening) return;

        try {
            recognition.start();
        } catch (error) {
            console.error("Start error:", error);
        }
    });

    recognition.onstart = function () {
        isListening = true;
        micBtn.classList.add("listening");
        console.log("Recognition started");
    };

    recognition.onresult = function (event) {
        const text = event.results[0][0].transcript;
        searchInput.value = text;
        console.log("Input updated:", text);
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);

        if (event.error === "not-allowed") {
            alert("Microphone permission was denied or blocked.");
        } else if (event.error === "no-speech") {
            alert("No speech detected. Try again.");
        } else if (event.error === "network") {
            alert("Network issue during speech recognition.");
        } else {
            alert("Speech error: " + event.error);
        }
    };

    recognition.onend = function () {
        isListening = false;
        micBtn.classList.remove("listening");
        console.log("Recognition ended");
    };
});