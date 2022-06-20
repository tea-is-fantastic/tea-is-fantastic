import os
from distutils.dir_util import copy_tree

TEMP_PATH = os.environ['TEMP_PATH']
OUTPUT_PATH = os.environ['OUTPUT_PATH']

copy_tree(TEMP_PATH, OUTPUT_PATH)
