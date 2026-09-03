# Md. Tariquzzaman — Academic Website

Source for [tariquzzamanf.github.io](https://tariquzzamanf.github.io).

**All content lives in one file: [`data.json`](data.json).** The HTML pages are
empty shells; `assets/app.js` reads `data.json` and renders every page from it —
navigation, profile, sections, publications, footer, and page metadata.

To update the site, edit `data.json` and push. Nothing else needs to change.

## Files

| Path | What it is |
| --- | --- |
| `data.json` | **All site content.** The only file you normally edit |
| `assets/app.js` | Renderer: templates, icon set, theme toggle, tabs, scroll spy |
| `assets/style.css` | The entire stylesheet, light and dark themes |
| `index.html` … `personal.html`, `404.html` | Shells — each just sets `data-page` |
| `media/` | Profile photo and institution logos |
| `files/tariq.pdf` | CV PDF |
| `about/`, `cv/`, `experience/`, … | Redirect stubs for the old Jekyll URLs |

There is no build step and there are no dependencies. `.nojekyll` tells GitHub
Pages to serve the files as they are.

## Editing data.json

Top-level keys:

- `site` — name, URL, email, CV path, copyright line
- `nav` — the navigation items, in order; also used for the footer
- `profile` — home-page sidebar: photo, role, institution, affiliation, socials
- `pages` — one entry per page, keyed by the shell's `data-page` value

Each page sets a `layout` (`home`, `sections`, `tabs`, or `simple`), its `title`
and `description`, and a list of `sections`. A section's `type` picks its
template: `prose`, `interests`, `news`, `team`, `entries`, `pubs`, `directions`,
or `list`. On `sections` pages the left sidebar is generated from each section's
`id`, `icon`, and `eyebrow`, so adding a section adds its own nav entry.

`icon` values come from the `ICONS` table at the top of `assets/app.js`. Text
fields accept inline HTML (links, `<strong>`, entities).

Adding a page means adding an entry under `pages`, a matching shell HTML file
with `data-page="<key>"`, and an entry in `nav`.

## Local preview

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Opening the files directly with `file://`
will not work — `fetch` needs HTTP.
