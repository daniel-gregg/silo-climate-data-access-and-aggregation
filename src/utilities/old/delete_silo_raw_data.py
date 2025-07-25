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

def delete_silo_raw_data(var, year):
    
    file = os.path.join(here(f'data/silo/{var}/{year}'))
    print(f'removing {file} from /data')
    os.remove(file)