import json

def load_config(filename):
    f=open(filename)
    return json.load(f)


