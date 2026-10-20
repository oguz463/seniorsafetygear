#!/usr/bin/env python3
"""Builds the SeniorSafetyGear static site into dist/.

Content lives in content/: site.py (site-wide settings and simple pages) and guides/*.py (one buying guide per
file) and articles/*.py (informational articles, no affiliate links). Run `python3 build.py`; Cloudflare Pages runs the same command and serves dist/.
"""
import datetime
import html
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / 'dist'


def _git(*args):
    try:
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ''


# Git dates are only trusted in a full clone; a shallow clone would date every file to the latest commit.
# CI builds (Cloudflare Workers Builds) may clone shallow, so try to fetch the history first.
if _git('rev-parse', '--is-shallow-repository') == 'true':
    try:
        subprocess.run(['git', 'fetch', '--unshallow', '--quiet'], cwd=ROOT, capture_output=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        pass
GIT_HISTORY = _git('rev-parse', '--is-shallow-repository') == 'false'


def lastmod(mod):
    """Sitemap date for a content module: the later of its UPDATED date and the last commit that changed its file.
    A file with uncommitted edits counts as changed today."""
    dates = [mod.UPDATED]
    if GIT_HISTORY:
        path = str(pathlib.Path(mod.__file__).relative_to(ROOT))
        if _git('status', '--porcelain', '--', path):
            dates.append(datetime.date.today())
        else:
            committed = _git('log', '-1', '--format=%cs', '--', path)
            if committed:
                dates.append(datetime.date.fromisoformat(committed))
    return max(dates)


def added_at(mod):
    """Sort key for newest-first lists: PUBLISHED, then the time the file was first committed, so pages published the
    same day still list in the order they went live. Files not committed yet sort as newest."""
    when = datetime.datetime.min
    if GIT_HISTORY:
        path = str(pathlib.Path(mod.__file__).relative_to(ROOT))
        first = _git('log', '--diff-filter=A', '--follow', '--format=%cI', '--', path).splitlines()
        when = datetime.datetime.fromisoformat(first[-1]).replace(tzinfo=None) if first else datetime.datetime.max
    return (mod.PUBLISHED, when, mod.TITLE)


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


site = load(ROOT / 'content' / 'site.py')
guides = sorted((load(p) for p in (ROOT / 'content' / 'guides').glob('*.py')), key=added_at, reverse=True)
articles = sorted((load(p) for p in (ROOT / 'content' / 'articles').glob('*.py')), key=added_at, reverse=True)
tools = sorted((load(p) for p in (ROOT / 'content' / 'tools').glob('*.py')), key=lambda t: t.TITLE)
e = html.escape


TITLE_CASE_SMALL_WORDS = {
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in', 'into', 'nor',
    'of', 'on', 'onto', 'or', 'over', 'per', 'the', 'to', 'up', 'via', 'vs', 'with', 'yet',
}


def title_case(text, capitalize_first=True):
    words = list(re.finditer(r"\b[\w]+(?:['’][\w]+)*\b", text))
    first_word = words[0].start() if words else -1

    def format_word(match):
        word = match.group()
        if re.fullmatch(r"[A-Z]{2,5}(?:['’]s)?", word) or (any(c.isupper() for c in word[1:]) and any(c.islower() for c in word)):
            return word
        lower = word.lower()
        previous_word = next((candidate for candidate in reversed(words) if candidate.end() <= match.start()), None)
        starts_phrase = (
            match.start() == first_word
            or previous_word is not None and re.search(r'[:!?]\W*$', text[previous_word.end():match.start()])
        )
        if lower in TITLE_CASE_SMALL_WORDS and not (capitalize_first and starts_phrase):
            return lower
        return lower[0].upper() + lower[1:]

    return re.sub(r"\b[\w]+(?:['’][\w]+)*\b", format_word, text)


def title_case_html(text):
    def format_heading(match):
        first_word_seen = False

        def format_part(part):
            nonlocal first_word_seen
            if part.group(1):
                return part.group(1)
            content = html.unescape(part.group(2))
            formatted = title_case(content, capitalize_first=not first_word_seen)
            if re.search(r"\b[\w]+(?:['’][\w]+)*\b", content):
                first_word_seen = True
            return e(formatted)

        inner = re.sub(
            r'(<[^>]+>)|([^<]+)',
            format_part,
            match.group(2),
        )
        return f'{match.group(1)}{inner}{match.group(3)}'

    return re.sub(r'(<h[1-4]\b[^>]*>)(.*?)(</h[1-4]>)', format_heading, text, flags=re.IGNORECASE | re.DOTALL)


def amazon(query):
    from urllib.parse import quote_plus
    return f'https://www.amazon.com/s?k={quote_plus(query)}&tag={site.AMAZON_TAG}'


def page(path, title, description, body, schema=None, canonical=None, image=None, has_toc=False, home=False):
    url = site.BASE_URL + path
    body = title_case_html(body)
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ''
    og_image = f'\n<meta property="og:image" content="{site.BASE_URL}/img/hero/{image}.jpg">\n<meta name="twitter:card" content="summary_large_image">' if image else ''
    nav = ''.join(f'<a href="{href}">{e(label)}</a>' for label, href in site.NAV)
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(canonical or url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(url)}">{og_image}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48.png" type="image/png" sizes="48x48">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/atkinson-hyperlegible-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/source-serif-4-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="strip"><div class="wrap"><span>Independent research for older adults and their families</span><a href="/disclosure/">We earn from qualifying Amazon purchases</a></div></div>
<header class="top"><div class="wrap"><a class="logo" href="/" aria-label="SeniorSafetyGear home"><svg class="mark" width="40" height="40" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#fff"/><path d="M20 7l11 4v8c0 7-4.6 11.6-11 14-6.4-2.4-11-7-11-14v-8z" fill="#12355c"/><path d="M14.5 20.5l4 4 7.5-8.5" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg><span class="word">SeniorSafety<span>Gear</span></span></a><button class="nav-toggle" type="button" aria-controls="primary-navigation" aria-expanded="false"><span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span><span>Menu</span></button><nav id="primary-navigation" aria-label="Main navigation">{nav}</nav></div></header>
<main id="main" class="{'home' if home else 'wrap' + (' has-toc' if has_toc else '')}">
{body}
</main>
<footer class="foot">
<div class="wrap foot-grid">
<div><p class="foot-logo">SeniorSafetyGear</p><p>Buying guides for mobility and bathroom safety equipment, built on public safety guidance and the makers' own specs.</p><p class="small">{e(site.DISCLOSURE)}</p></div>
<div><p class="foot-head">Guides</p><ul>{foot_guides()}</ul></div>
<div><p class="foot-head">The site</p><ul><li><a href="/how-we-research/">How we research</a></li><li><a href="/about/">About</a></li><li><a href="/articles/">Articles</a></li><li><a href="/tools/">Tools</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/disclosure/">Affiliate disclosure</a></li></ul></div>
</div>
<div class="wrap fine"><p>© {datetime.date.today().year} SeniorSafetyGear. Not medical advice: ask a doctor or therapist about your own needs.</p></div>
</footer>
<script>
const menuToggle = document.querySelector('.nav-toggle');
const mainNavigation = document.querySelector('#primary-navigation');
const tocDialog = document.querySelector('.toc-dialog');
const tocToggle = document.querySelector('.toc-toggle');
function closeMenu() {{
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.lastElementChild.textContent = 'Menu';
  mainNavigation.classList.remove('is-open');
}}
menuToggle.addEventListener('click', () => {{
  const isOpen = menuToggle.getAttribute('aria-expanded') !== 'true';
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.lastElementChild.textContent = isOpen ? 'Close' : 'Menu';
  mainNavigation.classList.toggle('is-open', isOpen);
}});
mainNavigation.addEventListener('click', event => {{
  if (event.target.closest('a')) closeMenu();
}});
document.addEventListener('keydown', event => {{
  if (event.key === 'Escape') {{
    if (menuToggle.getAttribute('aria-expanded') === 'true') {{
      closeMenu();
      menuToggle.focus();
    }}
    if (tocDialog?.open) {{
      tocDialog.close();
      tocToggle.focus();
    }}
  }}
}});
if (tocDialog && tocToggle) {{
  tocToggle.addEventListener('click', () => tocDialog.showModal());
  tocDialog.querySelector('.toc-dialog-close').addEventListener('click', () => tocDialog.close());
  tocDialog.addEventListener('click', event => {{
    if (event.target.closest('a')) tocDialog.close();
  }});
}}
</script>
</body>
</html>
'''
    target = DIST / path.strip('/') / 'index.html' if path != '/' else DIST / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(out, encoding='utf-8')


def foot_guides():
    return ''.join(f'<li><a href="/guides/#{cat_slug(c)}">{e(c)}</a></li>' for c, _ in guides_by_category())


def hero(name, alt):
    return (f'<figure class="hero-photo"><img src="/img/hero/{name}.jpg" srcset="/img/hero/{name}-800.jpg 800w, /img/hero/{name}.jpg 1600w" '
            f'sizes="(max-width: 860px) 100vw, 828px" alt="{e(alt)}" width="1600" height="1067" fetchpriority="high"></figure>')


def related_articles(slug):
    items = ''.join(f'<li><a href="/articles/{a.SLUG}/">{e(title_case(a.TITLE))}</a></li>' for a in articles if slug in a.RELATED)
    return f'<h2>Related reading</h2><ul class="related">{items}</ul>' if items else ''


def mobile_toc(title, toc):
    return f'''<button class="toc-toggle" type="button" aria-haspopup="dialog" aria-controls="mobile-toc-dialog">Contents</button>
<dialog class="toc-dialog" id="mobile-toc-dialog" aria-labelledby="mobile-toc-title">
<div class="toc-dialog-header"><h2 id="mobile-toc-title">{title}</h2><button class="toc-dialog-close" type="button" aria-label="Close contents">Close</button></div>
<nav aria-label="Contents"><ol>{toc}</ol></nav>
</dialog>'''


def compare_table(g):
    c = getattr(g, 'COMPARE', None)
    if not c:
        return ''
    # Amazon ratings stay in each guide's research notes, not on the page.
    keep = [i for i, col in enumerate(c['cols']) if col != 'Rating']
    head = ''.join(f'<th>{e(x)}</th>' for x in ['Pick'] + [c['cols'][i] for i in keep])
    rows = ''.join(f'<tr><th><a href="#{p["id"]}">{e(title_case(p["name"]))}</a></th>'
                   + ''.join(f'<td>{e(c["rows"][p["id"]][i])}</td>' for i in keep) + '</tr>' for p in g.PRODUCTS)
    return (f'<h2 id="compare">Compare the {len(g.PRODUCTS)} picks</h2><div class="scroll"><table class="compare"><thead><tr>{head}</tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


def guide_body(g):
    picks = ''.join(f'<tr><td>{e(p["rank"])}</td><td><a href="#{p["id"]}">{e(title_case(p["name"]))}</a></td>'
                    f'<td><a href="{e(amazon(p["q"]))}" rel="nofollow sponsored noopener" target="_blank">Check price</a></td></tr>'
                    for p in g.PRODUCTS)
    cards = []
    for i, p in enumerate(g.PRODUCTS, 1):
        specs = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in list(p['specs'].items()))
        pros = ''.join(f'<li>{e(x)}</li>' for x in p['pros'])
        cons = ''.join(f'<li>{e(x)}</li>' for x in p['cons'])
        text = ''.join(f'<p>{x}</p>' for x in p['text'])
        text += ''.join(f'<h4>{e(h)}</h4>{body}' for h, body in p.get('sections', []))
        if p.get('best_for') or p.get('skip_if'):
            text += (f'<p class="fit"><strong>Best for:</strong> {p.get("best_for", "")}<br>'
                     f'<strong>Skip it if:</strong> {p.get("skip_if", "")}</p>')
        cards.append(f'''<section class="card" id="{p["id"]}">
<div class="card-media"><span class="badge">#{i}</span><img src="/img/{p["img"]}" alt="{e(p["alt"])}" width="400" height="400" loading="lazy"><a class="btn" href="{e(amazon(p["q"]))}" rel="nofollow sponsored noopener" target="_blank">Check price on Amazon</a></div>
<div class="card-main">
<p class="rank">{e(p["rank"])}</p>
<h3>{e(title_case(p["name"]))}</h3>
<dl class="specs">{specs}</dl>
{text}
<div class="pc"><div class="pro"><h4>Good for</h4><ul>{pros}</ul></div><div class="con"><h4>Watch out for</h4><ul>{cons}</ul></div></div>
</div>
</section>''')
    top = g.PRODUCTS[0]
    verdict = (f'<aside class="verdict"><img src="/img/{top["img"]}" alt="{e(top["alt"])}" width="400" height="400">'
               f'<div><p class="verdict-label">Our top pick</p><p class="verdict-name"><a href="#{top["id"]}">{e(title_case(top["name"]))}</a></p>'
               f'<p>{top.get("best_for", "")}</p><p class="verdict-actions"><a class="btn" href="{e(amazon(top["q"]))}" rel="nofollow sponsored noopener" target="_blank">Check price on Amazon</a> '
               f'<a class="link" href="#{top["id"]}">Read why</a></p></div></aside>')
    sources = ''.join(f'<li><a href="{e(u)}" rel="noopener" target="_blank">{e(label)}</a></li>' for label, u in g.SOURCES)
    body, heads = with_ids(g.BODY)
    extra = [('compare', f'Compare the {len(g.PRODUCTS)} picks')] if getattr(g, 'COMPARE', None) else []
    toc = ''.join(f'<li><a href="#{i}">{e(title_case(t))}</a></li>' for i, t in [('picks', g.CARDS_HEADING)] + extra + heads)
    return f'''<article class="guide">
<p class="crumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › <a href="/guides/#{cat_slug(g.CATEGORY)}">{e(g.CATEGORY)}</a></p>
<h1>{e(g.TITLE)}</h1>
    <div class="guide-layout">
    <div class="guide-meta">
    <p class="byline">By <a href="/about/#author">{e(site.AUTHOR)}</a> · Updated {g.UPDATED:%B %-d, %Y}</p>
    <p class="disclose">{e(site.DISCLOSURE)}</p>
    </div>
    <nav class="toc" aria-label="Table of Contents"><strong>Table of Contents</strong><ol>{toc}</ol></nav>
    <div class="guide-content">
    {hero(g.PHOTO, g.PHOTO_ALT)}
{g.INTRO}
{verdict}
<table class="picks"><thead><tr><th>Best for</th><th>Pick</th><th>Amazon</th></tr></thead><tbody>{picks}</tbody></table>
<h2 id="picks">{e(g.CARDS_HEADING)}</h2>
{''.join(cards)}
{compare_table(g)}
{body}
{related_articles(g.SLUG)}
<h2>Sources</h2><ul class="sources">{sources}</ul>
</div>
</div>
{mobile_toc('Table of Contents', toc)}
</article>'''


def article_body(a):
    takeaways = ''.join(f'<li>{x}</li>' for x in a.TAKEAWAYS)
    sources = ''.join(f'<li><a href="{e(u)}" rel="noopener" target="_blank">{e(label)}</a></li>' for label, u in a.SOURCES)
    body, heads = with_ids(a.BODY)
    toc = ''.join(f'<li><a href="#{i}">{e(title_case(t))}</a></li>' for i, t in heads)
    related = ''.join(guide_tile(g) for g in guides if g.SLUG in a.RELATED)
    related = f'<h2>Shopping for One?</h2><div class="rows related">{related}</div>' if related else ''
    return f'''<article class="guide article">
<p class="crumbs"><a href="/">Home</a> › <a href="/articles/">Articles</a> › {e(a.TOPIC)}</p>
<h1>{e(a.TITLE)}</h1>
    <div class="guide-layout">
    <div class="guide-meta">
    <p class="byline">By <a href="/about/#author">{e(site.AUTHOR)}</a> · Updated {a.UPDATED:%B %-d, %Y}</p>
    </div>
    <nav class="toc" aria-label="Table of Contents"><strong>Table of Contents</strong><ol>{toc}</ol></nav>
    <div class="guide-content">
    {hero(a.PHOTO, a.PHOTO_ALT)}
<aside class="takeaways"><strong>Key takeaways</strong><ul>{takeaways}</ul></aside>
{body}
{related}
<h2>Sources</h2><ul class="sources">{sources}</ul>
</div>
</div>
{mobile_toc('Table of Contents', toc)}
</article>'''


def article_schema(a):
    url = f'{site.BASE_URL}/articles/{a.SLUG}/'
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Article', 'headline': a.TITLE, 'description': a.DESCRIPTION, 'datePublished': a.PUBLISHED.isoformat(),
         'dateModified': a.UPDATED.isoformat(), 'image': f'{site.BASE_URL}/img/hero/{a.PHOTO}.jpg',
         'author': {'@type': 'Person', 'name': site.AUTHOR, 'url': site.AUTHOR_URL, 'sameAs': site.AUTHOR_SAME_AS}, 'publisher': {'@type': 'Organization', 'name': 'SeniorSafetyGear'}, 'mainEntityOfPage': url},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': site.BASE_URL + '/'},
                                                        {'@type': 'ListItem', 'position': 2, 'name': 'Articles', 'item': site.BASE_URL + '/articles/'},
                                                        {'@type': 'ListItem', 'position': 3, 'name': a.TITLE, 'item': url}]},
    ]}


def guide_schema(g):
    url = f'{site.BASE_URL}/{g.SLUG}/'
    return {
        '@context': 'https://schema.org',
        '@graph': [
            {'@type': 'Article', 'headline': g.TITLE, 'description': g.DESCRIPTION, 'datePublished': g.PUBLISHED.isoformat(),
             'dateModified': g.UPDATED.isoformat(), 'image': f'{site.BASE_URL}/img/hero/{g.PHOTO}.jpg', 'author': {'@type': 'Person', 'name': site.AUTHOR, 'url': site.AUTHOR_URL, 'sameAs': site.AUTHOR_SAME_AS},
             'publisher': {'@type': 'Organization', 'name': 'SeniorSafetyGear'}, 'mainEntityOfPage': url},
            {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i, 'name': p['name'], 'url': f'{url}#{p["id"]}'}
                                                      for i, p in enumerate(g.PRODUCTS, 1)]},
            {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': site.BASE_URL + '/'},
                                                            {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': site.BASE_URL + '/guides/'},
                                                            {'@type': 'ListItem', 'position': 3, 'name': g.TITLE, 'item': url}]},
        ],
    }


def with_ids(body):
    """Gives every <h2> in a body an id and returns the body plus [(id, text)] for a table of contents."""
    import re
    heads = []

    def tag(m):
        text = re.sub(r'<[^>]+>', '', m.group(1))
        slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
        heading = title_case_html(f'<h2>{m.group(1)}</h2>')[4:-5]
        display_text = re.sub(r'<[^>]+>', '', heading)
        heads.append((slug, html.unescape(display_text)))
        return f'<h2 id="{slug}">{heading}</h2>'
    return re.sub(r'<h2>(.*?)</h2>', tag, body), heads


PICKS_JS = """function renderPicks(keys, head) {
  var cards = keys.map(function (k) { return PICKS[k]; }).filter(Boolean).map(function (p) {
    return '<div class="pick"><img src="/img/' + p.img + '" alt="' + p.alt + '" width="400" height="400" loading="lazy"><em>' + p.rank + '</em><strong>' + p.name + '</strong>'
      + '<a class="btn" href="' + p.url + '" rel="nofollow sponsored noopener" target="_blank">Check price on Amazon</a><a class="rev" href="/' + p.guide + '/#' + p.id + '">Read our notes</a></div>';
  });
  return cards.length ? '<span class="picks-head">' + head + '</span><div class="picks-grid">' + cards.join('') + '</div><p class="small">""" + html.escape(site.DISCLOSURE) + """</p>' : '';
}"""


def tool_picks(t):
    """Picks from the guides a tool names in PICK_GUIDES, keyed 'guide-slug/product-id', for the tool's script."""
    out = {}
    for g in guides:
        if g.SLUG in getattr(t, 'PICK_GUIDES', []):
            for p in g.PRODUCTS:
                out[f'{g.SLUG}/{p["id"]}'] = {'id': p['id'], 'guide': g.SLUG, 'name': e(p['name']), 'img': p['img'], 'alt': e(p['alt']),
                                              'price': e(p['price']), 'rank': e(p['rank']), 'url': e(amazon(p['q']))}
    return out


def tool_body(t):
    sources = ''.join(f'<li><a href="{e(u)}" rel="noopener" target="_blank">{e(label)}</a></li>' for label, u in t.SOURCES)
    related = ''.join(f'<li><a href="/{g.SLUG}/">{e(title_case(g.TITLE))}</a></li>' for g in guides if g.SLUG in getattr(t, 'RELATED', []))
    related = f'<h2>Related guides</h2><ul>{related}</ul>' if related else ''
    return f'''<article class="guide tool">
<p class="crumbs"><a href="/">Home</a> › <a href="/tools/">Tools</a></p>
<h1>{e(t.TITLE)}</h1>
<p class="byline">By <a href="/about/#author">{e(site.AUTHOR)}</a> · Updated {t.UPDATED:%B %-d, %Y}</p>
{t.INTRO}
<div class="widget">{t.WIDGET}</div>
{('<script>var PICKS = ' + json.dumps(tool_picks(t)) + ';' + PICKS_JS + '</script>') if getattr(t, 'PICK_GUIDES', None) else ''}
<script>{t.SCRIPT}</script>
{t.BODY}
{related}
<h2>Sources</h2><ul class="sources">{sources}</ul>
</article>'''


CATEGORY_ORDER = ['Walkers & Rollators', 'Canes', 'Bath Safety', 'Toilet & Bedroom', 'Lift & Mobility', 'Daily Living']


def cat_slug(category):
    return re.sub(r'[^a-z0-9]+', '-', category.lower()).strip('-')


def guides_by_category():
    cats = sorted({g.CATEGORY for g in guides}, key=lambda c: (CATEGORY_ORDER.index(c) if c in CATEGORY_ORDER else len(CATEGORY_ORDER), c))
    return [(c, [g for g in guides if g.CATEGORY == c]) for c in cats]


def guides_page_body():
    groups = guides_by_category()
    nav = ''.join(f'<a href="#{cat_slug(c)}">{e(c)} <span>{len(gs)}</span></a>' for c, gs in groups)
    sections = ''.join(f'<h2 id="{cat_slug(c)}">{e(c)}</h2><div class="rows">{"".join(guide_tile(g) for g in gs)}</div>' for c, gs in groups)
    return (f'<h1>Buying guides</h1><p>Research-based guides to mobility aids and bathroom and bedroom safety products for older adults, built on maker specs and public safety guidance.</p>'
            f'<nav class="cat-nav" aria-label="Guide categories">{nav}</nav>{sections}')


def guide_tile(g):
    return (f'<a class="row-card" href="/{g.SLUG}/"><img src="/img/hero/{g.PHOTO}-800.jpg" alt="{e(g.PHOTO_ALT)}" width="800" height="533" loading="lazy">'
            f'<span class="row-text"><em>{e(g.CATEGORY)}</em><strong>{e(title_case(g.TITLE))}</strong><span>{e(g.DESCRIPTION)}</span></span></a>')


def article_tile(a):
    return (f'<a class="row-card" href="/articles/{a.SLUG}/"><img src="/img/hero/{a.PHOTO}-800.jpg" alt="{e(a.PHOTO_ALT)}" width="800" height="533" loading="lazy">'
            f'<span class="row-text"><em>{e(a.TOPIC)}</em><strong>{e(title_case(a.TITLE))}</strong><span>{e(a.DESCRIPTION)}</span></span></a>')


def tool_tile(t):
    return f'<a class="tool-tile" href="/tools/{t.SLUG}/"><strong>{e(title_case(t.NAME))}</strong><span>{e(t.DESCRIPTION)}</span></a>'

CATEGORY_ICONS = {'Walkers & Rollators': '<circle cx="8" cy="30" r="4"/><circle cx="32" cy="30" r="4"/><path d="M8 26V12h24v14M8 18h24"/>', 'Canes': '<path d="M14 36L26 8a6 6 0 1 1 10 4"/>', 'Bath Safety': '<path d="M10 8h12a6 6 0 0 1 6 6v2M6 20h28v4a8 8 0 0 1-8 8H14a8 8 0 0 1-8-8zM12 34l-2 3M28 34l2 3"/>', 'Toilet & Bedroom': '<path d="M4 30V10M4 24h32v6M36 24v-6a4 4 0 0 0-4-4H16v10"/><circle cx="10" cy="19" r="3"/>', 'Lift & Mobility': '<circle cx="20" cy="26" r="9"/><circle cx="20" cy="26" r="2"/><path d="M20 17V8h8M29 8l4 4"/>', 'Daily Living': '<path d="M12 36V16a3 3 0 0 1 6 0v8M18 14V9a3 3 0 0 1 6 0v8M24 14a3 3 0 0 1 6 0v10a12 12 0 0 1-12 12h-2a6 6 0 0 1-5-3L6 26"/>'}
FEATURED = ['best-rollators', 'best-shower-chairs', 'best-raised-toilet-seats', 'best-canes', 'best-bedside-commodes', 'best-lift-chairs']


def home_body():
    cats = ''.join(
        f'<a class="cat" href="/guides/#{cat_slug(c)}"><svg viewBox="0 0 40 40" width="44" height="44" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{CATEGORY_ICONS.get(c, "")}</svg>'
        f'<strong>{e(c)}</strong><span>{len(gs)} guide{"s" if len(gs) != 1 else ""}</span></a>' for c, gs in guides_by_category())
    feat = [g for slug in FEATURED for g in guides if g.SLUG == slug]
    ranked = ''.join(
        f'<li><a href="/{g.SLUG}/"><span class="num">{i}</span><span class="rank-text"><strong>{e(title_case(g.TITLE))}</strong><span>{e(g.DESCRIPTION)}</span></span><span class="go" aria-hidden="true">→</span></a></li>'
        for i, g in enumerate(feat, 1))
    steps = ''.join(f'<div><span class="step-n">{i}</span><strong>{e(t)}</strong><span>{e(d)}</span></div>' for i, (t, d) in enumerate(site.HOME_STEPS, 1))
    tl = ''.join(tool_tile(t) for t in tools)
    arts = ''.join(article_tile(a) for a in articles[:3])
    return f'''<section class="hero-band"><div class="wrap hero-grid">
<div class="hero-copy"><p class="eyebrow">{e(site.HOME_EYEBROW)}</p><h1>{e(site.HOME_H1)}</h1><p class="lead">{e(site.HOME_LEAD)}</p>
<p class="hero-links"><a class="btn" href="/guides/">Browse all {len(guides)} guides</a><a class="btn btn-light" href="/tools/">Free calculators</a></p></div>
<nav class="cats" aria-label="Find a guide by need"><p class="cats-title">Find what you need</p><div class="cat-grid">{cats}</div></nav>
</div></section>
<section class="band"><div class="wrap"><h2>Most searched guides</h2><ol class="rank-list">{ranked}</ol><p class="more"><a href="/guides/">See all {len(guides)} guides →</a></p></div></section>
<section class="band alt"><div class="wrap"><h2>How we research</h2><div class="steps-3">{steps}</div><p class="more"><a href="/how-we-research/">Read our full process →</a></p></div></section>
<section class="band"><div class="wrap"><h2>Free calculators</h2><div class="tool-tiles">{tl}</div></div></section>
<section class="band alt"><div class="wrap"><h2>Latest articles</h2><div class="rows">{arts}</div><p class="more"><a href="/articles/">More articles ({len(articles)}) →</a></p></div></section>'''


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / 'static', DIST)
    for g in guides:
        page(f'/{g.SLUG}/', g.SEO_TITLE, g.DESCRIPTION, guide_body(g), guide_schema(g), image=g.PHOTO, has_toc=True)
    for a in articles:
        page(f'/articles/{a.SLUG}/', a.SEO_TITLE, a.DESCRIPTION, article_body(a), article_schema(a), image=a.PHOTO, has_toc=True)
    for t in tools:
        page(f'/tools/{t.SLUG}/', t.SEO_TITLE, t.DESCRIPTION, tool_body(t),
             {'@context': 'https://schema.org', '@type': 'WebApplication', 'name': t.NAME, 'applicationCategory': 'UtilitiesApplication',
              'operatingSystem': 'Any', 'url': f'{site.BASE_URL}/tools/{t.SLUG}/', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}})
    page('/guides/', 'Senior Safety and Mobility Buying Guides | SeniorSafetyGear', 'Every SeniorSafetyGear buying guide, by category: walkers and rollators, bath safety, toilet and bedroom aids, canes and mobility equipment.',
         guides_page_body())
    page('/articles/', 'Senior Safety Articles and Buying Advice | SeniorSafetyGear', 'Articles on choosing and using mobility and bathroom safety equipment, built on CDC, FDA and CPSC guidance and named sources.',
         f'<h1>Articles</h1><p>How to choose, fit and use mobility and bathroom safety equipment, each built on CDC, FDA and CPSC guidance and named sources.</p><div class="rows">{"".join(article_tile(a) for a in articles)}</div>{site.ARTICLES_NOTES}')
    page('/tools/', 'Senior Safety Tools and Calculators | SeniorSafetyGear', 'Free fit calculators and size charts for walkers, canes and bathroom equipment.',
         f'<h1>Tools</h1><p>Quick calculators and size charts, each built from a named source.</p><div class="tool-tiles">{"".join(tool_tile(t) for t in tools)}</div>{site.TOOLS_NOTES}')
    page('/', site.HOME_TITLE, site.HOME_DESCRIPTION, home_body(),
         {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'SeniorSafetyGear', 'url': site.BASE_URL + '/'}, home=True)
    for slug, (title, description, body) in site.PAGES.items():
        page(f'/{slug}/', title, description, f'<article class="guide"><h1>{e(title.split(" | ")[0])}</h1>{body}</article>')
    content_updated = max(lastmod(item) for item in [site] + guides + articles + tools)
    sitemap_entries = [
        ('/', content_updated),
        ('/guides/', max(lastmod(g) for g in guides)),
        ('/articles/', max((lastmod(a) for a in articles), default=lastmod(site))),
        ('/tools/', max((lastmod(t) for t in tools), default=lastmod(site))),
        *[(f'/{g.SLUG}/', lastmod(g)) for g in guides],
        *[(f'/articles/{a.SLUG}/', lastmod(a)) for a in articles],
        *[(f'/tools/{t.SLUG}/', lastmod(t)) for t in tools],
        *[(f'/{slug}/', lastmod(site)) for slug in site.PAGES],
    ]
    urls = [url for url, _ in sitemap_entries]
    (DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + ''.join(f'<url><loc>{site.BASE_URL}{url}</loc><lastmod>{updated.isoformat()}</lastmod></url>\n'
                                               for url, updated in sitemap_entries) + '</urlset>\n', encoding='utf-8')
    (DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {site.BASE_URL}/sitemap.xml\n', encoding='utf-8')
    redirects = DIST / '_redirects'
    if redirects.exists():
        for line in redirects.read_text(encoding='utf-8').splitlines():
            if line.strip() and not line.startswith('#'):
                src, to, code = line.split()
                assert to in urls, f'_redirects: {src} points to {to}, which is not a built page'
                assert not (DIST / src.strip('/') / 'index.html').exists(), f'_redirects: {src} would shadow a built page'
    print(f'built {len(urls)} pages into {DIST}')


if __name__ == '__main__':
    main()
