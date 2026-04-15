function setLightMode(){
    document.body.classList.add("light");
    localStorage.setItem("mode","light");
}

function setDarkMode(){
    document.body.classList.remove("light");
    localStorage.setItem("mode","dark");
}



function openVideo(url){
    const video = document.getElementById("videoFrame");

    video.src = url;
    video.currentTime = 0;
    video.play();

    document.getElementById("videoModal").style.display = "flex";


}
// نوققف الفيدو ونقفل النافذه
function closeVideo(){
    document.getElementById("videoModal").style.display = "none";
    document.getElementById("videoFrame").src = "";
}


// عند تحميل الصفحه
document.addEventListener("DOMContentLoaded",()=>{

    const mode = localStorage.getItem("mode");

    if(mode === "light"){
        document.body.classList.add("light");
    }

   // الانيميشن
    const items = document.querySelectorAll(
        ".timeline-item,.breed-card,.info-card,.video-card,.content-block"
    );

    const observer = new IntersectionObserver(entries=>{
        entries.forEach(e=>{
            if(e.isIntersecting){
                e.target.classList.add("show");
            }
        });
    },{threshold:0.15});

    items.forEach(el=>observer.observe(el));
//mobile
    const exploreBtn = document.querySelector(".explore-btn");
    const exploreDropdown = document.querySelector(".explore-dropdown");

    if (exploreBtn && exploreDropdown) {

        exploreBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            exploreDropdown.classList.toggle("active");
        });
//اذا برا القائمه الضغط يقفلها الصفحه الحالية
        document.addEventListener("click", function (e) {
            if (!exploreDropdown.contains(e.target)) {
                exploreDropdown.classList.remove("active");
            }
        });

    }

});