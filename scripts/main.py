from tif_util import process_template, process_yaml

if __name__ == '__main__':
    template = process_yaml('app', 'template')
    print("template")
    print(template)
    process_template(template)
