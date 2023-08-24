from src.run_game import current_subject
from random import choice
from systems.questions.maths.maths_questions import MathsQuiz
from systems.questions.spelling.english import SpellingQuiz


class Subject:
    def __init__(self, name, problems):
        self.name = name
    
def set_current_subject(value, subject):
    current_subject[0] = subject

class Quiz:
    def __init__(self):
        self.quiz = choice[MathsQuiz(), SpellingQuiz()]
