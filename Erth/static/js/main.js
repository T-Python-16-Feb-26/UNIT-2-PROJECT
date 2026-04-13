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

document.addEventListener("DOMContentLoaded",()=>{

    if(localStorage.getItem("mode")==="light"){
        document.body.classList.add("light");
    }

    const items = document.querySelectorAll(
        ".timeline-item,.breed-card,.info-card,.video-card,.content-block"
    );

    const observer = new IntersectionObserver(entries=>{
        entries.forEach(e=>{
            if(e.isIntersecting) e.target.classList.add("show");
        });
    },{threshold:0.15});

    items.forEach(el=>observer.observe(el));
});