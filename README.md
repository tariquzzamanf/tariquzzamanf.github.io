# Md. Tariquzzaman — Academic Website

Source for [tariquzzamanf.github.io](https://tariquzzamanf.github.io).

**All content lives in one file: [`data.json`](data.json).** `build.js` renders it
into fully static HTML — text, navigation, meta tags and schema.org JSON-LD are
all written into the source, so search engines and link previews see the complete
page without running any JavaScript.

## Updating the site

Edit `data.json`, then:

```bash
node build.js   # rewrites the HTML pages, sitemap.xml and robots.txt
```

Commit both `data.json` and the regenerated files. Pushing to `main` also runs
the build in CI and deploys it, so an edit made in the GitHub web editor
publishes on its own.

`node build.js --check` exits non-zero if the committed HTML is behind
`data.json` — useful in a pre-commit hook.

## Files

| Path | What it is |
| --- | --- |
| `data.json` | **All site content.** The only file you normally edit |
| `build.js` | Generator: templates, icon set, meta tags, JSON-LD, sitemap |
| `assets/app.js` | Behavior only — theme toggle, menu, scroll spy, tabs |
| `assets/style.css` | The entire stylesheet, light and dark themes |
| `index.html` … `personal.html`, `404.html` | **Generated.** Do not edit by hand |
| `sitemap.xml`, `robots.txt` | **Generated** from `data.json` |
| `media/`, `files/` | Photo, institution logos, CV PDF |
| `about/`, `cv/`, `experience/`, … | Redirect stubs for the old Jekyll URLs |

No dependencies — `build.js` uses only the Node standard library.

## Editing data.json

Top-level keys:

- `site` — name, URL, email, CV path, copyright line
- `seo` — job title, employer, `knowsAbout`, `alumniOf`, `sameAs`; feeds the JSON-LD
- `nav` — navigation items, in order; also used for the footer
- `profile` — home sidebar: photo, role, institution, affiliation, socials
- `pages` — one entry per page, keyed by output filename

Each page sets a `layout` (`home`, `sections`, `tabs`, `simple`), a `title`,
`description` and `canonical`, and a list of `sections`. A section's `type` picks
its template: `prose`, `interests`, `news`, `team`, `entries`, `pubs`,
`directions` or `list`. On `sections` pages the left sidebar is generated from
each section's `id`, `icon` and `eyebrow`, so a new section brings its own nav
entry. Pages with `"noindex": true` are excluded from the sitemap and the JSON-LD.

`icon` values come from the `ICONS` table at the top of `build.js`. Text fields
accept inline HTML.

## Local preview

```bash
node build.js && python3 -m http.server 8000
```

Then open <http://localhost:8000>.
