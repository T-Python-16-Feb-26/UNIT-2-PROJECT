function toggleMode(){
    document.body.classList.toggle("light");
    localStorage.setItem("mode",
        document.body.classList.contains("light") ? "light" : "dark");
}

function openVideo(id){
    document.getElementById("videoModal").style.display = "flex";
    document.getElementById("videoFrame").src =
        "https://www.youtube.com/embed/" + id;
}

function closeVideo(){
    document.getElementById("videoModal").style.display = "none";
    document.getElementById("videoFrame").src = "";
}
function setLightMode(){
    document.body.classList.add("light");
    localStorage.setItem("mode","light");
}

function setDarkMode(){
    document.body.classList.remove("light");
    localStorage.setItem("mode","dark");
}

document.addEventListener("DOMContentLoaded",()=>{

    // وضع الإضاءة
    if(localStorage.getItem("mode")==="light"){
        document.body.classList.add("light");
    }

    // الانيميشن
    const items = document.querySelectorAll(
        ".timeline-item,.breed-card,.info-card,.video-card,.content-block"
    );

    const observer = new IntersectionObserver(entries=>{
        entries.forEach(e=>{
            if(e.isIntersecting) e.target.classList.add("show");
        });
    },{threshold:0.15});

    items.forEach(el=>observer.observe(el));


    //  زر استكشف للجوال
    const exploreBtn = document.querySelector(".explore-btn");
    const exploreDropdown = document.querySelector(".explore-dropdown");

    if (exploreBtn && exploreDropdown) {
        exploreBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            exploreDropdown.classList.toggle("active");
        });

        document.addEventListener("click", function (e) {
            if (!exploreDropdown.contains(e.target)) {
                exploreDropdown.classList.remove("active");
            }
        });
    }

});