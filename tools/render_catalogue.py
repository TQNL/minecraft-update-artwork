"""Render the offline gallery and source guide from catalogue.json."""
from pathlib import Path
import html
import json
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

def render():
    data = json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'))
    assets = data['assets']; groups = list(dict.fromkeys(a['update'] for a in assets))
    esc = html.escape
    reconstruction = data.get('collection') == 'reconstruction'
    branch_link = 'https://github.com/TQNL/minecraft-update-artwork/tree/ai-reconstruction'
    readme = f'''# Minecraft Update Artwork

A visual archive of Minecraft update artwork, from **Wilderness Bound** to the **Redstone Update**, arranged newest first.

![Wilderness Bound key art](.catalogue/previews/01.jpg)

**{len(assets)} images · {len(groups)} updates**

Open **[index.html](index.html)** for the searchable offline gallery. Primary labels identify the archive's preferred source scene; they do not assert an official publisher ranking.

## Source collection and reconstructions

The default branch contains collected source artwork. The **[ai-reconstruction branch]({branch_link})** contains separately labelled reconstructions, enhancements and custom title treatments. Source files remain alongside derivatives except for the documented collection removals and replacements.

**[Reconstruction guide](RECONSTRUCTION.md)** · **[Stable PDF asset mapping](ASSET-MAP.md)** · **[Sources](SOURCES.md)** · **[Catalogue](catalogue.json)** · **[Credits](CREDITS.md)**

## Browse the collection

| Update | Files | Primary source |
| :--- | ---: | :--- |
'''
    for group in groups:
        rows=[a for a in assets if a['update']==group]; primary=next((a for a in rows if a.get('primary')),None)
        ref=f'[{primary["id"]}]({primary["file"]})' if primary else 'Separate title references'
        readme+=f'| [{group}]({Path(rows[0]["file"]).parent.as_posix()}) | {len(rows)} | {ref} |\n'
    readme+='''
## About the files

- Original compositions and title treatments are kept separately.
- Dimensions describe stored pixels, not guaranteed native detail.
- Source artwork, promotional banners, fan art and reconstructed variants are distinguished in the catalogue.
- Descriptive metadata is removed from published image files.
- Stable asset IDs retain the numbers used in the PDF reviews; removed entries are not renumbered.

This is an independent archive. Artwork and trademarks belong to their respective creators; inclusion does not grant a new licence.
'''
    if reconstruction:readme=readme.replace('## Browse the collection','This checkout includes reconstructed derivatives. See **[progress and validation](reconstruction/progress.json)** for completed work and limitations.\n\n## Browse the collection')
    (ROOT/'README.md').write_text(readme,encoding='utf-8')
    source='# Sources and resolution notes\n\nSource references and stored dimensions are recorded below. Older attribution gaps remain explicit. Promotional panoramas are separate from key-art scenes.\n\nDirect wallpaper ZIPs for six recent updates were unavailable during collection; they may contain additional variants.\n\n'
    kinds=list(dict.fromkeys(a['classification'] for a in assets))
    page=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Minecraft Update Artwork</title><link rel="stylesheet" href=".catalogue/style.css"></head><body>',
          '<header><p class="eyebrow">THE UPDATE COLLECTION</p><h1>Minecraft<br>Update Artwork<span>.</span></h1><p class="intro">Source artwork and clearly identified variants, newest first.</p>',
          f'<p class="stats">{len(assets)} images <span>/</span> {len(groups)} updates <span>/</span> '+('Reconstruction branch' if reconstruction else 'Source collection')+'</p>',
          '<nav aria-label="Collection resources"><a href="README.md">Collection guide</a><a href="SOURCES.md">Sources</a><a href="RECONSTRUCTION.md">Reconstructions</a><a href="ASSET-MAP.md">PDF asset mapping</a></nav>',
          '<div class="filters"><label for="search">Find artwork</label><input id="search" type="search" placeholder="Search an update, ID or variant"><label for="type">Artwork type</label><select id="type"><option value="">All types</option>'+''.join(f'<option>{esc(k)}</option>' for k in kinds)+'</select></div><p id="count" role="status" aria-live="polite"></p></header><main>']
    for n,group in enumerate(groups,1):
        source+=f'## {group}\n\n'
        page.append(f'<section class="update"><h2><span>{n:02d}</span>{esc(group)}</h2><div class="grid">')
        for a in [x for x in assets if x['update']==group]:
            file=quote(a['file'],safe='/');badge=' · Primary source' if a.get('primary') else ''
            tag=a['classification']+badge
            source+=f'### {a["id"]}: {a["title"]}\n\n[{a["width"]} × {a["height"]} {a["format"]}]({a["file"]}) · {tag}\n\n'
            if a.get('creator'):source+=f'Creator: {a["creator"]}.\n\n'
            if a.get('source_page'):source+=f'[Source reference]({a["source_page"]})\n\n'
            if a.get('source_image'):source+=f'[Source image]({a["source_image"]})\n\n'
            if a.get('note'):source+=a['note']+'\n\n'
            if a.get('derived_from'):source+='Source asset IDs: '+', '.join(a['derived_from'])+'.\n\n'
            needle=esc(f'{group} {a["id"]} {a["title"]} {tag}'.lower(),quote=True)
            page.append(f'<article class="card" data-search="{needle}" data-type="{esc(a["classification"],quote=True)}"><a class="image" href="{file}"><img loading="lazy" src="{a["preview"]}" alt="{esc(group+": "+a["title"],quote=True)}"></a><div class="info"><p class="tag">{esc(tag)}</p><h3>{esc(a["id"]+" · "+a["title"])}</h3><p class="dimensions">{a["width"]:,} × {a["height"]:,}<span>{a["format"]}</span></p>')
            if a.get('note'):page.append(f'<p class="note">{esc(a["note"])}</p>')
            page.append(f'<div class="links"><a href="{file}" download>Download image ↓</a>')
            if a.get('source_page'):page.append(f'<a href="{esc(a["source_page"],quote=True)}" rel="noreferrer">Source ↗</a>')
            page.append('</div></div></article>')
        page.append('</div></section>')
    page.append(f'<p id="empty" hidden>No artwork matches. Try another update or clear the filters.</p></main><footer>Independent archive · Artwork belongs to its respective creators · Updated {data["updated"]}</footer><script src=".catalogue/filter.js"></script></body></html>')
    (ROOT/'index.html').write_text('\n'.join(page),encoding='utf-8')
    (ROOT/'SOURCES.md').write_text(source,encoding='utf-8')

if __name__=='__main__':render()
