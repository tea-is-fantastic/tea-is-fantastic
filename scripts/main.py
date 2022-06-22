from tif_util import process_template
from tif_yaml import process_yaml

if __name__ == '__main__':
    template = process_yaml('app', 'template')
    process_template(template)
