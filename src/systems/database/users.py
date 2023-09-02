import json


class User:
    def __init__(self, name):
        self.name = name
        self.score = {
            'maths': {
                'correct': 0,
                'wrong': 0
            },
            'spelling': {
                'correct': 0,
                'wrong': 0
            }
        }

    def correct_answer(self, subject):
        self.score[subject]['correct'] += 1

    def wrong_answer(self, subject):
        self.score[subject]['wrong'] += 1

    def update_user(self):
        with open('save_file.json', 'r+') as f:
            data = json.load(f)
            user_data = data[self.name]
            for subject in user_data.keys():
                subject_data = user_data[subject]
                subject_data['total correct'] += self.scores[subject]['correct']
                subject_data['total wrong'] += self.scores[subject]['wrong']
                self.scores[subject]['correct'] = 0
                self.scores[subject]['wrong'] = 0
            json.dump(data, f)


def create_user(new_user):
    with open('save_file.json', 'r+', encoding='utf8') as f:
        data = json.load(f)
        if new_user not in get_users_names():
            data[new_user] = {
                'maths': {
                    'total correct': 0,
                    'total wrong': 0
                },
                'spelling': {
                    'total correct': 0,
                    'total wrong': 0
                }
            }
        json.dump(data, f)


def get_users_names():
    with open('save_file.json', 'r') as f:
        return list(json.load(f).keys())
