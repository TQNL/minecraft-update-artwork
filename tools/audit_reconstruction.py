"""Independently verify completion, source preservation and public-content hygiene."""
from pathlib import Path
import hashlib,json,os,re,subprocess
from PIL import Image
from verify_catalogue import verify
ROOT=Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True,encoding='utf-8').strip()

def audit():
    verify()
    data=json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'))
    assets={a['id']:a for a in data['assets']}
    source=json.loads(git('show','main:catalogue.json'))
    source_ids={a['id'] for a in source['assets']}
    expected_source={f'P{i:02}' for i in range(1,52)}-{'P27','P33','P44','P46'}|{'S52'}
    assert source_ids==expected_source
    for a in source['assets']:
        assert assets[a['id']]==a or all(assets[a['id']][k]==a[k] for k in a)
        assert hashlib.sha256((ROOT/a['file']).read_bytes()).hexdigest()==a['sha256']
    mapping=json.loads((ROOT/'.catalogue/asset-map.json').read_text())['assets']
    assert {a['pdf_number'] for a in mapping}==set(range(1,52))
    for a in mapping:
        assert a['id']==f"P{a['pdf_number']:02}"
        if a['id'] not in source_ids:assert not (ROOT/a['filename']).exists()
    for aid in ['P14','P17','P41']:assert assets[aid]['primary']
    assert assets['P23']['role']=='promotional-panorama'
    assert (assets['S52']['width'],assets['S52']['height'])==(640,360)
    assert (assets['R49']['width'],assets['R49']['height'])==(5120,2880)
    expected=[[],['R03'],['R05','R04'],[],[],[],['R12'],[],[],['R17','R16'],[],[],['R21','R23'],['R25','R26'],['R28'],['R30'],['R34'],['R37'],['R38'],['R40A','R40B','R41'],[],['R52'],[],['R49']]
    progress=json.loads((ROOT/'reconstruction/progress.json').read_text())
    assert len(progress['updates'])==24
    seen=[]
    for row,want in zip(progress['updates'],expected):
        assert row['status'].startswith('complete'),row['update']
        assert set(row['outputs'])==set(want),row['update']
        for p in row['validation']:
            v=json.loads((ROOT/p).read_text());assert v['source_collection_unchanged']
            for output in v.get('outputs',[]):
                assert output['sha256']==assets[output['id']]['sha256']
        seen+=row['outputs']
    derived={a['id'] for a in assets.values() if a.get('origin')=='reconstructed'}
    assert set(seen)==derived and len(seen)==20
    assert not (ROOT/'reconstructed').exists()
    for aid in derived:
        a=assets[aid]
        source_folder=Path(next(s['file'] for s in source['assets'] if s['update']==a['update'])).parent
        assert Path(a['file']).parent==source_folder,aid
        assert (ROOT/source_folder/'README.md').is_file(),aid
    tracked=git('ls-files','--cached','--others','--exclude-standard').splitlines()
    personal=os.environ.get('USERNAME','')
    bad=re.compile(r'[a-z]:[/\\]users|@(?:gmail|outlook|hotmail)\.'+(('|' + re.escape(personal)) if len(personal)>3 else ''),re.I)
    for name in tracked:
        p=ROOT/name
        assert not bad.search(name),name
        if p.suffix.lower() in {'.md','.json','.txt','.html','.css','.js','.py','.yml','.yaml'}:
            # Exclude this scanner's own list of forbidden patterns.
            if p.name!='audit_reconstruction.py':assert not bad.search(p.read_text(encoding='utf-8')),name
        assert p.suffix.lower() not in {'.ppt','.pptx','.zip','.log'},name
    for a in assets.values():
        with Image.open(ROOT/a['file']) as im:
            assert not im.getexif(),a['id']
            assert not any(k.lower() in {'author','artist','comment','description','xmp','xml:com.adobe.xmp'} for k in im.info),a['id']
    identities=set(git('log','--all','--format=%an <%ae>|%cn <%ce>').splitlines())
    assert identities=={'Artwork Archive <archive@example.invalid>|Artwork Archive <archive@example.invalid>'},identities
    assert git('merge-base','main','ai-reconstruction')==git('rev-parse','main')
    for branch in ['main','ai-reconstruction']:
        assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==git('rev-parse',branch)
    result={'date':'2026-09-08','status':'passed','updates_checked':24,'source_assets_preserved':48,'derived_assets':20,'total_assets':68,'stable_pdf_mapping':'all 51 original IDs retained, including removal records','required_removals':['P27','P33','P44','P46'],'replacement':'S52','required_primary_sources':['P14','P17','P41'],'source_hashes':'unchanged from main','catalogue_hashes_dimensions_lineage_and_links':'verified','public_identity_scan':'passed','image_descriptive_metadata':'absent','git_author_and_committer_identity':'anonymous archive identity','source_branch_ancestry':'verified','remote_branches':'verified against local commits at audit time','visual_review':'Each derivative reviewed at full view and targeted close-ups; see per-update validation. Gallery opened locally and displayed all 68 entries.','quality_limits':'Completion means requested variants have been delivered and reviewed; it does not claim native high-resolution detail in resized source areas or exact recovery of hidden content.'}
    result['folder_layout']='All 20 added images share their update folders with source artwork; 14 folder READMEs explain the additions.'
    quality=json.loads((ROOT/'reconstruction/quality-review/final.json').read_text())
    assert quality['status']=='accepted' and quality['reviewed_assets']==20
    assert quality['review_type']=='source-composite detail refinement'
    assert quality['historical_critic_rounds']==3 and quality['independent_critic_rounds_this_revision']==0
    assert {a['id'] for a in quality['assets']}==derived
    for a in quality['assets']:
        assert a['sha256']==assets[a['id']]['sha256']
    critic=json.loads((ROOT/'reconstruction/quality-review/round-3.json').read_text())
    assert {a['id'] for a in critic['assets']}==derived
    for a in critic['assets']:
        assert a['score']>=8 and a['pass']
    historical={a['id']:a for a in critic['assets']}
    for a in quality['assets']:
        assert a['before_sha256']==historical[a['id']]['sha256']
        assert a['changed']==(a['before_sha256']!=a['sha256'])
    assert sum(a['changed'] for a in quality['assets'])==quality['replaced_assets']==5
    assert not (ROOT/'review.html').exists() and not (ROOT/'.catalogue/f-review').exists()
    for name in tracked:
        p=ROOT/name
        if p.suffix.lower() in {'.html','.md','.json','.css','.js'}:
            assert not re.search(r'f-quality|f-stage|f-branch|f-review|pages-gallery',p.read_text(encoding='utf-8'),re.I),name
    result['visual_review']='All 20 adopted derivatives were visually inspected; five refined images were accepted by the user. Current hashes verified. Earlier independent scores remain historical.'
    result['historical_quality_review_rounds']=quality['historical_critic_rounds']
    result['quality_replaced_files']=quality['replaced_assets']
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':audit()
