import os
from string import Formatter
from tif_yaml import process_yaml

class TeaFormatter(Formatter):
    def __init__(self):
        Formatter.__init__(self)

    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            try:
                return kwds[key]
            except KeyError:
                y = key.split("|")
                if y[0] == "yaml":
                    return process_yaml(y[1], y[2])
                elif y[0] == "env":
                    return os.environ[y[1]]
        else:
            Formatter.get_value(key, args, kwds)

tea_format = TeaFormatter()