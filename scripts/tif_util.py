import os
import yaml
import subprocess

DATA_PATH = os.environ['DATA_PATH']
APP_PATH = os.environ['APP_PATH']


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


def open_yaml(yaml_loc):
    with open(yaml_loc, "r") as stream:
        return yaml.safe_load(stream)


def process_yaml(name, varname):
    keys = varname.split('.')
    test_yaml = open_yaml("{}/{}.yaml".format(DATA_PATH, name))
    return nested_get(test_yaml, keys)


def process_args(args):
    output = []
    for x in args:
        y = x.split("|")
        if y[0] == "yaml":
            output.append(process_yaml(y[1], y[2]))
        elif y[0] == "env":
            output.append(os.environ[y[1]])
    return output


def process_action(name, args):
    script_loc = "{}/actions/{}/main.py".format(APP_PATH, name)
    final_args = process_args(args)
    subprocess.call(["python", script_loc, *final_args])


def process_step(elem):
        step = elem["type"].split("|")
        try:
            args = elem["args"]
        except Error as e:
            args = []
        if step[0] == "action":
            process_action(step[1], args)


def process_template(tempstr):
    template = open_yaml("{}/templates/{}/main.yaml".format(APP_PATH, tempstr))
    pre = template["pre"] or []
    run = template["run"] or []
    post = template["post"] or []

    for x in pre:
        process_step(x)
    for x in run:
        process_step(x)
    for x in post:
        process_step(x)

