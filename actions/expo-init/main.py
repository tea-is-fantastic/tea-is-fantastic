import os, sys, subprocess

name = sys.argv[1]
TEMP_PATH = sys.argv[2]

if __name__ == '__main__':
    os.chdir(TEMP_PATH)
    os.system('expo init {} --no-install --yes'.format(name))
