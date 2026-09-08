"""Render the curated primary-source and preferred-variant gallery."""
from pathlib import Path
from urllib.parse import quote
import html,json
ROOT=Path(__file__).resolve().parents[1]
BRANCH='https://github.com/TQNL/minecraft-update-artwork/tree/ai-reconstruction/'

def render():
    data=json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'))
    selection=json.loads((ROOT/'.catalogue/showcase.json').read_text(encoding='utf-8'))
    preferred=set(selection['preferred_variants']);titles=set(selection['title_only_references'])
    assets=data['assets'];ids={a['id'] for a in assets};assert preferred|titles<=ids
    selected=[a for a in assets if a.get('primary') or a['id'] in preferred|titles]
    groups=list(dict.fromkeys(a['update'] for a in selected));esc=html.escape
    page=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Minecraft update key art: primary originals and selected reconstructed variants, newest first."><title>Key Art Showcase · Minecraft Update Artwork</title><link rel="stylesheet" href=".catalogue/style.css"><link rel="stylesheet" href=".catalogue/showcase.css"></head><body>',
    '<header><p class="eyebrow">THE KEY ART SELECTION</p><h1>Originals &amp;<br>preferred variants<span>.</span></h1><p class="intro">The primary source for each update, alongside selected reconstructed and custom versions.</p>',
    f'<p class="stats">{sum(bool(a.get("primary")) for a in selected)} primary sources <span>/</span> {len(preferred)} preferred variants</p>',
    '<nav aria-label="Gallery navigation"><a href="showcase.html" aria-current="page">Key art showcase</a><a href="index.html">Complete gallery</a><a href="'+BRANCH+'reconstruction/RESULTS.md">Methods &amp; quality notes</a><a href="'+BRANCH+'">Repository</a></nav>',
    '<p class="selection-note">Browse newest first. Original files remain available beside every added version. “Preferred” identifies the variants selected for this gallery, not an official publisher ranking. Two older title-only references follow the scene artwork.</p>',
    '<div class="filters"><label for="search">Find an update</label><input id="search" type="search" placeholder="Search an update, asset ID or title"><label for="type">Show</label><select id="type"><option value="">Originals &amp; variants</option><option>Primary source</option><option>Preferred variant</option><option>Title reference</option></select></div><p id="count" role="status" aria-live="polite"></p></header><main>']
    for n,group in enumerate(groups,1):
        rows=[a for a in selected if a['update']==group]
        rows.sort(key=lambda a:0 if a.get('primary') else 1)
        page.append(f'<section class="update"><h2><span>{n:02}</span>{esc(group)}</h2>')
        if not any(a['id'] in preferred for a in rows):
            note='Standalone title reference; no collected key-art scene.' if all(a['id'] in titles for a in rows) else 'Primary source retained. No reconstructed variant was requested for this update.'
            page.append(f'<p class="family-note">{note}</p>')
        page.append('<div class="grid">')
        for a in rows:
            role='Primary source' if a.get('primary') else 'Preferred variant' if a['id'] in preferred else 'Title reference'
            file=quote(a['file'],safe='/');needle=esc(f'{group} {a["id"]} {a["title"]} {a["classification"]}'.lower(),quote=True)
            page.append(f'<article class="card" data-search="{needle}" data-type="{role}"><a class="image" href="{file}" aria-label="View full-size {esc(a["id"],quote=True)}: {esc(a["title"],quote=True)}"><img loading="lazy" src="{a["preview"]}" alt="{esc(group+": "+a["title"],quote=True)}"></a><div class="info"><p class="tag">{role} · {esc(a["classification"])}</p><h3>{esc(a["id"]+" · "+a["title"])}</h3><p class="dimensions">{a["width"]:,} × {a["height"]:,}<span>{a["format"]}</span></p>')
            if a.get('note'):page.append(f'<p class="note">{esc(a["note"])}</p>')
            page.append(f'<div class="links"><a href="{file}">View full size ↗</a><a href="{file}" download>Download ↓</a></div></div></article>')
        page.append('</div></section>')
    page.append('<p id="empty" hidden>No artwork matches. Try another update or clear the filters.</p></main><footer>Independent archive · Artwork belongs to its respective creators · Added variants are clearly labelled; enlarged dimensions do not establish native detail. <a href="index.html">Browse every version</a></footer><script src=".catalogue/filter.js"></script></body></html>')
    (ROOT/'showcase.html').write_text('\n'.join(page),encoding='utf-8')
    print(json.dumps({'showcase_images':len(selected),'preferred_variants':len(preferred),'update_groups':len(groups)}))

if __name__=='__main__':render()
