// ===== GHOSN - SHARED JS =====

// Theme Management
const THEME_KEY = 'ghosn-theme';

function getTheme() {
  return localStorage.getItem(THEME_KEY) || 'light';
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem(THEME_KEY, theme);
  updateThemeUI(theme);
}

function updateThemeUI(theme) {
  const icon = document.querySelector('.theme-toggle-icon');
  const label = document.querySelector('.theme-toggle-label');
  if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
  if (label) label.textContent = theme === 'dark' ? 'Light' : 'Dark';
}

function toggleTheme() {
  const current = getTheme();
  setTheme(current === 'dark' ? 'light' : 'dark');
}

// Apply theme immediately (before DOM ready to avoid flash)
document.documentElement.setAttribute('data-theme', getTheme());

document.addEventListener('DOMContentLoaded', () => {
  // Set initial theme UI
  setTheme(getTheme());

  // Theme toggle button
  const toggleBtn = document.getElementById('themeToggle');
  if (toggleBtn) toggleBtn.addEventListener('click', toggleTheme);

  // Also mobile toggle
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

  // Scroll reveal
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.card, .region-card, .tech-card, .fact-card, .nav-card').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = `opacity 0.5s ease ${i * 0.07}s, transform 0.5s ease ${i * 0.07}s, box-shadow 0.35s cubic-bezier(0.175,0.885,0.32,1.275), border-color 0.35s ease`;
    observer.observe(el);
  });
});