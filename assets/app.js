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
  const contents = document.querySelector('.page-contents');
  if (contents) {
    const links = [...contents.querySelectorAll('a[href^="#"]')];
    const sections = links.map(link => document.getElementById(link.hash.slice(1)));
    const header = document.querySelector('.site-header');
    let scheduled = false;
    const updateSection = () => {
      scheduled = false;
      const stickyHeight = getComputedStyle(contents).position === 'sticky' && window.innerWidth <= 600 ? contents.offsetHeight : 0;
      root.style.setProperty('--contents-height', `${stickyHeight}px`);
      const threshold = header.getBoundingClientRect().bottom + stickyHeight + 45;
      let active = 0;
      sections.forEach((section, index) => {
        if (section && section.getBoundingClientRect().top <= threshold) active = index;
      });
      if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 3) active = links.length - 1;
      links.forEach((link, index) => {
        if (index === active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    const schedule = () => {
      if (!scheduled) { scheduled = true; requestAnimationFrame(updateSection); }
    };
    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule);
    window.addEventListener('load', schedule);
    new ResizeObserver(schedule).observe(contents);
    updateSection();
  }
})();
