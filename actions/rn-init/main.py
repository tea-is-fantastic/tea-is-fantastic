import os

# args: name

OUTPUT_PATH = os.environ['OUTPUT_PATH']
name = sys.argv[1]

os.chdir(OUTPUT_PATH)
os.system('expo init . --name {} --no-install --yes'.format(name))