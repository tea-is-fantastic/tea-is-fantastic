import os, shutil, sys

SRC_PATH = sys.argv[1]
DEST_PATH = sys.argv[2]

if __name__ == '__main__':
    if (os.path.isdir(DEST_PATH)):
        shutil.rmtree(DEST_PATH)
    shutil.move(SRC_PATH, DEST_PATH)
