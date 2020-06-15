 # importing a specific module 
from collections import defaultdict, namedtuple
import multiprocessing as mp  # renaming the module
from csv import reader as csvreader
from random import *    # will import every object from a module { Not advidsable}

#Dealing with sub modules 
# [ import package_name.submodule_name ]
import os.path 
#import os.path.isdir # [Wrong ] You cannot import a function from a sub module 

from datetime import datetime


os.path.isdir('my_path')
#collections.defaultdict() # this will give an error 
defaultdict() # we do not need the dot notation 
print(mp.cpu_count())
