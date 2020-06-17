#!/pkg/python/3.6.8/bin/python3.6
from pathlib import Path
import os
from time import strftime

def export(images, names, location, sample_name=None):
    outdir = location
    if type(outdir) is not Path:
        outdir = Path(outdir)
    if not outdir.exists():
        raise ValueError(f'Output directory {str(location)} does not exist')
    sample_id = sample_name if sample_name else strftime('%Y-%m-%d_%H:%M:%S%z')
    sample_dir = outdir / sample_id
    os.mkdir(str(sample_dir))
    os.mkdir(str(sample_dir / 'TNG.in'))
    os.mkdir(str(sample_dir / 'TNG.tmp'))
    os.mkdir(str(sample_dir / 'TNG.out'))
    for I,name in zip(images,names):
        pass 
    