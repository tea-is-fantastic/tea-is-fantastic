import os
import yaml
import subprocess
from tif_yaml import open_yaml
from tif_format import TeaFormatter

DATA_PATH = os.environ['DATA_PATH']
APP_PATH = os.environ['APP_PATH']

tea_format = TeaFormatter()


def process_step(elem):
    action = elem["action"]
    try:
        args = elem["args"]
    except:
        args = []
    if action is not None:
        script_loc = "{}/actions/{}/main.py".format(APP_PATH, action)
        subprocess.call(["python", script_loc, *args])


def process_template(tempstr):
    raw_template = open_yaml("{}/templates/{}/main.yaml".format(APP_PATH, tempstr))
    template = tea_format.format(raw_template)
    pre = template["pre"] or []
    run = template["run"] or []
    post = template["post"] or []

    for x in pre:
        process_step(x)
    for x in run:
        process_step(x)
    for x in post:
        process_step(x)

