import os
import yaml
import subprocess

DATA_PATH = os.environ['DATA_PATH']
APP_PATH = os.environ['APP_PATH']


def nested_get(dic, keys):    
    for key in keys:
        dic = dic[key]
    return dic


def process_yaml(name, varname):
    keys = varname.split('.')
    test_yaml = yaml.safe_load("{}/{}.yaml".format(DATA_PATH, name))
    return nested_get(test_yaml, keys)


def process_args(args):
    output = List()
    for x in args:
        y = x.split("|")
        if y[0] is "yaml":
            output.append(process_yaml(y[1], y[2]))
        elif y[0] is "env":
            output.append(os.environ[y[1]])
    return output


def process_action(name, args):
    script_loc = "{}/actions/{}.py".format(APP_PATH, name)
    final_args = process_args(args)
    subprocess.call([script_loc, *final_args])


def process_step(elem):
        step = elem["type"].split("|")
        if step[0] is "action":
            process_action(step[1], elem["args"])


def process_template(template):
    pre = template["pre"]
    run = template["run"]
    post = template["post"]

    for x in pre:
        process_step(x)
    for x in run:
        process_step(x)
    for x in post:
        process_step(x)

