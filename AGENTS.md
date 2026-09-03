# Repository Guide for Agents

## Purpose

Md. Tariquzzaman's academic website: a static site generated from a single JSON
file and served by GitHub Pages.

## Architecture

`data.json` holds every piece of content. `build.js` renders it into complete
static HTML — body content, `<title>`, `<meta>` tags, Open Graph, Twitter cards
and schema.org JSON-LD are all in the committed source. `assets/app.js` carries
no content; it only wires the theme toggle, mobile menu, scroll spy and personal
page tabs. SEO is a stated priority for this site: never move content rendering
back into the browser.

**Content changes go in `data.json`.** The `.html`, `sitemap.xml` and
`robots.txt` files are build output — editing them by hand is always wrong,
and the next build overwrites it.

## Build and verification

No dependencies; `build.js` uses only the Node standard library.

```bash
node build.js            # regenerate; always run after editing data.json
node build.js --check    # exit 1 if the committed output is stale
python3 -m http.server 8000
```

After a change, verify:

- `data.json` parses;
- `node build.js --check` passes and the regenerated files are committed;
- output markup is balanced and every `class` exists in `assets/style.css`;
- every local `src`/`href` and every cross-page `#anchor` resolves;
- each indexed page has a `<title>`, description, canonical and valid JSON-LD.

CI (`.github/workflows/pages.yml`) rebuilds on push and deploys to Pages. It
warns if the committed HTML is behind `data.json` but deploys the fresh build.

## Source map

| Desired change | Edit here |
| --- | --- |
| Any text, link, paper, course, date, or list item | `data.json` |
| Navigation items and order | `nav` in `data.json` |
| Structured data: job title, employer, knowsAbout, sameAs | `seo` in `data.json` |
| Page title, description, canonical | that page's entry in `data.json` |
| A new section type, layout, or icon | `build.js` |
| Colors, typography, spacing, dark theme | `assets/style.css` |
| Theme toggle, menu, scroll spy, tabs | `assets/app.js` |

## Conventions

- Section types: `prose`, `interests`, `news`, `team`, `entries`, `pubs`,
  `directions`, `list`. Layouts: `home`, `sections`, `tabs`, `simple`.
- On `sections` pages the sidebar is derived from each section's `id`, `icon`
  and `eyebrow` — never hand-write one.
- `icon` values must exist in the `ICONS` table in `build.js`. Outline icons
  need only path data; self-painting icons carry an `attrs` string.
- Text fields are emitted as HTML, so inline tags and entities are allowed and
  raw `<`/`&` must be escaped in `data.json`.
- Nav and footer links are root-relative (`/cv.html`) so `404.html` works when
  GitHub Pages serves it from an arbitrary path. Keep them that way.
- The theme is applied by a small inline `<script>` in `<head>` so a stored
  choice cannot flash; `app.js` loads with `defer`.
- Bump `VERSION` in `build.js` when `style.css` or `app.js` changes, then
  rebuild — it drives the `?v=` cache-busting string on every page.
- The palette lives in `:root` in `assets/style.css` and is repeated for
  `html[data-theme="dark"]` and for `@media (prefers-color-scheme: dark)` scoped
  to `html:not([data-theme="light"])`. A new token must be added in all three.

## Content accuracy

Publication metadata, venues, awards, dates and course lists are factual records.
Do not invent, extrapolate or round them. Anything that cannot be sourced from
`data.json`, a linked paper, or the user should be left for the user to supply.

## Legacy URLs

`research/`, `publications/`, `experience/`, `teaching/`, `cv/`, `resume/` and
`about/` each hold a meta-refresh `index.html` preserving the old Jekyll URLs.
Keep them when renaming pages.
