import json
import os


filename = 'save_file.json'
if filename not in os.listdir():
    with open(filename, 'w') as f:
        data = {
            'player': {
                'maths': {
                    'total correct': 0,
                    'total wrong': 0
                },
                'spelling': {
                    'total correct': 0,
                    'total wrong': 0
                }
            }
        }
        json.dump(data, f)
