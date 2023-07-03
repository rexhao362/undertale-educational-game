import json


with open('save_file.json', 'w') as f:
    data = {'player': {
        'total correct': 0,
        'total wrong': 0
        }
    }
    json.dump(data, f)
