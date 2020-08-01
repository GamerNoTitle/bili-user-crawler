import json as js
def read_config():
    with open("config.json") as json_file:
        config = js.load(json_file)
    return config