// ===== NAVBAR INJECTION =====
// This file injects the navbar into every page

document.addEventListener('DOMContentLoaded', () => {
  const navHTML = `
  <nav class="navbar">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo">
        <span class="logo-leaf">🌿</span> Ghosn
      </a>
      <div class="nav-links">
         <a href="{% url 'home_view' %}">Home</a>
        <a href="{% url 'crops_view' %}">Crops</a>
        <a href="{% url 'regions_view' %}">Regions</a>
        <a href="{% url 'main:initiatives_view' %}">Initiatives</a>
        <a href="{% url 'main:technology_view' %}">Technology</a>
        <a href="{% url 'main:records_view' %}">Records</a>
        <a href="{% url 'main:facts_view' %}">Facts</a>
        <a href="{% url 'main:quiz_view' %}">Quiz</a>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
          <span class="theme-toggle-icon">🌙</span>
          <span class="theme-toggle-label">Dark</span>
        </button>
      </div>
      <button class="nav-hamburger" id="hamburger" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
  <div class="nav-mobile" id="mobileNav">
    <a href="index.html">🏠 Home</a>
    <a href="crops.html">🌾 Crops</a>
    <a href="regions.html">📍 Regions</a>
    <a href="technology.html">⚙️ Technology</a>
    <a href="facts.html">📊 Facts</a>
    <a href="quiz.html">🧠 Quiz</a>
    <button class="theme-toggle" id="themeToggleMobile" style="margin-top:0.5rem;align-self:flex-start">
      <span class="theme-toggle-icon">🌙</span>
      <span class="theme-toggle-label">Dark</span>
    </button>
  </div>`;

  // Insert at beginning of body
  document.body.insertAdjacentHTML('afterbegin', navHTML);
});