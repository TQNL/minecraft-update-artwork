"""Check catalogue files, pixel dimensions, hashes, links and derivative lineage."""
from pathlib import Path
import hashlib,json,re
from urllib.parse import unquote
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]

def verify():
    data=json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'));assets=data['assets']
    ids={a['id'] for a in assets};assert len(ids)==len(assets)
    files=set()
    for a in assets:
        p=ROOT/a['file'];assert p.is_file(),p
        assert a['file'] not in files;files.add(a['file'])
        raw=p.read_bytes();assert len(raw)==a['bytes'] and hashlib.sha256(raw).hexdigest()==a['sha256'],a['id']
        with Image.open(p) as im:
            assert im.size==(a['width'],a['height']) and im.format==a['format'],a['id']
            assert not im.getexif()
        assert (ROOT/a['preview']).is_file(),a['id']
        if a.get('derived_from'):
            assert all(n in ids for n in a['derived_from']),a['id']
            assert a.get('origin')=='reconstructed' and not a.get('primary'),a['id']
    actual={p.relative_to(ROOT).as_posix() for directory in ['artwork','reconstructed'] for p in (ROOT/directory).rglob('*') if p.is_file() and p.name!='README.md'}
    assert files==actual,(files-actual,actual-files)
    page=(ROOT/'index.html').read_text(encoding='utf-8')
    assert page.count('<article ')==len(assets)
    showcase=ROOT/'showcase.html'
    if showcase.exists():
        selection=json.loads((ROOT/'.catalogue/showcase.json').read_text())
        chosen=set(selection['preferred_variants'])|set(selection['title_only_references'])|{a['id'] for a in assets if a.get('primary')}
        assert chosen<=ids
        curated=showcase.read_text(encoding='utf-8')
        assert curated.count('<article ')==len(chosen)
        page+='\n'+curated
    for target in re.findall(r'(?:href|src)="([^"]+)"',page):
        if not target.startswith(('http:','https:','#')):assert (ROOT/unquote(target)).is_file(),target
    for p in [ROOT/'README.md',ROOT/'SOURCES.md',ROOT/'ASSET-MAP.md',ROOT/'RECONSTRUCTION.md',*list((ROOT/'reconstruction').glob('*.md')),*list((ROOT/'artwork').glob('*/README.md'))]:
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if not target.startswith(('http:','https:','#')):assert (p.parent/unquote(target)).exists(),(p,target)
    print(json.dumps({'assets':len(assets),'hashes_dimensions_links':'verified','derived':sum(a.get('origin')=='reconstructed' for a in assets)}))

if __name__=='__main__':verify()
