"""Build the static academic site with Python's standard library."""
from pathlib import Path
from html import escape
from datetime import date, datetime
import json
import re

ROOT = Path(__file__).resolve().parent.parent
def read(name): return (ROOT / 'content' / name).read_text()

papers = json.loads(read('publications.json'))
news = json.loads(read('news.json'))
terms = json.loads(read('teaching.json'))
metrics = json.loads(read('scholar-metrics.json'))
SITE = 'https://mdtariquzzaman.github.io/'
ME = 'Md. Tariquzzaman'
GSC_TOKEN = 'boT_CMjz6ow5mcyZhAbCVE0JK2v9CAJwCu424PfT1U0'
BING_TOKEN = 'E9CE5F8AA8FFFD3C486CAF3DAAAACB56'

# Inline stroke icons (24px grid, currentColor) so actions read at a glance without JavaScript.
# Content files use {{icon:name}}; render() expands the tokens.
ICONS = {
    'arrow-right': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'arrow-left': '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    'external': '<path d="M7 17 17 7M9 7h8v8"/>',
    'download': '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    'scholar': '<path d="M2 9.5 12 4l10 5.5L12 15z"/><path d="M6 12v4.5c3.3 2.3 8.7 2.3 12 0V12M22 9.5V15"/>',
    'github': '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    'paper': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    'arxiv': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9.5 12.5l5 5M14.5 12.5l-5 5"/>',
    'pdf': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M12 11v6M9.5 14.5 12 17l2.5-2.5"/>',
    'code': '<path d="m8 7-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16"/>',
    'dataset': '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    'video': '<circle cx="12" cy="12" r="9"/><path d="m10 8.5 5.5 3.5-5.5 3.5z" fill="currentColor"/>',
    'project': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 13h8M8 16.5h5"/>',
    'copy': '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/>',
    'expand': '<path d="M14 4h6v6M10 20H4v-6M20 4l-6.5 6.5M4 20l6.5-6.5"/>',
}

