import os, shutil

TEMP_PATH = os.environ['TEMP_PATH']
OUTPUT_PATH = os.environ['OUTPUT_PATH']

if __name__ == '__main__':
    shutil.move(TEMP_PATH, OUTPUT_PATH)
    os.mkdir(TEMP_PATH)
