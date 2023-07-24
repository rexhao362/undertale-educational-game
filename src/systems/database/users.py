import json

class User:
    def __init__(self, name):
        self.name = name
        self.scores = {
            'maths': {
                'correct': 0,
                'wrong': 0
            }
        }

    def correct_answer(self, subject):
        self.scores[subject]['correct'] += 1
        return 'That is the right answer!'

    def wrong_answer(self, subject, answer):
        self.scores[subject]['wrong'] += 1
        return f'That is the wrong answer. The correct answer is {answer}'

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
                'english': {
                    'total correct': 0,
                    'total wrong': 0
                }
            }
        json.dump(data, f)


def get_users_names():
    with open('save_file.json', 'r') as f:
        return list(json.load(f).keys())