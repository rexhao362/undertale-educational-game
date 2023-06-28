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

    def wrong_answer(self, subject):
        self.scores[subject]['questions'] += 1

    def update_user(self):
        pass

def get_users():
    pass
