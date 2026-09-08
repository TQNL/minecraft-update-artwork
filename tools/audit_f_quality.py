"""Verify F-stage review artifacts, source preservation and public metadata."""
from pathlib import Path
import hashlib,json,re,subprocess,os
from PIL import Image
import numpy as np
from verify_catalogue import verify
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True,encoding='utf-8').strip()
def audit():
    verify()
    data=json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'));assets={a['id']:a for a in data['assets']}
    main=json.loads(git('show','main:catalogue.json'))
    for a in main['assets']:
        assert a==assets[a['id']],a['id']
        assert digest(ROOT/a['file'])==a['sha256'],a['id']
    report=json.loads((ROOT/'reconstruction/quality-review/final.json').read_text())
    assert report==json.loads((ROOT/'.catalogue/f-review/data.json').read_text())
    assert len(report['assets'])==20 and sum(r['changed'] for r in report['assets'])==5
    assert report['new_AI_generation'] is False and report['independent_critic_rounds_this_request']==0
    old=json.loads(git('show',report['baseline_commit']+':catalogue.json'));old={a['id']:a for a in old['assets']}
    for r in report['assets']:
        assert r['before_sha256']==old[r['id']]['sha256']
        assert digest(ROOT/r['before_file'])==r['before_sha256']
        assert digest(ROOT/r['after_file'])==r['sha256']==assets[r['id']]['sha256']
        a=np.array(Image.open(ROOT/r['before_file']).convert('RGB')).astype(np.int16)
        b=np.array(Image.open(ROOT/r['after_file']).convert('RGB')).astype(np.int16)
        d=np.abs(a-b);assert int(d.max())==r['max_channel_change']
        assert abs(float(d.mean())-r['mean_channel_change'])<1e-9
        assert np.any(d)==r['changed']
        assert Image.open(ROOT/r['after_file']).size==(r['width'],r['height'])
    by={r['id']:r for r in report['assets']}
    clean0=np.array(Image.open(ROOT/by['R40A']['before_file']));title0=np.array(Image.open(ROOT/by['R40B']['before_file']))
    clean=np.array(Image.open(ROOT/by['R40A']['after_file']));title=np.array(Image.open(ROOT/by['R40B']['after_file']))
    mask=np.any(clean0!=title0,axis=2)
    assert np.array_equal(clean[~mask],title[~mask])
    assert np.array_equal(title[mask],title0[mask])
    progress=json.loads((ROOT/'reconstruction/progress.json').read_text())
    for row in progress['updates']:
        for name in row['validation']:
            v=json.loads((ROOT/name).read_text());assert v['source_collection_unchanged']
            for output in v.get('outputs',[]):assert output['sha256']==assets[output['id']]['sha256']
    personal=os.environ.get('USERNAME','');bad=re.compile(r'[a-z]:[/\\]users|@(?:gmail|outlook|hotmail)\.'+(('|' + re.escape(personal)) if len(personal)>3 else ''),re.I)
    for name in git('ls-files','--cached','--others','--exclude-standard').splitlines():
        p=ROOT/name
        if p.suffix.lower() in {'.md','.json','.txt','.html','.css','.js','.py','.yml','.yaml'} and not p.name.startswith('audit_'):
            assert not bad.search(p.read_text(encoding='utf-8')),name
        assert p.suffix.lower() not in {'.ppt','.pptx','.zip','.log'},name
        if p.suffix.lower() in {'.jpg','.png'}:
            with Image.open(p) as im:
                assert not im.getexif(),name
                assert not any(k.lower() in {'author','artist','comment','description','xmp','xml:com.adobe.xmp'} for k in im.info),name
    identities=set(git('log','--format=%an <%ae>|%cn <%ce>').splitlines())
    assert identities=={'Artwork Archive <archive@example.invalid>|Artwork Archive <archive@example.invalid>'}
    result={'status':'passed','original_sources_unchanged':48,'reviewed':20,'adjusted':5,'retained':15,'checkpoint_hashes':'verified','current_hashes_dimensions':'verified','aquatic_shared_scene_and_title_preservation':'verified','descriptive_image_metadata':'absent','public_identity_scan':'passed'}
    print(json.dumps(result));return result
if __name__=='__main__':audit()
