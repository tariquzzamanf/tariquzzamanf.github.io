(() => {
  const root = document.documentElement;
  root.classList.add('js');
  const themeButton = document.querySelector('.theme-toggle');
  const menuButton = document.querySelector('.nav-burger');
  const nav = document.querySelector('.site-header nav');

  try {
    const savedTheme = localStorage.getItem('tariq-theme');
    if (savedTheme === 'dark' || savedTheme === 'light') root.dataset.theme = savedTheme;
  } catch (_) { /* Reading controls still work when storage is unavailable. */ }

  if (themeButton) {
    const updateThemeLabel = () => {
      const dark = root.dataset.theme === 'dark';
      themeButton.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
      themeButton.title = dark ? 'Switch to light theme' : 'Switch to dark theme';
      themeButton.textContent = dark ? '☼' : '◐';
    };
    updateThemeLabel();
    themeButton.addEventListener('click', () => {
      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('tariq-theme', root.dataset.theme); } catch (_) {}
      updateThemeLabel();
    });
  }

  if (menuButton && nav) {
    const closeMenu = () => {
      nav.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open menu');
    };
    menuButton.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        closeMenu();
        menuButton.focus();
      }
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu();
    });
  }
})();
