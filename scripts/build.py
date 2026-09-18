"""Build the static site with Python's standard library: python3 scripts/build.py."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
def read(name): return (ROOT / 'content' / name).read_text()
papers = json.loads(read('publications.json'))
def publication(p, compact=False):
    authors = ', '.join('<strong>'+escape(a)+'</strong>' if a == 'Md. Tariquzzaman' else escape(a) for a in p['authors'])
    if compact and len(p['authors']) > 8:
        authors = 'Zhiwei Liu et al., including <strong>Md. Tariquzzaman</strong>'
    links = ' '.join(f'<a href="{escape(v)}">{escape(k)} <span aria-hidden="true">↗</span></a>' for k,v in p['links'].items())
    award = f'<p class="award">{escape(p["award"])}</p>' if p['award'] else ''
    return f'''<article class="publication" id="{p['id']}"><div class="pub-year">{p['year']}</div><div><p class="pub-status">{p['status']}</p><h3><a href="{p['links']['Paper']}">{escape(p['title'])}</a></h3><p class="authors">{authors}</p><p class="venue">{escape(p['venue'])}</p>{award}<div class="link-row paper-links">{links}</div></div></article>'''
news=json.loads(read('news.json'))
def news_list(items): return '<dl class="news">'+''.join(f'<div><dt>{x["date"]}</dt><dd>{x["text"]}</dd></div>' for x in items)+'</dl>'
news_html=news_list(news[:3])+'<details class="older-news"><summary>Earlier milestones</summary>'+news_list(news[3:])+'</details>'
course_terms={}
for term in json.loads(read('teaching.json')):
    for course in term['courses']:
        course_terms.setdefault(course, []).append(term['term'])
teaching=''.join('<article class="record"><h3>'+escape(course)+'</h3><p class="detail">['+'; '.join(escape(term) for term in terms)+']</p></article>' for course,terms in course_terms.items())
pub_body='''<header class="page-heading"><p class="eyebrow">Papers &amp; open resources</p><h1>Publications</h1><p class="lead">A record of my research, in print and in progress.</p><p>Peer-reviewed work and preprints are listed separately. Code and datasets are linked alongside each paper.</p></header><div class="publication-actions" aria-label="Publication navigation"><a class="button button-primary" href="https://scholar.google.com/citations?user=LWB_NzwAAAAJ">Google Scholar <span aria-hidden="true">↗</span></a><a class="button" href="#peer-reviewed">Peer-reviewed work</a><a class="button" href="#preprints">Preprints</a><a class="button" href="#resources">Code &amp; data</a></div><section class="section" id="peer-reviewed"><h2>Peer-reviewed work</h2>'''+''.join(publication(p) for p in papers if p['status']!='Preprint')+'''</section><section class="section" id="preprints"><h2>Preprints</h2>'''+''.join(publication(p) for p in papers if p['status']=='Preprint')+'''</section><section class="section" id="resources"><h2>Code &amp; data</h2><div class="resource-list"><article><h3><a href="https://huggingface.co/datasets/aplycaebous/BdSLIG">BdSLIG ↗</a></h3><p>Bangla Sign Language instruction generation dataset.</p></article><article><h3><a href="https://github.com/tariquzzamanf/SPIP">SPIP ↗</a></h3><p>Sign Parameter Informed Prompting: reference implementation.</p></article><article><h3><a href="https://github.com/tariquzzamanf/VITD">VITD ↗</a></h3><p>Informal Bangla embeddings and violence-inciting text detection.</p></article></div></section>'''
pages=[('index','Home','Low-resource NLP, language model evaluation, and accessibility research by Md. Tariquzzaman, Junior Lecturer at IUT.',read('home.html').replace('{{NEWS}}',news_html).replace('{{SELECTED}}',''.join(publication(p,True) for p in papers[:2]))),('research','Research','Research on Bangla NLP, multilingual model evaluation, and sign language accessibility.',read('research.html')),('publications','Publications','Publications, preprints, code, and datasets by Md. Tariquzzaman.',pub_body),('cv','CV','Education, academic appointments, teaching, and awards of Md. Tariquzzaman.',read('cv.html').replace('{{TEACHING}}',teaching)),('personal','Personal','Books, films, anime, sports, and writing by Md. Tariquzzaman.',read('personal.html'))]
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
