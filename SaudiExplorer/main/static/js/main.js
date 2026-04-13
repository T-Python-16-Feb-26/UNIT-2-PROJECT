// ===== GHOSN - SHARED JS =====

// ===== COOKIE THEME STORAGE =====
function setThemeCookie(theme) {
  document.cookie = `ghosn-theme=${theme}; path=/; max-age=31536000`;
}

function getThemeCookie() {
  return document.cookie
    .split('; ')
    .find(row => row.startsWith('ghosn-theme='))
    ?.split('=')[1] || null;
}

// ===== THEME CORE =====
function getTheme() {
  return getThemeCookie() || 'light';
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  setThemeCookie(theme);
  updateThemeUI(theme);
}

function toggleTheme() {
  const current = getTheme();
  setTheme(current === 'dark' ? 'light' : 'dark');
}

// ===== UI UPDATE =====
function updateThemeUI(theme) {
  const icon = document.querySelector('.theme-toggle-icon');
  const label = document.querySelector('.theme-toggle-label');

  if (icon) {
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  if (label) {
    label.textContent = theme === 'dark' ? 'Light' : 'Dark';
  }
}

// ===== APPLY THEME EARLY (prevent flash) =====
document.documentElement.setAttribute('data-theme', getTheme());

// ===== DOM READY =====
document.addEventListener('DOMContentLoaded', () => {

  // Apply UI once DOM is ready
  updateThemeUI(getTheme());

  // Theme toggle buttons
  const toggleBtn = document.getElementById('themeToggle');
  if (toggleBtn) toggleBtn.addEventListener('click', toggleTheme);

  const mobileToggle = document.getElementById('themeToggleMobile');
  if (mobileToggle) mobileToggle.addEventListener('click', toggleTheme);

  // Hamburger menu
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      mobileNav.classList.toggle('open');
    });
  }

  // Close mobile nav on link click
  document.querySelectorAll('.nav-mobile a').forEach(link => {
    link.addEventListener('click', () => {
      if (mobileNav) mobileNav.classList.remove('open');
    });
  });

  // Active nav link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  document.querySelectorAll('.nav-links a, .nav-mobile a').forEach(link => {
    const href = link.getAttribute('href');

    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Scroll reveal animation
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.card, .region-card, .tech-card, .fact-card, .nav-card')
    .forEach((el, i) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition =
        `opacity 0.5s ease ${i * 0.07}s,
         transform 0.5s ease ${i * 0.07}s,
         box-shadow 0.35s cubic-bezier(0.175,0.885,0.32,1.275),
         border-color 0.35s ease`;

      observer.observe(el);
    });
});