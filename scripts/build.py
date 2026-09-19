"""Build the static site with Python's standard library: python3 scripts/build.py."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
def read(name): return (ROOT / 'content' / name).read_text()
papers = json.loads(read('publications.json'))
def publication(p, compact=False, label=None):
    authors = ', '.join('<strong>'+escape(a)+'</strong>' if a == 'Md. Tariquzzaman' else escape(a) for a in p['authors'])
    if compact and len(p['authors']) > 8:
        authors = 'Zhiwei Liu et al., including <strong>Md. Tariquzzaman</strong>'
    links = ' '.join(f'<a href="{escape(v)}">{escape(k)} <span aria-hidden="true">↗</span></a>' for k,v in p['links'].items())
    award = f'<p class="award">{escape(p["award"])}</p>' if p['award'] else ''
    marker = escape(label) if label else p['year']
    tags = '<div class="tags">'+''.join(f'<span class="tag">{escape(area)}</span>' for area in p.get('areas', []))+'</div>' if label else ''
    return f'''<article class="publication" id="{p['id']}"><div class="pub-year">{marker}</div><div><p class="pub-status">{p['status']}</p><h3><a href="{p['links']['Paper']}">{escape(p['title'])}</a></h3><p class="authors">{authors}</p><p class="venue">{escape(p['venue'])}</p>{award}{tags}<div class="link-row paper-links">{links}</div></div></article>'''
news=json.loads(read('news.json'))
def news_list(items): return '<dl class="news">'+''.join(f'<div><dt>{x["date"]}</dt><dd>{x["text"]}</dd></div>' for x in items)+'</dl>'
news_html=news_list(news[:3])+'<details class="older-news"><summary>Earlier milestones</summary>'+news_list(news[3:])+'</details>'
course_terms={}
for term in json.loads(read('teaching.json')):
    for course in term['courses']:
        course_terms.setdefault(course, []).append(term['term'])
teaching=''.join('<article class="record"><h3>'+escape(course)+'</h3><p class="detail">['+'; '.join(escape(term) for term in terms)+']</p></article>' for course,terms in course_terms.items())
groups = [('journal', 'journal-articles', 'Journal articles', 'Journal Articles', 'J'),
          ('conference', 'conference-papers', 'Conference papers', 'Conference Papers', 'C'),
          ('workshop', 'workshop-papers', 'Workshop & shared-task papers', 'Workshop Papers', 'W'),
          ('preprint', 'preprints', 'Preprints', 'Preprints', 'P')]
metrics = json.loads(read('scholar-metrics.json'))
metric_items = [(len(papers), 'Publications'), (metrics['citations'], 'Citations'),
                (metrics['h_index'], 'h-index'), (metrics['i10_index'], 'i10-index')]
unavailable_metric = '<span aria-label="Unavailable">—</span>'
metric_html = ''.join(f'<div><dt>{name}</dt><dd>{value if value is not None else unavailable_metric}</dd></div>' for value, name in metric_items)
missing_metrics = [name for value, name in metric_items if value is None]
metric_note = 'Google Scholar metrics supplied by the author'+(' on '+escape(metrics['verified_on']) if metrics['verified_on'] else '')+'.'
if missing_metrics:
    metric_note += ' Unavailable: '+', '.join(missing_metrics)+'. See Google Scholar for the latest counts.'
contents = ''.join(f'<a href="#{anchor}">{nav}</a>' for _, anchor, _, nav, _ in groups)
sections = ''
for kind, anchor, heading, _, prefix in groups:
    entries = sorted((p for p in papers if p['type'] == kind), key=lambda p: int(p['year']), reverse=True)
    listing = ''.join(publication(p, label=f'{prefix}{len(entries)-i}') for i, p in enumerate(entries))
    if not entries:
        listing = '<p class="empty-publications">No journal articles listed yet.</p>'
    legacy_anchor = '<span id="peer-reviewed" class="legacy-anchor"></span>' if kind == 'conference' else ''
    sections += f'{legacy_anchor}<section class="publication-group" id="{anchor}" aria-labelledby="{anchor}-heading"><h2 id="{anchor}-heading">{escape(heading)} <span class="group-count">{len(entries)}</span></h2>{listing}</section>'
pub_body = f'''<header class="page-heading publications-heading"><p class="eyebrow">Research output</p><h1>Publications</h1><p class="lead">A record of my research, in print and in progress.</p></header>
<div class="publications-summary"><dl class="publication-metrics">{metric_html}</dl><div class="publication-actions"><a class="button button-primary" href="https://scholar.google.com/citations?user=LWB_NzwAAAAJ">Google Scholar <span aria-hidden="true">↗</span></a><a class="button" href="files/cv/tariq.pdf">Full CV (PDF) <span aria-hidden="true">↗</span></a></div></div><p class="metrics-note">{metric_note}</p>
<div class="reading-layout publications-layout"><nav class="contents page-contents" aria-label="On this page"><p class="eyebrow">On this page</p>{contents}<a href="#resources">Code &amp; data</a></nav><div class="publication-sections">{sections}''' + '''<section class="section" id="resources"><h2>Code &amp; data</h2><div class="resource-list"><article><h3><a href="https://huggingface.co/datasets/aplycaebous/BdSLIG">BdSLIG ↗</a></h3><p>Bangla Sign Language instruction generation dataset.</p></article><article><h3><a href="https://github.com/tariquzzamanf/SPIP">SPIP ↗</a></h3><p>Sign Parameter Informed Prompting: reference implementation.</p></article><article><h3><a href="https://github.com/tariquzzamanf/VITD">VITD ↗</a></h3><p>Informal Bangla embeddings and violence-inciting text detection.</p></article></div></section></div></div>'''

personal_data = json.loads(read('personal.json'))
personal_body = read('personal.html')
for category, entries in personal_data.items():
    ranked = category in ('anime', 'movies')
    cards = []
    for index, entry in enumerate(entries, 1):
        title = escape(entry['title'])
        source = escape(entry['source'], quote=True)
        artwork = escape(entry['image'], quote=True)
        rank = f'<span class="favorite-rank" aria-hidden="true">{index:02}</span>' if ranked else ''
        author = f'<p class="favorite-author">{escape(entry["author"])}</p>' if entry.get('author') else ''
        alt = f'{title} club crest' if category == 'sports' else f'Cover of {title}'
        cards.append(f'<li class="favorite-card"><a class="favorite-link" href="{source}"><div class="favorite-art"><img src="{artwork}" alt="{alt}" loading="lazy" decoding="async" width="300" height="450" referrerpolicy="no-referrer"></div><div class="favorite-title">{rank}<h3>{title}</h3></div></a>{author}<a class="artwork-source" href="{source}">{escape(entry["provider"])} <span aria-hidden="true">↗</span></a></li>')
    tag = 'ol' if ranked else 'ul'
    gallery = f'<{tag} class="favorites-grid favorites-{category}" role="list">'+''.join(cards)+f'</{tag}>'
    personal_body = personal_body.replace('{{'+category.upper()+'}}', gallery)

pages=[('index','Home','Low-resource NLP, language model evaluation, and accessibility research by Md. Tariquzzaman, Junior Lecturer at IUT.',read('home.html').replace('{{NEWS}}',news_html).replace('{{SELECTED}}',''.join(publication(p,True) for p in papers[:2]))),('research','Research','Research on Bangla NLP, multilingual model evaluation, and sign language accessibility.',read('research.html')),('publications','Publications','Publications, preprints, code, and datasets by Md. Tariquzzaman.',pub_body),('cv','CV','Education, academic appointments, teaching, and awards of Md. Tariquzzaman.',read('cv.html').replace('{{TEACHING}}',teaching)),('personal','Personal','Favorite anime, movies, books, and sports beyond the academic work of Md. Tariquzzaman.',personal_body)]
for slug,title,description,body in pages:
    nav=''.join(f'<a href="{s}.html"'+(' aria-current="page"' if s==slug else '')+f'>{t}</a>' for s,t,_,_ in pages)
    canonical='https://tariquzzamanf.github.io/'+('' if slug=='index' else slug+'.html')
    page_title='Md. Tariquzzaman · Language & Research' if slug=='index' else title+' · Md. Tariquzzaman'
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(page_title)}</title><meta name="description" content="{escape(description)}"><meta name="theme-color" content="#f8f5ed"><link rel="canonical" href="{canonical}"><meta property="og:type" content="website"><meta property="og:title" content="{escape(page_title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://tariquzzamanf.github.io/profile.jpg"><meta property="og:image:alt" content="Md. Tariquzzaman"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="assets/fonts/literata.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="assets/style.css"></head>
<body class="page-{slug}"><a class="skip-link" href="#main">Skip to content</a><div class="site-shell"><header class="site-header"><a class="wordmark" href="index.html" aria-label="Tariq, home">tariq<span>.</span></a><nav aria-label="Main navigation">{nav}</nav><button class="theme-toggle" type="button" aria-label="Switch to dark theme" title="Switch to dark theme"><span aria-hidden="true">◐</span></button><button class="nav-burger" type="button" aria-label="Open menu" aria-expanded="false"><span>☰</span></button></header><main id="main">{body}</main><footer class="site-footer"><p>© 2026 Md. Tariquzzaman<span>Made for reading, and a little curiosity.</span></p><div><a href="mailto:tariquzzaman@iut-dhaka.edu">Email</a><a href="https://www.linkedin.com/in/tariquzzamanf/">LinkedIn</a><a href="#main">Back to top ↑</a></div></footer></div><script src="assets/app.js"></script></body></html>'''
    html = html.replace('</head>', '<link rel="stylesheet" href="assets/interactions.css?v=20260919"></head>')
    (ROOT / (slug+'.html')).write_text(html)
print(f'Built {len(pages)} static pages.')
