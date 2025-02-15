#core modules/packages
import sys
import os
from pyprojroot.here import here
from pathlib import Path
import glob

## Setting things up
#append path using 'here'
path_root = here()
sys.path.append(str(path_root))

def delete_silo_raw_data(var):
    ## delete target silo data var
    dirpath = os.path.join(here(f'data/silo/{var}/'))
    years = os.listdir(dirpath)
    for year in years:
        file = os.path.joing(here(f'data/silo/{var}/{year}.nc'))
        print(f'removing {file} from /data')
        os.remove(file)