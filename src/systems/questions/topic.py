from src.run_game import current_subject
from random import choice
from src.systems.questions.maths import MathsQuiz
from src.systems.questions.english import SpellingQuiz


class Subject:
    def __init__(self, name, problems):
        self.name = name
    
def set_current_subject(value, subject):
    current_subject[0] = subject

class Quiz:
    def __init__(self):
        self.quiz = choice[MathsQuiz(), SpellingQuiz()]
