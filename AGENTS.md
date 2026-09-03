# Repository Guide for Agents

## Purpose

Md. Tariquzzaman's academic website. Static files served by GitHub Pages from the
repository root, with all content in a single JSON file.

## Architecture

`data.json` holds every piece of content. The `.html` files are shells that carry
only `<head>` links and `<body data-page="…"><div id="site"></div>`.
`assets/app.js` fetches `/data.json`, renders the page into `#site`, and wires the
interactive behavior.

**Content changes go in `data.json`, never in the HTML files.** Touch `app.js`
only to add a new section type, layout, or icon.

## Build and verification

No build step, no dependencies. `.nojekyll` disables Jekyll on GitHub Pages.

```bash
python3 -m http.server 8000
```

`file://` will not work: `fetch` requires HTTP.

After a change, verify:

- `python3 -c "import json;json.load(open('data.json'))"` parses;
- the renderer produces balanced markup and no `undefined` strings;
- every `class` in the output exists in `assets/style.css`;
- every local `src`/`href` resolves.

## Source map

| Desired change | Edit here |
| --- | --- |
| Any text, link, paper, course, date, or list item | `data.json` |
| Navigation items and order | `nav` in `data.json` |
| Home sidebar: photo, role, affiliation, socials | `profile` in `data.json` |
| A new kind of section, layout, or icon | `assets/app.js` |
| Colors, typography, spacing, dark theme | `assets/style.css` |
| Images and CV PDF | `media/`, `files/` |

## Conventions

- Section types: `prose`, `interests`, `news`, `team`, `entries`, `pubs`,
  `directions`, `list`. Layouts: `home`, `sections`, `tabs`, `simple`.
- On `sections` pages the sidebar is derived from each section's `id`, `icon`,
  and `eyebrow` — do not hand-write a sidebar.
- `icon` values must exist in the `ICONS` table in `assets/app.js`. Outline icons
  need only path data; icons that paint themselves carry an `attrs` string.
- Text fields are injected as HTML, so entities and inline tags are allowed and
  raw `<`/`&` must be escaped.
- Nav and footer links are root-relative (`/cv.html`) so `404.html` works when
  GitHub Pages serves it from an arbitrary path. Keep them that way.
- `data.json` is fetched from `/data.json`, also for the 404 case.
- Bump the `?v=` query string on `/assets/style.css` and `/assets/app.js` in all
  six shells when either file changes.
- The palette lives in `:root` in `assets/style.css` and is repeated for
  `html[data-theme="dark"]` and for `@media (prefers-color-scheme: dark)` scoped
  to `html:not([data-theme="light"])`. A new token must be added in all three.

## Content accuracy

Publication metadata, venues, awards, dates, and course lists are factual records.
Do not invent, extrapolate, or round them. Anything that cannot be sourced from
`data.json`, a linked paper, or the user should be left for the user to supply.

## Legacy URLs

`research/`, `publications/`, `experience/`, `teaching/`, `cv/`, `resume/`, and
`about/` each contain a meta-refresh `index.html` preserving the old Jekyll URLs.
Keep them when renaming pages.
