import os, sys

name = sys.argv[1]
TEMP_PATH = sys.argv[2]

if __name__ == '__main__':
    os.chdir(TEMP_PATH)
    os.system(f'npx react-native init {name} --template react-native-template-typescript --no-install --quiet')
