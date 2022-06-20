import os
from distutils.dir_util import copy_tree

TEMP_PATH = os.environ['TEMP_PATH']
OUTPUT_PATH = os.environ['OUTPUT_PATH']

if __name__ == '__main__':
    os.rename(TEMP_PATH, OUTPUT_PATH)
    os.mkdir(TEMP_PATH)
