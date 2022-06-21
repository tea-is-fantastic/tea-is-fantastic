import os, shutil, sys

SRC_PATH = sys.argv[1]
DEST_PATH = sys.argv[2]

if __name__ == '__main__':
    shutil.move(SRC_PATH, DEST_PATH)
