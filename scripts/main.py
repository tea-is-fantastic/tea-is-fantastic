from tif_util import process_template
from tif_yaml import yaml_extract

if __name__ == '__main__':
    template = yaml_extract('app', 'template')
    process_template(template)
