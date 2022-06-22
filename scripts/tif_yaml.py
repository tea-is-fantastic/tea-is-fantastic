import os
import yaml

DATA_PATH = os.environ['DATA_PATH']


def open_yaml(yaml_loc):
    with open(yaml_loc, "r") as stream:
        return yaml.safe_load(stream)


app_yaml = open_yaml(f"{DATA_PATH}/app.yaml")
assets_yaml = open_yaml(f"{DATA_PATH}/assets.yaml")


def open_raw(yaml_loc):
    with open(yaml_loc, "r") as stream:
        return stream.read()


def yaml_dict(stream):
    return yaml.safe_load(stream)


def name_to_yaml(name):
    if name == "assets":
        return assets_yaml
    else:
        return app_yaml


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


def yaml_extract(name, varname):
    keys = varname.split('.')
    test_yaml = name_to_yaml(name)
    return nested_get(test_yaml, keys)