def icon(name, cls='icon'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')

def expand_icons(html):
    # Direction and external-link marks trail the label; every other icon leads it.
    trailing = {'external', 'arrow-right'}
    return re.sub(r'\{\{icon:([a-z-]+)\}\}',
                  lambda m: icon(m.group(1), 'icon icon-trail' if m.group(1) in trailing else 'icon'), html)

# Paper resource labels map to an icon and a colour cue, so Paper, Code, and Dataset look different.
LINK_KIND = {'Paper': 'paper', 'arXiv': 'arxiv', 'PDF': 'pdf', 'Code': 'code', 'Dataset': 'dataset', 'Video': 'video'}

def resource_button(label, href):
    kind = LINK_KIND.get(label, 'paper')
    download = label == 'PDF' and not href.startswith(('http://', 'https://'))
    trail = '' if download else icon('external', 'icon icon-trail')
    return (f'<a class="btn" data-kind="{kind}" href="{escape(href, quote=True)}"{" download" if download else ""}>'
            f'{icon(kind)}<span>{escape(label)}</span>{trail}</a>')

def project_button(href):
    return f'<a class="btn" data-kind="project" href="{href}">{icon("project")}<span>Project page</span>{icon("arrow-right", "icon icon-trail")}</a>'

def local_publication_url(p, prefix=''):
    return f'{prefix}publications/{p["id"]}/index.html'

def external_links(p, prefix=''):
    return ''.join(resource_button(label, value) for label, value in p.get('links', {}).items())

def publication(p, compact=False, label=None, prefix=''):
    authors = ', '.join('<strong>'+escape(a)+'</strong>' if a == ME else escape(a) for a in p['authors'])
    if compact and len(p['authors']) > 8:
        authors = 'Zhiwei Liu et al., including <strong>Md. Tariquzzaman</strong>'
    award = f'<p class="award">{escape(p["award"])}</p>' if p.get('award') else ''
    marker = escape(label) if label else escape(p['year'])
    status = f'<p class="pub-status">{escape(p["status"])}</p>' if p.get('status') else ''
    tags = '<div class="tags">'+''.join(f'<span class="tag">{escape(area)}</span>' for area in p.get('areas', []))+'</div>' if label else ''
    paper_url = local_publication_url(p, prefix)
    links = project_button(paper_url) + external_links(p, prefix)
    return f'''<article class="publication" id="{escape(p['id'])}"><div class="pub-year">{marker}</div><div>{status}<h3><a href="{paper_url}">{escape(p['title'])}</a></h3><p class="authors">{authors}</p><p class="venue">{escape(p['venue'])}</p>{award}{tags}<div class="link-row paper-links">{links}</div></div></article>'''

def news_list(items):
    return '<dl class="news">'+''.join(f'<div><dt>{escape(x["date"])}</dt><dd>{x["text"]}</dd></div>' for x in items)+'</dl>'

def _courses(supervisory):
    seen = []
    for term in terms:
        for course in term['courses']:
            is_sup = '(Supervisor)' in course or '(Co-Supervisor)' in course
            if is_sup == supervisory and course not in seen:
                seen.append(course)
    return seen

def _group(heading, courses):
    if not courses: return ''
    return ('<article class="record"><h3>'+escape(heading)+'</h3><ul class="course-list">'
            + ''.join('<li>'+escape(c)+'</li>' for c in courses) + '</ul></article>')

teaching = _group('Courses', _courses(False)) + _group('Supervision', _courses(True))
groups = [('conference', 'conference-papers', 'Conference papers', 'C'),
          ('journal', 'journal-articles', 'Journal articles', 'J'),
          ('workshop', 'workshop-papers', 'Workshop & shared-task papers', 'W'),
          ('preprint', 'preprints', 'Preprints', 'P')]
metric_items = [(len(papers), 'Publications'), (metrics['citations'], 'Citations'),
                (metrics['h_index'], 'h-index'), (metrics['i10_index'], 'i10-index')]
unavailable_metric = '<span aria-label="Unavailable">—</span>'
metric_html = ''.join(f'<div><dt>{name}</dt><dd>{value if value is not None else unavailable_metric}</dd></div>' for value, name in metric_items)
missing_metrics = [name for value, name in metric_items if value is None]
metric_note = ('Google Scholar metrics refreshed' if metrics.get('source') == 'google-scholar' else 'Google Scholar metrics supplied by the author')
if metrics.get('verified_on'): metric_note += ' on ' + escape(metrics['verified_on'])
metric_note += '.'
if missing_metrics: metric_note += ' Unavailable: ' + ', '.join(missing_metrics) + '. See Google Scholar for the latest counts.'

def is_preprint(p):
    # arXiv-only work is a preprint: never label it accepted, on a paper page or in the news.
    return p['type'] == 'preprint' or 'arxiv' in p['venue'].lower()

# Home's Recent list shows every news.json entry, newest first, whatever order the file is in.
for item in news:
    for p in papers:
        if is_preprint(p) and f'publications/{p["id"]}/' in item['text'] and 'accept' in item['text'].lower():
            raise SystemExit(f'news.json calls preprint "{p["id"]}" accepted: {item["date"]}')
news_html = news_list(sorted(news, key=lambda x: datetime.strptime(x['date'], '%b %Y'), reverse=True))
contents = ''.join(f'<a href="#{anchor}">{escape(heading)}</a>' for _, anchor, heading, _ in groups)
sections = ''
for kind, anchor, heading, prefix in groups:
    entries = sorted((p for p in papers if p['type'] == kind), key=lambda p: int(p['year']), reverse=True)
    listing = ''.join(publication(p, label=f'{prefix}{len(entries)-i}') for i, p in enumerate(entries))
    if not entries: listing = '<p class="empty-publications">No journal articles listed yet.</p>'
    legacy_anchor = '<span id="peer-reviewed" class="legacy-anchor"></span>' if kind == 'conference' else ''
    sections += f'{legacy_anchor}<section class="publication-group" id="{anchor}" aria-labelledby="{anchor}-heading"><h2 id="{anchor}-heading">{escape(heading)} <span class="group-count">{len(entries)}</span></h2>{listing}</section>'
pub_body = f'''<header class="page-heading publications-heading"><p class="eyebrow">Research output</p><h1>Publications</h1><p class="lead">A record of my research, in print and in progress.</p></header>
<div class="publications-summary"><dl class="publication-metrics">{metric_html}</dl><div class="publication-actions"><a class="btn" data-kind="scholar" href="https://scholar.google.com/citations?user=LWB_NzwAAAAJ">{icon("scholar")}<span>Google Scholar</span>{icon("external", "icon icon-trail")}</a><a class="btn" data-kind="cv" href="files/cv/tariq.pdf" target="_blank" rel="noopener">{icon("pdf")}<span>Download CV</span>{icon("external", "icon icon-trail")}</a></div></div><p class="metrics-note">{metric_note}</p>
<div class="reading-layout publications-layout"><nav class="contents page-contents" aria-label="On this page"><p class="eyebrow">On this page</p>{contents}<a href="#resources">Code &amp; data</a></nav><div class="publication-sections">{sections}<section class="section" id="resources"><h2>Code &amp; data</h2><div class="resource-list"><article><h3><a href="https://huggingface.co/datasets/aplycaebous/BdSLIG">BdSLIG{icon("external", "icon icon-trail")}</a></h3><p>Bangla Sign Language instruction generation dataset.</p></article><article><h3><a href="https://github.com/mdtariquzzaman/SPIP">SPIP{icon("external", "icon icon-trail")}</a></h3><p>Sign Parameter Informed Prompting: reference implementation.</p></article><article><h3><a href="https://github.com/mdtariquzzaman/VITD">VITD{icon("external", "icon icon-trail")}</a></h3><p>Informal Bangla embeddings and violence-inciting text detection.</p></article></div></section></div></div>'''

personal_data = json.loads(read('personal.json'))
personal_body = read('personal.html')
for category, entries in personal_data.items():
    ranked = category in ('anime', 'movies')
    cards = []
    for index, entry in enumerate(entries, 1):
        title = escape(entry['title']); destination = escape(entry['url'], quote=True)
        artwork = escape(entry['image'], quote=True)
        rank = f'<span class="favorite-rank" aria-hidden="true">{index:02}</span>' if ranked else ''
        author = f'<p class="favorite-author">{escape(entry["author"])}</p>' if entry.get('author') else ''
        alt = f'{title} club crest' if category == 'sports' else f'Cover of {title}'
        cards.append(f'<li class="favorite-card"><a class="favorite-link" href="{destination}"><div class="favorite-art"><img src="{artwork}" alt="{alt}" loading="lazy" decoding="async" width="300" height="450" referrerpolicy="no-referrer"></div><div class="favorite-title">{rank}<h3>{title}</h3></div>{author}</a></li>')
    tag = 'ol' if ranked else 'ul'
    personal_body = personal_body.replace('{{'+category.upper()+'}}', f'<{tag} class="favorites-grid favorites-{category}" role="list">'+''.join(cards)+f'</{tag}>')

# Home's Personal teaser: one card per topic, in personal.json order.
TOPIC_LABELS = {'anime': 'Anime', 'movies': 'Movies', 'books': 'Books', 'sports': 'Sports'}
personal_topics = '<ul class="topic-grid" role="list">' + ''.join(
    f'<li><a href="personal.html#{c}"><h3>{TOPIC_LABELS[c]}</h3></a></li>' for c in personal_data) + '</ul>'
pages = [('index', 'Home', 'Misinformation detection, LLM evaluation, low-resource Bangla NLP, and sign language accessibility research by Md. Tariquzzaman, Junior Lecturer at IUT.', read('home.html').replace('{{NEWS}}', news_html).replace('{{PERSONAL_TOPICS}}', personal_topics).replace('{{SELECTED}}', ''.join(publication(p, True) for p in papers[:2]))),
         ('publications', 'Publications', 'Publications, preprints, code, and datasets by Md. Tariquzzaman.', pub_body),
         ('cv', 'CV', 'Education, academic appointments, teaching, and awards of Md. Tariquzzaman.', read('cv.html').replace('{{TEACHING}}', teaching)),
         ('personal', 'Personal', 'Favorite anime, movies, books, and sports beyond the academic work of Md. Tariquzzaman.', personal_body)]

PERSON = {'@type': 'Person', '@id': SITE + '#person', 'name': ME,
          'alternateName': ['Tariquzzaman', 'Md Tariquzzaman', 'Tariquzzaman Md'],
          'jobTitle': 'Junior Lecturer', 'url': SITE, 'image': SITE + 'profile.jpg',
          'affiliation': {'@type': 'CollegeOrUniversity', 'name': 'Islamic University of Technology', 'url': 'https://www.iutoic-dhaka.edu/'},
          'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'Islamic University of Technology'},
          'knowsAbout': ['Misinformation & harmful content', 'LLM evaluation & bias', 'Low-resource & Bangla NLP', 'Accessibility & sign language'],
          'sameAs': ['https://scholar.google.com/citations?user=LWB_NzwAAAAJ', 'https://github.com/mdtariquzzaman', 'https://www.linkedin.com/in/md-tariquzzaman/', 'https://orcid.org/0009-0002-3322-8741', 'https://huggingface.co/md-tariquzzaman']}

def ld(payload):
    return '<script type="application/ld+json">' + json.dumps(payload, separators=(',', ':')).replace('</', r'<\/') + '</script>'

def arxiv_id(p):
    if p.get('arxiv'): return str(p['arxiv']).removeprefix('arXiv:')
    for value in p.get('links', {}).values():
        match = re.search(r'arxiv\.org/(?:abs|pdf)/([^/?#]+)', value, re.I)
        if match: return match.group(1).removesuffix('.pdf')
    return None

def publication_schema(p, canonical):
    item = {'@type': 'ScholarlyArticle', '@id': canonical + '#article', 'name': p['title'], 'headline': p['title'],
            'author': [{'@id': PERSON['@id']} if a == ME else {'@type': 'Person', 'name': a} for a in p['authors']],
            'datePublished': p['year'], 'inLanguage': 'en', 'url': canonical,
            'isPartOf': {'@type': 'CollectionPage', 'name': 'Publications', 'url': SITE + 'publications.html'},
            'creativeWorkStatus': p['status'] or 'Published'}
    if p.get('venue'): item['isPartOf'] = {'@type': 'CreativeWork', 'name': p['venue']}
    if p.get('abstract'): item['abstract'] = p['abstract']
    if p.get('areas'): item['keywords'] = p['areas']
    doi = p.get('doi') or p.get('metadata', {}).get('doi')
    if doi:
        item['identifier'] = {'@type': 'PropertyValue', 'propertyID': 'DOI', 'value': doi, 'url': 'https://doi.org/' + doi}
    aid = arxiv_id(p)
    if aid: item['identifier'] = [{'@type': 'PropertyValue', 'propertyID': 'arXiv', 'value': aid, 'url': f'https://arxiv.org/abs/{aid}'}] + ([item['identifier']] if isinstance(item.get('identifier'), dict) else [])
    if p.get('pdf'):
        pdf = p['pdf'] if p['pdf'].startswith('http') else SITE + p['pdf'].lstrip('/')
        item['encoding'] = {'@type': 'MediaObject', 'contentUrl': pdf, 'encodingFormat': 'application/pdf'}
    item['mainEntityOfPage'] = {'@type': 'WebPage', '@id': canonical}
    return item

def citation_meta(p):
    tags = [f'<meta name="citation_title" content="{escape(p["title"], quote=True)}">']
    tags += [f'<meta name="citation_author" content="{escape(a, quote=True)}">' for a in p['authors']]
    if p.get('year'): tags.append(f'<meta name="citation_publication_date" content="{escape(str(p["year"]))}">')
    if p.get('venue'):
        key = 'citation_journal_title' if p['type'] == 'journal' else 'citation_conference_title'
        tags.append(f'<meta name="{key}" content="{escape(p["venue"], quote=True)}">')
    aid = arxiv_id(p)
    if aid: tags.append(f'<meta name="citation_arxiv_id" content="{escape(aid, quote=True)}">')
    metadata = dict(p.get('metadata', {}))
    if p.get('doi'): metadata['doi'] = p['doi']
    for label, value in metadata.items():
        if label in {'doi', 'volume', 'issue', 'firstpage', 'lastpage', 'issn', 'technical_report_institution', 'technical_report_number', 'date'} and value:
            tags.append(f'<meta name="citation_{label}" content="{escape(str(value), quote=True)}">')
    pdf = p.get('pdf')
    if pdf:
        absolute = pdf if pdf.startswith('http') else SITE + pdf.lstrip('/')
        tags.append(f'<meta name="citation_pdf_url" content="{escape(absolute, quote=True)}">')
    return ''.join(tags)

LINK_ORDER = ['Paper', 'arXiv', 'PDF', 'Code', 'Dataset', 'Video']

def paper_figure(f, prefix, extra=''):
    src = escape(prefix + f['src'], quote=True)
    size = f' width="{f["width"]}" height="{f["height"]}"' if f.get('width') else ''
    classes = 'paper-figure' + (' paper-figure-narrow' if f.get('narrow') else '') + extra
    # The image and the caption link open the same file; only the text link is in the tab order.
    return (f'<figure class="{classes}"><a class="figure-image" href="{src}" tabindex="-1">'
            f'<img src="{src}" alt="{escape(f["alt"], quote=True)}"{size} loading="lazy" decoding="async"></a>'
            f'<figcaption>{escape(f["caption"])} <a class="figure-zoom" href="{src}">View full size{icon("expand", "icon icon-trail")}</a></figcaption></figure>')

def paper_table(t):
    head = ''.join(f'<th scope="col">{escape(c)}</th>' for c in t['columns'])
    rows = ''.join('<tr>' + ''.join(f'<th scope="row">{cell}</th>' if i == 0 else f'<td>{cell}</td>' for i, cell in enumerate(r)) + '</tr>' for r in t['rows'])
    # The caption sits outside the scroll box so it stays readable when a wide table scrolls on phones.
    return (f'<div class="paper-table-wrap"><p class="table-caption">{escape(t["caption"])}</p>'
            f'<div class="table-scroll" role="region" tabindex="0" aria-label="{escape(t["caption"], quote=True)}"><table class="paper-table">'
            f'<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></div>')

def paper_list(items, ordered=False):
    tag = 'ol' if ordered else 'ul'
    return f'<{tag} class="paper-list">' + ''.join(f'<li>{x}</li>' for x in items) + f'</{tag}>'

def paper_section(sec, prefix):
    # Section prose may carry <strong>; it is authored in publications.json, like news.json's links.
    parts = [f'<p>{x}</p>' for x in sec.get('paragraphs', [])]
    if sec.get('list'): parts.append(paper_list(sec['list'], sec.get('ordered')))
    parts += [f'<p>{x}</p>' for x in sec.get('after', [])]
    if sec.get('table'): parts.append(paper_table(sec['table']))
    parts += [paper_figure(f, prefix) for f in sec.get('figures', [])]
    if sec.get('embed'):
        e = sec['embed']
        parts.append(f'<figure class="paper-embed"><iframe src="{escape(e["src"], quote=True)}" title="{escape(e["title"], quote=True)}" loading="lazy"></iframe><figcaption>{escape(e["caption"])}</figcaption></figure>')
    sid = escape(sec['id'])
    return f'<section class="section paper-section" id="{sid}" aria-labelledby="{sid}-heading"><h2 id="{sid}-heading">{escape(sec["heading"])}</h2>{"".join(parts)}</section>'

def paper_findings(findings, prefix):
    items = []
    for n, f in enumerate(findings, 1):
        body = f'<p>{f["detail"]}</p>'
        body += ''.join(f'<blockquote class="paper-quote"><p>{escape(q)}</p></blockquote>' for q in f.get('quotes', []))
        if f.get('figure'): body += paper_figure(f['figure'], prefix)
        if f.get('table'): body += paper_table(f['table'])
        items.append(f'<details class="finding"><summary><span class="finding-index" aria-hidden="true">{n:02}</span><span>{escape(f["claim"])}</span></summary><div class="finding-body">{body}</div></details>')
    return f'<section class="section paper-section" id="findings" aria-labelledby="findings-heading"><h2 id="findings-heading">Findings</h2><p class="section-note">Open a finding for the detail and evidence behind it.</p><div class="findings">{"".join(items)}</div></section>'

def paper_video(v):
    src, title = escape(v['src'], quote=True), escape(v['title'], quote=True)
    if v['kind'] == 'video':
        player = f'<video controls preload="metadata" src="{src}" title="{title}"><a href="{src}">Download the video</a></video>'
    else:
        player = f'<iframe src="{src}" title="{title}" loading="lazy" allow="fullscreen" allowfullscreen></iframe>'
    return f'<section class="section paper-section" id="video" aria-labelledby="video-heading"><h2 id="video-heading">Video</h2><div class="paper-video">{player}</div></section>'

TYPE_LABEL = {'conference': 'Conference paper', 'journal': 'Journal article', 'workshop': 'Workshop paper', 'preprint': 'Preprint'}

def publication_body(p, prefix='', prev=None, nxt=None):
    page = p.get('page', {})
    group = next(g for g in groups if g[0] == p['type'])
    breadcrumb = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{prefix}publications.html">Publications</a>'
                  f'<span aria-hidden="true">/</span><a href="{prefix}publications.html#{group[1]}">{escape(group[2])}</a></nav>')

    links = {**p.get('links', {}), **page.get('links', {})}
    if p.get('pdf'): links['PDF'] = p['pdf'] if p['pdf'].startswith(('http://', 'https://')) else prefix + p['pdf']
    ordered = sorted(links.items(), key=lambda kv: LINK_ORDER.index(kv[0]) if kv[0] in LINK_ORDER else len(LINK_ORDER))
    resources = '<div class="link-row paper-links publication-resources">' + ''.join(
        resource_button(k, v) for k, v in ordered) + '</div>'

    award = f'<p class="award">{escape(p["award"])}</p>' if p.get('award') else ''
    topics = '<div class="tags">'+''.join(f'<span class="tag">{escape(x)}</span>' for x in p.get('areas', []))+'</div>' if p.get('areas') else ''
    accepted_venue = '' if is_preprint(p) else (
        f'<p class="accepted-venue" role="note"><span class="accepted-label">Accepted</span>'
        f'<span class="accepted-name">{escape(p["venue"])}</span></p>')
    header = (f'<header class="page-heading paper-hero">{breadcrumb}<p class="eyebrow">{TYPE_LABEL[p["type"]]} · {escape(p["year"])}</p>'
              f'<h1>{escape(p["title"])}</h1>{accepted_venue}{award}{topics}{resources}</header>')

    # Section order follows a project page: teaser, summary, the work itself, findings, video, citation.
    teaser = paper_figure(page['teaser'], prefix, ' paper-teaser') if page.get('teaser') else ''
    lead = page.get('tldr') or p.get('summary', '')
    abstract = f'<details class="paper-abstract"><summary>Full abstract</summary><p>{escape(p["abstract"])}</p></details>' if p.get('abstract') else ''
    overview = (f'<section class="paper-overview" id="overview" aria-labelledby="overview-heading">{teaser}<div class="paper-tldr">'
                f'<h2 class="paper-tldr-label" id="overview-heading">In short</h2><p>{escape(lead)}</p>{abstract}</div></section>')
    sections = ''.join(paper_section(sec, prefix) for sec in page.get('sections', []))
    findings = paper_findings(page['findings'], prefix) if page.get('findings') else ''
    video = paper_video(page['video']) if page.get('video') else ''
    citation = ('<section class="section citation-block" id="citation" aria-labelledby="citation-heading"><div class="section-heading"><h2 id="citation-heading">Cite this paper</h2></div>'
                f'<div class="citation-code"><pre tabindex="0"><code id="bibtex-text">{escape(p.get("bibtex", ""))}</code></pre>'
                '<button class="btn copy-citation" data-kind="copy" type="button" data-copy-target="bibtex-text">' + icon('copy') + '<span class="copy-label">Copy BibTeX</span></button></div></section>')
    thanks = (f'<section class="section paper-section" id="acknowledgements" aria-labelledby="acknowledgements-heading"><h2 id="acknowledgements-heading">Acknowledgements</h2><p>{escape(page["acknowledgements"])}</p></section>'
              if page.get('acknowledgements') else '')

    # "On this page" uses short labels; the section headings stay descriptive.
    toc = [('overview', 'Overview')] + [(s['id'], s.get('nav', s['heading'])) for s in page.get('sections', [])]
    if page.get('findings'): toc.append(('findings', 'Findings'))
    if page.get('video'): toc.append(('video', 'Video'))
    toc.append(('citation', 'Cite'))
    contents = '<nav class="contents page-contents" aria-label="On this page"><p class="eyebrow">On this page</p>' + ''.join(f'<a href="#{i}">{escape(t)}</a>' for i, t in toc) + '</nav>'

    def pager_link(q, rel, label):
        if not q: return '<span></span>'
        return f'<a class="pager-{rel}" href="{prefix}publications/{q["id"]}/index.html" rel="{rel}"><span class="pager-label">{label}</span><span class="pager-title">{escape(q["title"])}</span></a>'
    pager = (f'<nav class="paper-pager" aria-label="More publications">{pager_link(prev, "prev", icon("arrow-left") + "Previous paper")}'
             f'{pager_link(nxt, "next", "Next paper" + icon("arrow-right"))}</nav>')
    return (f'<article class="publication-detail">{header}<div class="reading-layout paper-layout">{contents}'
            f'<div class="paper-body">{overview}{sections}{findings}{video}{citation}{thanks}{pager}</div></div></article>')

