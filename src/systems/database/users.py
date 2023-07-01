import shelve


class User:
    def __init__(self, name):
        self.name = name
        self.scores = {
            'maths': {
                'marks': 0,
                'questions': 0
            }
        }

    def correct_answer(self, subject):
        self.scores[subject]['marks'] += 1
        self.scores[subject]['questions'] += 1
        return 'That is the right answer!'

    def wrong_answer(self, subject, answer):
        self.scores[subject]['questions'] += 1
        return f'That is the wrong answer. The correct answer is {answer}'

    def update_user(self, subject):
        with shelve.open('save_file', flag='c') as f:
            data = f[self.name]
            data[subject]['total marks'] += self.scores[subject]['marks']
            data[subject]['total questions'] += self.scores[subject]['questions']
            f[self.name] = data



def create_user(new_user):
    with shelve.open('save_file', flag='c') as f:
        if new_user not in get_users_names():
            f[new_user] = {
                'maths': {
                    'total marks': 0,
                    'total questions': 0
                }
            }

def get_users_names():
    with shelve.open('save_file', flag='c') as f:
        return list(f.keys())