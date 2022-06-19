import os

# args: name

TEMP_PATH = os.environ['TEMP_PATH']
DATA_PATH = os.environ['DATA_PATH']
OUTPUT_PATH = os.environ['OUTPUT_PATH']

os.system('expo init {} --name {} --no-install --yes'.format(OUTPUT_PATH, name))