def render(slug, page_title, description, canonical, body, current=None, head_extra='', noindex=False, asset_prefix=''):
    nav = ''.join(f'<a href="{asset_prefix}{s}.html"' + (' aria-current="page"' if s == current else '') + f'>{t}</a>' for s, t, _, _ in pages)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow">'
    asset = asset_prefix
    body = expand_icons(body)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(page_title)}</title><meta name="description" content="{escape(description, quote=True)}">{robots}<meta name="google-site-verification" content="{GSC_TOKEN}"><meta name="msvalidate.01" content="{BING_TOKEN}"><meta name="theme-color" content="#f8f5ed"><link rel="canonical" href="{canonical}"><meta property="og:type" content="{'article' if slug == 'publication' else 'website'}"><meta property="og:title" content="{escape(page_title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE}profile.jpg"><meta property="og:image:alt" content="Md. Tariquzzaman"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(page_title, quote=True)}"><meta name="twitter:description" content="{escape(description, quote=True)}"><meta name="twitter:image" content="{SITE}profile.jpg"><link rel="icon" href="{asset}assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="{asset}assets/fonts/literata.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{asset}assets/style.css"><link rel="stylesheet" href="{asset}assets/interactions.css?v=20260925i">{head_extra}</head><body class="page-{slug}"><a class="skip-link" href="#main">Skip to content</a><div class="site-shell"><header class="site-header"><a class="wordmark" href="{asset}index.html" aria-label="Tariq, home">tariq<span>.</span></a><nav aria-label="Main navigation">{nav}</nav><button class="theme-toggle" type="button" aria-label="Switch to dark theme" title="Switch to dark theme"><span aria-hidden="true">◐</span></button><button class="nav-burger" type="button" aria-label="Open menu" aria-expanded="false"><span>☰</span></button></header><main id="main">{body}</main><footer class="site-footer"><p>© 2026 Md. Tariquzzaman</p><div><a href="mailto:tariquzzaman@iut-dhaka.edu">Email</a><a href="https://www.linkedin.com/in/md-tariquzzaman/">LinkedIn</a><a href="https://orcid.org/0009-0002-3322-8741">ORCID</a><a href="https://huggingface.co/md-tariquzzaman">Hugging Face</a><a href="#main">Back to top ↑</a></div></footer></div><script src="{asset}assets/app.js"></script></body></html>'''

schemas = {'index': ld({'@context': 'https://schema.org', **PERSON})}
for slug, title, description, body in pages:
    canonical = SITE + ('' if slug == 'index' else slug + '.html')
    page_title = 'Md. Tariquzzaman · Junior Lecturer & NLP Researcher at IUT' if slug == 'index' else title + ' · Md. Tariquzzaman'
    (ROOT / (slug + '.html')).write_text(render(slug, page_title, description, canonical, body, current=slug, head_extra=schemas.get(slug, '')))

# Preserve old Research URLs while consolidating research discovery in Publications.
(ROOT / 'research.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=publications.html"><link rel="canonical" href="' + SITE + 'publications.html"><title>Research · Md. Tariquzzaman</title></head><body><p>Research is now organised through the <a href="publications.html">Publications page</a>.</p></body></html>')

publication_routes = []
# Previous/next follow the order of the Publications page.
paper_order = [p for kind, *_ in groups for p in sorted((q for q in papers if q['type'] == kind), key=lambda q: int(q['year']), reverse=True)]
for i, p in enumerate(paper_order):
    route = ROOT / 'publications' / p['id'] / 'index.html'; route.parent.mkdir(parents=True, exist_ok=True)
    canonical = SITE + 'publications/' + p['id'] + '/'
    description = f'{p["title"]} by {ME}. {p["venue"]}.'
    extra = citation_meta(p) + ld({'@context': 'https://schema.org', '@graph': [PERSON, publication_schema(p, canonical)]})
    route.write_text(render('publication', p['title'] + ' · Md. Tariquzzaman', description, canonical, publication_body(p, '../../', paper_order[i-1] if i else None, paper_order[i+1] if i+1 < len(paper_order) else None), current='publications', head_extra=extra, asset_prefix='../../'))
    publication_routes.append(canonical)

not_found = '<header class="page-heading"><p class="eyebrow">Error 404</p><h1>Page not found</h1><p class="lead">That address does not exist on this site. It may have moved, or the link may be incomplete.</p></header><section class="section"><h2>Try one of these</h2><div class="personal-topics"><a href="index.html">Home{{icon:arrow-right}}</a><a href="publications.html">Publications{{icon:arrow-right}}</a><a href="cv.html">CV{{icon:arrow-right}}</a><a href="personal.html">Personal{{icon:arrow-right}}</a></div></section>'
(ROOT / '404.html').write_text(render('404', 'Page not found · Md. Tariquzzaman', 'That page does not exist on this site.', SITE + '404.html', not_found, noindex=True))

today = date.today().isoformat()
urls = [SITE if s == 'index' else SITE + s + '.html' for s, _, _, _ in pages] + publication_routes
url_xml = ''.join(f'<url><loc>{escape(u)}</loc><lastmod>{today}</lastmod></url>' for u in urls)
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+url_xml+'</urlset>\n')
(ROOT / 'robots.txt').write_text(f'''User-agent: *
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: {SITE}sitemap.xml
''')
llms = '# Md. Tariquzzaman\n\nAcademic website: '+SITE+'\n\nResearch: misinformation and harmful content; LLM evaluation and bias; low-resource and Bangla NLP; accessibility and sign language.\n\n## Pages\n- [Research]('+SITE+'research.html)\n- [Publications]('+SITE+'publications.html)\n- [CV]('+SITE+'cv.html)\n\n## Publications\n' + ''.join(f'- [{p["title"]}]({SITE}publications/{p["id"]}/)\n' for p in papers)
(ROOT / 'llms.txt').write_text(llms)
print(f'Built {len(pages)} static pages, {len(papers)} publication pages, plus 404.html, sitemap.xml, robots.txt, and llms.txt.')
