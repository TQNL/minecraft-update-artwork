"""Rebuild the five quality adjustments from the public checkpoint PNGs.

Usage: python tools/rebuild_f_quality.py OUTPUT_DIRECTORY
Requires numpy, Pillow and opencv-python. Does not overwrite archive files.
"""
from pathlib import Path
import json,sys
import numpy as np
from PIL import Image
from quality_adjustments import apply
ROOT=Path(__file__).resolve().parents[1]
def rebuild(destination):
    destination=Path(destination).resolve()
    if destination==ROOT or ROOT in destination.parents:
        raise ValueError('Use an output directory outside the archive checkout.')
    destination.mkdir(parents=True,exist_ok=True)
    report=json.loads((ROOT/'reconstruction/quality-review/final.json').read_text())
    before={r['id']:np.array(Image.open(ROOT/r['before_file']).convert('RGB')) for r in report['assets'] if r['changed']}
    after={}
    for row in report['assets']:
        if not row['changed']:continue
        aid=row['id'];out=apply(before[aid],aid)
        if aid=='R40B':
            mask=np.any(before['R40A']!=before['R40B'],axis=2)
            out=after['R40A'].copy();out[mask]=before['R40B'][mask]
        after[aid]=out
        expected=np.array(Image.open(ROOT/row['after_file']).convert('RGB'))
        if not np.array_equal(out,expected):raise AssertionError(aid+' pixels differ from published result')
        Image.fromarray(out).save(destination/(aid+'.png'))
    print(json.dumps({'rebuilt':len(after),'pixels_match_published':True}))
if __name__=='__main__':rebuild(sys.argv[1])
