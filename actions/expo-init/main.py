import os, sys

name = sys.argv[1]
TEMP_PATH = sys.argv[2]

if __name__ == '__main__':
    os.chdir(TEMP_PATH)
    os.system('expo init . --name {} --no-install --yes'.format(name))
