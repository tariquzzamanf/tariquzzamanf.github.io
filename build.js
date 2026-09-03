#!/usr/bin/env node
/* =========================================================================
   Static site generator for tariquzzamanf.github.io

   Reads data.json and writes fully-rendered HTML — content, meta tags and
   schema.org JSON-LD are all in the source, so crawlers that do not run
   JavaScript still see the whole page.

     node build.js          write the pages
     node build.js --check  exit 1 if the committed pages are out of date

   Editing data.json is the only step needed; CI runs this and deploys.
   ========================================================================= */
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = __dirname;
const data = JSON.parse(fs.readFileSync(path.join(ROOT, "data.json"), "utf8"));
const VERSION = process.env.ASSET_VERSION || "20260903d";

/* ------------------------------------------------------------------ icons */
const ICONS = {
  user:      '<circle cx="12" cy="8" r="3.4"/><path d="M5.5 20a6.5 6.5 0 0 1 13 0"/>',
  flask:     '<path d="M9 3h6M10 3v5l-4.6 8.5A2 2 0 0 0 7.2 19h9.6a2 2 0 0 0 1.8-2.5L14 8V3"/><path d="M8 14h8"/>',
  megaphone: '<path d="M4 10v4a1 1 0 0 0 1 1h3l5 4V5L8 9H5a1 1 0 0 0-1 1Z"/><path d="M17 9a4.5 4.5 0 0 1 0 6"/>',
  users:     '<circle cx="9" cy="8.5" r="3"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9.5" r="2.4"/><path d="M15.5 14.3a4.6 4.6 0 0 1 5.5 4.4"/>',
  briefcase: '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>',
  doc:       '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/><path d="M8.5 13h7M8.5 17h7"/>',
  conference:'<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8.5 20h7M8.5 9.5l2.5 2.5 4.5-4.5"/>',
  workshop:  '<path d="M14.5 5.5 18 9 9.5 17.5 6 18l.5-3.5Z"/><path d="M13 7 17 11"/><path d="M4 21h16"/>',
  preprint:  '<path d="M7 3h7l5 5v13H7Z"/><path d="M14 3v5h5"/><path d="M9.5 13.5h5M9.5 17h5"/>',
  database:  '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
  building:  '<path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6"/>',
  cap:       '<path d="M12 3 1 9l11 6 11-6Z"/><path d="M5 12.5V17c0 1.5 3.1 3 7 3s7-1.5 7-3v-4.5"/>',
  trophy:    '<circle cx="12" cy="9" r="5.5"/><path d="m8.8 13.6-1.8 7 5-2.8 5 2.8-1.8-7"/>',
  book:      '<path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H19v15.5H5.5A1.5 1.5 0 0 0 4 20Z"/><path d="M19 18.5V21H5.5A1.5 1.5 0 0 1 4 19.5"/>',
  code:      '<path d="m8 6-5 6 5 6M16 6l5 6-5 6M13.5 4l-3 16"/>',
  sparkle:   '<path d="M12 3.2l1.9 5.4 5.4 1.9-5.4 1.9L12 17.8l-1.9-5.4L4.7 10.5l5.4-1.9Z"/>',
  alert:     '<circle cx="12" cy="12" r="8.5"/><path d="M12 8v5M12 16h.01"/>',
  accessibility: '<circle cx="12" cy="4.6" r="2"/><path d="M4.5 8.2h15M12 6.6V15M12 15l-3.5 5.4M12 15l3.5 5.4"/>',
  cube:      '<path d="M3 7.5 12 3l9 4.5-9 4.5-9-4.5Z"/><path d="M3 7.5V17l9 4.5 9-4.5V7.5"/><path d="M12 12v9.5"/>',
  film:      '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M3 15h18M8 4v16M16 4v16"/>',
  anime:     '<path d="M12 4c5 0 8 3.5 8 7 0 4.5-4 7-8 7s-8-2.5-8-7c0-3.5 3-7 8-7Z"/><path d="M9.5 11h.01M14.5 11h.01M9.5 14.5c1.6 1.2 3.4 1.2 5 0"/>',
  sports:    '<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5c3 3 3 14 0 17M12 3.5c-3 3-3 14 0 17M3.5 12h17"/>',
  pen:       '<path d="M12 20h8.5"/><path d="M16.5 3.6a2 2 0 0 1 2.9 2.8L7.5 18.3 3.5 19.5l1.2-4Z"/>',
  download:  '<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/>',
  mailOutline:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
  scholarOutline: '<path d="M12 3 1 9l11 6 9-4.9"/><path d="M5 13.2v3.4L12 21l7-4.4v-3.4"/>',
  moon:      '<path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11Z"/>',
  sun:       '<circle cx="12" cy="12" r="4.4"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M19.1 4.9l-1.7 1.7M6.6 17.4l-1.7 1.7"/>',
  burger:    { attrs: 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"', inner: '<path d="M3 6h18M3 12h18M3 18h18"/>' },
  mail:      { attrs: 'fill="none" stroke="currentColor" stroke-width="2"', inner: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>' },
  scholar:   { attrs: 'fill="currentColor"', inner: '<path d="M12 3 1 9l11 6 9-4.9V17h2V9zM5 13.2v3.4L12 21l7-4.4v-3.4l-7 3.8z"/>' },
  github:    { attrs: 'fill="currentColor"', inner: '<path d="M12 1a11 11 0 0 0-3.5 21.4c.55.1.75-.24.75-.53v-1.8c-3 .65-3.7-1.45-3.7-1.45-.5-1.3-1.2-1.6-1.2-1.6-1-.68.07-.67.07-.67 1.1.08 1.7 1.15 1.7 1.15 1 1.7 2.6 1.2 3.2.92.1-.72.4-1.2.7-1.5-2.4-.27-4.9-1.2-4.9-5.3 0-1.2.42-2.1 1.1-2.85-.1-.27-.48-1.36.1-2.84 0 0 .92-.3 3 1.1a10.4 10.4 0 0 1 5.5 0c2.1-1.4 3-1.1 3-1.1.6 1.48.22 2.57.1 2.84.7.75 1.1 1.65 1.1 2.85 0 4.1-2.5 5-4.9 5.27.4.35.75 1 .75 2.05v3c0 .3.2.64.76.53A11 11 0 0 0 12 1z"/>' },
  hf:        { attrs: 'fill="currentColor"', inner: '<circle cx="12" cy="12" r="10"/><circle cx="9" cy="10" r="1.4" fill="var(--surface)"/><circle cx="15" cy="10" r="1.4" fill="var(--surface)"/><path d="M8.5 14.5a4 4 0 0 0 7 0" stroke="var(--surface)" stroke-width="1.6" fill="none" stroke-linecap="round"/>' },
  linkedin:  { attrs: 'fill="currentColor"', inner: '<path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1-.02-5zM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4 0 4.8 2.6 4.8 6V21h-4v-5.6c0-1.34-.03-3.07-1.9-3.07-1.9 0-2.2 1.46-2.2 2.97V21h-4z"/>' }
};

function icon(name, cls) {
  const def = ICONS[name];
  if (!def) return "";
  const inner = typeof def === "string" ? def : def.inner;
  const attrs = typeof def === "string" ? "" : " " + def.attrs;
  return `<svg${cls ? ` class="${cls}"` : ""} viewBox="0 0 24 24" aria-hidden="true"${attrs}>${inner}</svg>`;
}

/* ---------------------------------------------------------------- helpers */
const ext = (on) => (on ? ' target="_blank" rel="noopener"' : "");
const map = (list, fn) => (list || []).map(fn).join("");
const esc = (s) => String(s).replace(/&(?!#?\w+;)/g, "&amp;").replace(/"/g, "&quot;");

function buttons(list) {
  if (!list || !list.length) return "";
  return `<div class="btn-row">${map(list, (b) =>
    `<a class="btn${b.ghost ? " ghost" : ""}" href="${b.href}"${ext(b.external)}>` +
    `${b.icon ? icon(b.icon) : ""}${b.label}</a>`)}</div>`;
}

function links(list) {
  if (!list || !list.length) return "";
  return `<div class="plinks">${map(list, (l) =>
    `<a href="${l.href}" target="_blank" rel="noopener">${l.label}</a>`)}</div>`;
}

const eyebrow = (s, band) =>
  `<div class="eyebrow${band ? " band" : ""}">${icon(s.icon)}${s.eyebrow}</div>`;

/* -------------------------------------------------------------- sections */
const SECTIONS = {
  prose: (s) =>
    eyebrow(s) +
    `<div class="prose${s.justify ? " justify" : ""}">` +
    (s.lead ? `<p class="lead">${s.lead}</p>` : "") +
    map(s.paragraphs, (p) => `<p>${p}</p>`) +
    "</div>" + buttons(s.buttons),

  interests: (s) =>
    eyebrow(s) + `<div class="interests">${map(s.items, (i) =>
      `<a class="interest" href="${i.href}">` +
      `<div class="ihead">${icon(i.icon)}<h3>${i.title}</h3></div>` +
      `<p>${i.text}</p>` +
      (i.tags && i.tags.length
        ? `<div class="tags">${map(i.tags, (t) => `<span class="tag">${t}</span>`)}</div>` : "") +
      `<span class="go">Read more &#8594;</span></a>`)}</div>`,

  news: (s) =>
    eyebrow(s) + `<div class="newslist">${map(s.items, (n) =>
      `<div class="news-item"><span class="n-when">${n.when}</span>` +
      `<span class="n-text">${n.html}</span></div>`)}</div>` + buttons(s.buttons),

  team: (s, band) =>
    eyebrow(s, band) +
    (s.intro ? `<div class="prose" style="margin-bottom:18px;"><p>${s.intro}</p></div>` : "") +
    `<div class="team-strip">${map(s.members, (m) => {
      const face = m.photo
        ? `<img class="m-photo" src="${m.photo}" alt="${esc(m.name)}" loading="lazy">`
        : `<div class="m-ph" aria-hidden="true">${m.initials || "?"}</div>`;
      const name = m.url
        ? `<a href="${m.url}" target="_blank" rel="noopener">${m.name}</a>` : m.name;
      return `<div class="member${m.pi ? " pi" : ""}">${face}` +
             `<span class="m-name">${name}</span>` +
             `<span class="m-role">${m.role}</span></div>`;
    })}</div>`,

  entries: (s, band) =>
    eyebrow(s, band) +
    (s.subhead ? `<div class="subhead">${s.subhead}</div>` : "") +
    `<div class="entry-grid${s.one ? " one" : ""}">${map(s.items, (e) =>
      `<div class="entry">` +
      (e.crest ? `<img class="crest" src="${e.crest}" alt="${esc(e.crestAlt || "")}" loading="lazy">` : "") +
      `<div class="e-body">` +
        `<div class="e-top"><div class="e-title">${e.title}</div>` +
        (e.when ? `<div class="e-when">${e.when}</div>` : "") + "</div>" +
        (e.org ? `<div class="e-org">${e.org}</div>` : "") +
        (e.meta ? `<div class="e-meta">${e.meta}</div>` : "") +
        (e.list && e.list.length ? `<ul>${map(e.list, (li) => `<li>${li}</li>`)}</ul>` : "") +
        (e.links && e.links.length
          ? `<div class="e-links">${map(e.links, (l) =>
              `<a href="${l.href}" target="_blank" rel="noopener">${l.label}</a>`)}</div>` : "") +
      `</div></div>`)}</div>` +
    (s.note ? `<div class="copi">${s.note}</div>` : ""),

  pubs: (s, band) =>
    (s.eyebrow ? eyebrow(s, band) : "") + map(s.items, (p) => {
      const title = p.url
        ? `<a href="${p.url}" target="_blank" rel="noopener">${p.title}</a>` : p.title;
      return `<div class="pub"><div class="vkey">${p.vkey}</div><div>` +
        `<div class="ptitle">${title}</div>` +
        (p.authors ? `<div class="pauthors">${p.authors}</div>` : "") +
        (p.venue ? `<div class="pvenue">${p.venue}</div>` : "") +
        (p.desc ? `<div class="pdesc">${p.desc}</div>` : "") +
        (p.badge ? `<div class="badge">${p.badge}</div>` : "") +
        (p.cats && p.cats.length
          ? `<div class="pcats">${map(p.cats, (c) =>
              `<span class="cat ${c.cls}">${c.label}</span>`)}</div>` : "") +
        links(p.links) + "</div></div>";
    }),

  directions: (s, band) =>
    eyebrow(s, band) + map(s.groups, (g) =>
      `<section class="section" id="${g.id}"><h2>${g.title}</h2>` +
      (g.intro ? `<div class="prose"><p>${g.intro}</p></div>` : "") +
      SECTIONS.pubs({ items: g.pubs }) + "</section>"),

  list: (s, band) =>
    eyebrow(s, band) +
    (s.subhead ? `<div class="subhead">${s.subhead}</div>` : "") +
    `<ul class="cv-list">${map(s.items, (i) => `<li>${i}</li>`)}</ul>`
};

/* ----------------------------------------------------------------- chrome */
// Nav and footer links are root-relative so 404.html works when GitHub Pages
// serves it from an arbitrary path.
const navbar = (current) =>
  `<nav class="nav"><div class="nav-inner">` +
  `<a href="/" class="brand">${data.site.name}</a>` +
  `<div class="nav-right"><ul class="nav-links">` +
  map(data.nav, (n) =>
    `<li><a href="/${n.href}"${n.page === current ? ' class="active"' : ""}>${n.label}</a></li>`) +
  `</ul>` +
  `<button class="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">` +
  icon("moon", "icon-moon") + icon("sun", "icon-sun") + `</button>` +
  `<button class="nav-burger" aria-label="Menu">${icon("burger")}</button>` +
  `</div></div></nav>`;

const footer = () =>
  `<footer class="footer"><div class="footer-inner">` +
  `<div>${data.site.copyright} · <a href="${data.site.url}">${data.site.shortUrl}</a></div>` +
  `<div class="fnav">${map(data.nav, (n) => `<a href="/${n.href}">${n.label}</a>`)}</div>` +
  `</div></footer>`;

function pageHead(h) {
  if (!h) return "";
  return `<header class="page-head reveal">` +
    `<div class="eyebrow">${icon(h.icon)}${h.eyebrow}</div>` +
    `<h1>${h.h1}</h1>` +
    (h.intro ? `<p>${h.intro}</p>` : "") +
    (h.stats && h.stats.length
      ? `<div class="stats">${map(h.stats, (s) =>
          `<div class="stat"><div class="num">${s.num}</div><div class="lab">${s.lab}</div></div>`)}</div>`
      : "") +
    buttons(h.buttons) + `</header>`;
}

const sidenav = (sections) =>
  `<nav class="sidenav" data-spy aria-label="Sections">` +
  `<span class="sn-label">On this page</span>` +
  map(sections, (s) => `<a href="#${s.id}">${icon(s.icon)}${s.eyebrow}</a>`) + `</nav>`;

/* ---------------------------------------------------------------- layouts */
const LAYOUTS = {
  home(page) {
    const p = data.profile;
    const aside = `<aside class="profile reveal">` +
      `<div class="profile-photo-wrap"><img class="profile-photo" src="${p.photo}" alt="${esc(p.name)}" width="200" height="200"></div>` +
      `<h1>${p.name}</h1>` +
      `<div class="role">${p.role}</div>` +
      `<div class="uni-line"><img class="crest sm" src="${p.institution.logo}" alt="${esc(p.institution.name)}" loading="lazy">` +
      `<div class="ul-text"><a href="${p.institution.url}" target="_blank" rel="noopener">${p.institution.name}</a><br>` +
      `${p.institution.dept}</div></div>` +
      `<div class="affil">${p.affiliation.join("<br>")}</div>` +
      `<div class="socials">${map(p.socials, (s) =>
        `<a href="${s.href}"${s.href.startsWith("mailto:") ? "" : ext(true)} title="${esc(s.label)}">` +
        `${icon(s.icon)} ${s.label}</a>`)}</div></aside>`;

    const main = `<main class="main">` + page.sections.map((s, i) =>
      `<section class="section reveal d${Math.min(i + 2, 4)}"${s.id ? ` id="${s.id}"` : ""}>` +
      SECTIONS[s.type](s, false) + `</section>`).join("") + `</main>`;

    return `<div class="wrap"><div class="layout">${aside}${main}</div></div>`;
  },

  sections(page) {
    const w = "wrap" + (page.wrapClass ? " " + page.wrapClass : "");
    return `<div class="${w}">${pageHead(page.head)}</div>` +
      `<div class="${w}"><div class="page-body"><div class="side-layout reveal d1">` +
      sidenav(page.sections) +
      `<div class="side-main">${map(page.sections, (s) =>
        `<section class="group" id="${s.id}">${SECTIONS[s.type](s, true)}</section>`)}</div>` +
      `</div></div></div>`;
  },

  tabs(page) {
    return `<div class="wrap">${pageHead(page.head)}</div>` +
      `<div class="wrap"><div class="page-body"><div class="personal-wrap reveal d1">` +
      `<nav class="ptabs" aria-label="Personal sections">` +
      map(page.tabs, (t, i) =>
        `<button class="ptab-btn${i === 0 ? " active" : ""}" data-tab="${t.id}">${icon(t.icon)}${t.label}</button>`) +
      `</nav><div class="ppanels">` +
      map(page.tabs, (t, i) =>
        `<div class="ppanel${i === 0 ? " active" : ""}" id="panel-${t.id}">` +
        `<h2>${t.h2}</h2>` +
        (t.lead ? `<p class="lead-sub">${t.lead}</p>` : "") +
        map(t.groups, (g) => {
          let body = "";
          if (g.list) {
            body = `<ul class="plist">${map(g.list, (li) => `<li>${li}</li>`)}</ul>`;
          } else if (g.ranklist) {
            body = `<ol class="ranklist">${g.ranklist.map((r, n) =>
              `<li><span class="rk">${String(n + 1).padStart(2, "0")}</span>` +
              `<span class="rtitle">${r.title}</span>` +
              (r.note ? `<span class="rnote">${r.note}</span>` : "") + `</li>`).join("")}</ol>`;
          } else if (g.books) {
            body = `<div class="bookgrid">${g.books.map((b, n) =>
              `<figure class="book${b.current ? " current" : ""}">` +
              `<div class="bcov" data-title="${esc(b.title)}" data-author="${esc(b.author)}">` +
              `<img src="${b.cover || ""}"${b.fallback ? ` data-alt="${b.fallback}"` : ""}` +
              ` alt="Cover of ${esc(b.title)}" loading="lazy" onerror="__cover(this)"></div>` +
              `<figcaption>` +
              (b.current ? `<span class="now">Now reading</span>`
                         : `<span class="brank">${String(n + 1).padStart(2, "0")}</span>`) +
              `<span class="btitle">${b.title}</span><span class="bauth">${b.author}</span>` +
              `</figcaption></figure>`).join("")}</div>`;
          }
          return `<div class="pgroup"><h3>${g.h3}</h3>${body}` +
                 (g.note ? `<div class="pnote">${g.note}</div>` : "") + `</div>`;
        }) + `</div>`) +
      `</div></div></div></div>`;
  },

  simple(page) {
    return `<div class="wrap">${pageHead(page.head)}</div>`;
  }
};

/* ------------------------------------------------------ structured data */
function jsonld(page) {
  const s = data.seo, site = data.site, p = data.profile;
  if (!s || page.noindex) return "";
  const org = (o) => ({ "@type": "CollegeOrUniversity", name: o.name, url: o.url });
  const person = {
    "@type": "Person",
    name: site.name,
    alternateName: s.alternateName,
    url: site.url,
    email: "mailto:" + site.email,
    image: site.url + "/" + p.photo,
    jobTitle: s.jobTitle,
    worksFor: org(s.worksFor),
    alumniOf: (s.alumniOf || []).map(org),
    knowsAbout: s.knowsAbout,
    sameAs: s.sameAs
  };
  const graph = {
    "@context": "https://schema.org",
    "@type": page.layout === "home" ? "ProfilePage" : "WebPage",
    name: page.title,
    description: page.description,
    url: page.canonical || site.url,
    isPartOf: { "@type": "WebSite", name: site.name, url: site.url },
    mainEntity: person
  };
  return `<script type="application/ld+json">${JSON.stringify(graph)}</script>`;
}

/* ------------------------------------------------------------- documents */
// Applied before first paint so a stored dark-mode choice never flashes.
const THEME_INLINE =
  `<script>(function(){try{var t=localStorage.getItem("theme");` +
  `if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>`;

function document_(key, page) {
  const site = data.site;
  const url = page.canonical || site.url + "/";
  const img = site.url + "/" + data.profile.photo;
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${page.title}</title>
<meta name="description" content="${esc(page.description)}">
${page.noindex ? '<meta name="robots" content="noindex">' : '<meta name="robots" content="index, follow">'}
<link rel="canonical" href="${url}">
<meta name="author" content="${site.name}">
<meta property="og:type" content="${page.layout === "home" ? "profile" : "website"}">
<meta property="og:site_name" content="${site.name}">
<meta property="og:title" content="${esc(page.title)}">
<meta property="og:description" content="${esc(page.description)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${img}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${esc(page.title)}">
<meta name="twitter:description" content="${esc(page.description)}">
<meta name="twitter:image" content="${img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Spline+Sans:wght@300..600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v=${VERSION}">
${THEME_INLINE}
<script src="/assets/app.js?v=${VERSION}" defer></script>
${jsonld(page)}
</head>
<body data-page="${key}">
${navbar(key)}
${LAYOUTS[page.layout](page)}
${footer()}
</body>
</html>
`;
}

function sitemap() {
  const rows = Object.entries(data.pages)
    .filter(([, p]) => !p.noindex && p.canonical)
    .map(([, p]) => `  <url><loc>${p.canonical}</loc><changefreq>monthly</changefreq></url>`);
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${rows.join("\n")}
</urlset>
`;
}

function robots() {
  return `User-agent: *\nAllow: /\n\nSitemap: ${data.site.url}/sitemap.xml\n`;
}

/* ------------------------------------------------------------------- run */
const outputs = new Map();
for (const [key, page] of Object.entries(data.pages)) {
  outputs.set(key + ".html", document_(key, page));
}
outputs.set("sitemap.xml", sitemap());
outputs.set("robots.txt", robots());

const check = process.argv.includes("--check");
let stale = [];
for (const [file, content] of outputs) {
  const dest = path.join(ROOT, file);
  const existing = fs.existsSync(dest) ? fs.readFileSync(dest, "utf8") : null;
  if (existing === content) continue;
  if (check) stale.push(file);
  else fs.writeFileSync(dest, content);
}

if (check) {
  if (stale.length) {
    console.error("Out of date with data.json: " + stale.join(", "));
    console.error("Run `node build.js` and commit the result.");
    process.exit(1);
  }
  console.log("All generated files are up to date.");
} else {
  console.log("Built " + outputs.size + " files from data.json.");
}
