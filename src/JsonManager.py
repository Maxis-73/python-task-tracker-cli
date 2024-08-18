import json
import os

def read_json():
    if not os.path.isfile('src/data.json'):
        with open('src/data.json', 'w') as f:
            json.dump([], f)
    with open('src/data.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data):
    with open('src/data.json', 'w') as f:
        json.dump(data, f)