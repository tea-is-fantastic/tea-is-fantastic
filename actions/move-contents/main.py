import os, shutil

SRC_PATH = sys.argv[1]
DEST_PATH = sys.argv[2]

if __name__ == '__main__':
    shutil.rmtree(DEST_PATH)
    os.makedirs(DEST_PATH)
    shutil.move(SRC_PATH, DEST_PATH, copy_function=shutil.copy_tree)
