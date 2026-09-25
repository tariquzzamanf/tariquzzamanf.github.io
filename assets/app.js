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
    let lastActive = -1;
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
      // On phones the paper-page contents is one swipeable row; keep the active link in view.
      if (active !== lastActive && contents.scrollWidth > contents.clientWidth) {
        contents.scrollLeft += links[active].getBoundingClientRect().left - contents.getBoundingClientRect().left - 16;
      }
      lastActive = active;
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
  // Publication drawers: the link-row buttons open the <details> below them, whose own
  // summaries are hidden once JavaScript runs. A hash link to a drawer opens it.
  const toggles = [...document.querySelectorAll('.drawer-toggle')];
  const syncToggles = (drawer) => {
    toggles.filter(t => t.getAttribute('aria-controls') === drawer.id).forEach((t) => {
      t.setAttribute('aria-expanded', String(drawer.open));
      if (t.hasAttribute('aria-label')) t.setAttribute('aria-label', drawer.open ? 'Hide BibTeX' : 'Show BibTeX');
    });
  };
  toggles.forEach((toggle) => {
    const drawer = document.getElementById(toggle.getAttribute('aria-controls'));
    if (!drawer) return;
    toggle.closest('[hidden]')?.removeAttribute('hidden');
    toggle.removeAttribute('hidden');
    toggle.addEventListener('click', () => { drawer.open = !drawer.open; });
    drawer.addEventListener('toggle', () => {
      syncToggles(drawer);
      // Fetch every figure once the drawer opens, so later slides are ready before a swipe reaches them.
      if (drawer.open) drawer.querySelectorAll('img[loading="lazy"]').forEach((img) => { img.loading = 'eager'; });
    });
  });
  document.querySelectorAll('.btn-split[hidden]').forEach(split => split.removeAttribute('hidden'));

  // Figure carousels: a scroll-snap track that also swipes without JavaScript; buttons,
  // dots, and arrow keys step through it, and the counter follows the scroll position.
  document.querySelectorAll('.figure-carousel:not(.is-single)').forEach((carousel) => {
    const track = carousel.querySelector('.carousel-track');
    const slides = [...track.children];
    const controls = carousel.querySelector('.carousel-controls');
    const dots = [...carousel.querySelectorAll('.carousel-dot')];
    const status = carousel.querySelector('.carousel-status');
    const [prev, next] = carousel.querySelectorAll('.carousel-step');
    controls.hidden = false;
    let current = 0;
    let heading = null; // The slide a smooth scroll is on its way to, so quick repeat presses keep counting.
    const show = (index) => {
      heading = Math.max(0, Math.min(slides.length - 1, index));
      const target = slides[heading];
      track.scrollTo({ left: target.offsetLeft, behavior: reduceMotion() ? 'auto' : 'smooth' });
    };
    const update = () => {
      current = Math.round(track.scrollLeft / Math.max(1, track.clientWidth));
      current = Math.max(0, Math.min(slides.length - 1, current));
      if (current === heading) heading = null;
      dots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === current)));
      // Off-screen slides leave the tab order and the accessibility tree.
      slides.forEach((slide, i) => { slide.inert = i !== current; });
      status.textContent = `${current + 1} / ${slides.length}`;
      prev.disabled = current === 0;
      next.disabled = current === slides.length - 1;
    };
    let pending = false;
    track.addEventListener('scroll', () => {
      if (!pending) { pending = true; requestAnimationFrame(() => { pending = false; update(); }); }
    }, { passive: true });
    const from = () => heading ?? current;
    prev.addEventListener('click', () => show(from() - 1));
    next.addEventListener('click', () => show(from() + 1));
    dots.forEach((dot, i) => dot.addEventListener('click', () => show(i)));
    track.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
        event.preventDefault();
        show(from() + (event.key === 'ArrowRight' ? 1 : -1));
      }
    });
    update();
  });
  function reduceMotion() { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  const openFromHash = () => {
    const target = location.hash && document.getElementById(location.hash.slice(1));
    if (target && target.matches('details.pub-drawer')) target.open = true;
  };
  window.addEventListener('hashchange', openFromHash);
  openFromHash();

  document.querySelectorAll('.copy-citation').forEach((button) => {
    button.addEventListener('click', async () => {
      const target = document.getElementById(button.dataset.copyTarget);
      if (!target) return;
      const text = target.textContent;
      try {
        await navigator.clipboard.writeText(text);
        const label = button.querySelector('.copy-label') || button;
        const original = label.textContent;
        label.textContent = 'Copied';
        button.classList.add('is-copied');
        window.setTimeout(() => { label.textContent = original; button.classList.remove('is-copied'); }, 1400);
      } catch (_) {
        target.focus();
      }
    });
  });

})();
