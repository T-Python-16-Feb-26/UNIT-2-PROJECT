let stars =document.getElementById('Stars')
let moon2 =document.getElementById('moon2')
let mountains3 =document.getElementById('mountains3')
let mountains4 =document.getElementById('mountains4')
let land5 =document.getElementById('land5')
let horse6 =document.getElementById('horse6')
let falcon7 =document.getElementById('falcon7')


window.onscroll = function(){
    let value = window.scrollY;

    if (value <= window.innerHeight) {
        stars.style.left = value + 'px';
        moon2.style.top = value * 4 + 'px';
        mountains3.style.top = value * 2 + 'px';
        mountains4.style.top = value * 1.5 + 'px';
        land5.style.top = value + 'px';

        
    }
}




function filterCategory(category) {
    const cards = document.querySelectorAll('.question-card');
    
    cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function checkAnswers() {
    const form = document.getElementById('quiz-form');
    const formData = new FormData(form);
    
    let correctCount = 0;
    let wrongCount = 0;

    // Check values from radio buttons
    for (let value of formData.values()) {
        if (value === 'correct') {
            correctCount++;
        } else {
            wrongCount++;
        }
    }

    const resultBox = document.getElementById('result-display');
    const correctEl = document.getElementById('correct-count');
    const wrongEl = document.getElementById('wrong-count');

    correctEl.innerText = "Correct Answers: " + correctCount;
    wrongEl.innerText = "Wrong Answers: " + wrongCount;
    
    resultBox.style.display = 'block';

    resultBox.scrollIntoView({ behavior: 'smooth' });
}



function filterCategory(cat) {
    const allItems = document.querySelectorAll('.question-card, .category-header');
    
    allItems.forEach(item => {
        if (cat === 'all') {
            item.style.display = 'block';
        } 
        else if (item.getAttribute('data-category') === cat) {
            item.style.display = 'block';
        } 
        else {
            item.style.display = 'none';
        }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
}


function filterStories(category) {
    const items = document.querySelectorAll('.story-item');
    
    items.forEach(item => {
        if (category === 'all' || item.getAttribute('data-category') === category) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}


function reveal() {
    var reveals = document.querySelectorAll(".reveal");

    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;

        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
    }
}

window.addEventListener("scroll", reveal);
window.addEventListener("load", reveal);



