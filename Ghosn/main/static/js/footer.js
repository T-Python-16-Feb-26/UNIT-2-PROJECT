// ===== FOOTER INJECTION =====

document.addEventListener('DOMContentLoaded', () => {
  const footerHTML = `
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <div class="nav-logo" style="margin-bottom:0.8rem">
            <span class="logo-leaf">🌿</span> Ghosn
          </div>
          <p>Exploring the roots of agriculture in the Kingdom of Saudi Arabia — from ancient date groves to modern smart farms.</p>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="crops.html">Crops</a></li>
            <li><a href="regions.html">Regions</a></li>
            <li><a href="technology.html">Technology</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Learn</h4>
          <ul>
            <li><a href="facts.html">Facts & Stats</a></li>
            <li><a href="quiz.html">Quiz</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Project</h4>
          <ul>
            <li><a href="#">About Ghosn</a></li>
            <li><a href="#">University Project</a></li>
            <li><a href="#">Sources</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>
  © 2026 <a href="index.html">Ghosn</a> — All rights reserved. <br>
  <span class="footer-credit">
    Built with ♡ by <strong>Araa Almarhabi</strong>
  </span>
</p>
        <div class="footer-socials">
          <a class="social-link" href="#" aria-label="Twitter">𝕏</a>
          <a class="social-link" href="#" aria-label="LinkedIn">in</a>
        </div>
      </div>
    </div>
  </footer>`;

  document.body.insertAdjacentHTML('beforeend', footerHTML);
});