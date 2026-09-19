# Agent instructions — academic website

## Working agreement

- Follow the user’s latest instructions. Keep durable design and workflow decisions here; do not duplicate biographies, publication records, metrics, or personal favorites.
- Use the PDF and LaTeX CV in `files/cv/` for factual records, together with approved sources in `content/` and explicit user corrections. Do not invent dates, interests, claims, or publication status. Preserve author order and distinguish accepted work from preprints.
- Maintain this guide in place. Do not create additional Markdown guides unless requested.
- Keep work inside this project. Verify the Git root before staging; never stage the parent home directory. Do not push or publish unless requested.

## Design philosophy

Create an original, reading-focused academic website. Help visitors identify the person, understand their work, find outputs, and make contact. Give Home, Research, Publications, CV, and Personal distinct purposes within consistent navigation.

- Use warm cream paper, muted green accents, subtle borders, polished buttons, and restrained motion. Use Bookerly when installed, otherwise bundled Literata; no external font service.
- Establish hierarchy through typography and spacing. Keep comfortable line lengths and make supporting metadata quieter than titles. Avoid generic slogans, decorative straplines, and repeated information.
- Keep substantive content and navigation usable without JavaScript. Use JavaScript only to enhance theme controls, mobile navigation, and active-section highlighting.
- Make layouts responsive, preserve semantic reading order, and support keyboard focus, readable contrast, and reduced motion.
- Keep documentation and site content self-contained, without references to an external design-inspiration website.

## Page and interaction rules

- **Home:** preserve the approved biography, research-interest cards, and personal section. Do not add news/milestones or selected publications. Keep desktop biography text at 19px and align its actions with the portrait/caption bottom where possible. On mobile, use name heading → portrait/caption → biography in DOM order. Center the portrait at up to 200px wide with natural proportions, hide the repeated small name, and retain role, institution, and location below the photo.
- **Research:** retain the four approved section names in `content/research.html`. Explain themes through concrete papers and resource links; paper titles must be smaller than section headings. Avoid redundant subtitles.
- **Publications:** place large publication/citation/h-index/i10-index metrics directly below the title and lead, without a box, border, or surface fill. Use Google Scholar and Download CV actions. Group entries as Conference papers, Journal articles, Workshop & shared-task papers, and Preprints, with C/J/W/P numbering and area tags. Preserve paper anchors and Code & data. Calculate publication totals from metadata; show unavailable metrics as dashes, treating zero as a valid value.
- **CV:** retain approved appointments without restoring removed entries. Group teaching by course, with semesters in brackets and course titles at 16px. Use full course names from the approved content.
- **CV actions:** Publications and CV buttons must read “Download CV” followed by an aria-hidden downward arrow (↓), matching Home; omit “Full” and “PDF”; link to `files/cv/tariq.pdf` with download behavior.
- **Section navigation:** Research, Publications, CV, and Personal share “On this page” navigation. Keep every link visible below the sticky header, highlight the active section while scrolling, and use compact sticky links on phones. Preserve stable anchors and correct scroll offsets.
- **Personal:** order topics Anime → Movies → Books → Sports, matching homepage links. Preserve the approved introduction and owner-supplied rankings. Describe collections as all-time favorites, not complete viewing histories; derive counts from supplied entries rather than inventing picks.
- **Favorite cards:** each whole card, including image, title, author, and padding, is one Wikipedia link. No repeated provider labels or nested links. Use only a soft drop shadow and subtle 1.015-scale zoom on hover, without borders, background changes, or upward lift. Preserve visible keyboard focus and disable motion for reduced-motion preferences.
- **Artwork:** load covers remotely; do not store artwork binaries in the repository. Keep provenance in metadata and the shared provider/rights-holder note. Remote hosting does not imply a copyright license.

## Source map

- `content/home.html`, `research.html`, `cv.html`, `personal.html`: approved page content and templates.
- `content/publications.json`: paper metadata, author order, types, status, topics, and resources.
- `content/scholar-metrics.json`: supplied/verified metrics and recorded date; `null` means unavailable.
- `content/personal.json`: ordered favorites; `image` is remote artwork, `source`/`provider` record provenance, and `url` is the Wikipedia card destination.
- `content/teaching.json`: teaching by term. `content/news.json`: historical updates, not shown on Home.
- `scripts/build.py`: shared HTML, page metadata, publication groups/metrics, teaching, and favorite-card rendering.
- `assets/style.css`: base typography/layout. `assets/interactions.css`: visual refinements, responsive overrides, interactions, and reduced motion.
- `assets/app.js`: theme, mobile menu with Escape handling, and `.page-contents` scroll highlighting through `aria-current="location"`.
- `profile.jpg`: portrait. `files/cv/`: factual CV sources and downloadable PDF.
- `readme.md`: website documentation. `github-profile/readme.md`: separate prepared profile README; keep consistent with approved content and publish only when requested.

## Build and verification

```sh
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Preview at http://127.0.0.1:8765; use another port if occupied. The site uses Python’s standard library and needs no package installation.

After content or template edits, rebuild and keep generated root HTML synchronized with sources. CSS-only edits do not need rebuilding. Check affected pages on desktop and narrow mobile widths after layout changes. Verify links, section-anchor positioning, keyboard focus, and reduced-motion behavior when relevant; run `git diff --check` before completion.

The site uses relative URLs and `.nojekyll` for branch-based GitHub Pages deployment from `main` at the repository root. Verify the repository and remote before any user-authorized publication.
