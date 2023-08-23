import random
from operator import add, sub, mul, truediv
import pygame

def create_maths_question():
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)
    max_num = max([num_1, num_2])
    min_num = min([num_1, num_2])
    operators = [add, sub, mul, truediv] if max_num % min_num == 0 else [
        add, sub, mul]
    op = random.choice(operators)

    i = operators.index(op)
    symbols = ['+', '-', 'x', '/']
    text = f"What is {max_num} {symbols[i]} {min_num}?"
    answer = op(max_num, min_num)

    return {
        'text': text,
        'answer': answer 
    }


def create_fraction_question():
    fractions = {
        1/2: 0.5,
        '1/4': 0.25,
        '1/3': 0.33,
        '3/4': 0.75,
        '1/8': 0.125,
        '3/8': 0.375,
        '3/8': 0.375,
        '5/8': 0.375
    }


def create_rounding_question():
    num = random.randint(1, 100)/10
    text = f'What is {num} rounded to the nearest integer?'
    answer = round(num)

    return {
        'text': text,
        'answer': answer 
    }


def choose_maths_question():
    questions_list = [
        create_maths_question,
        create_fraction_question,
        create_rounding_question
    ]

    chosen_question = random.choice(questions_list)

    return chosen_question()

class MathsQuiz:
    def __init__(self) -> None:
        self.quiz = choose_maths_question()
        self.text = self.quiz['text']
        self.answer = self.quiz['answer']

    def events(self):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                # self.running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                pass

    def draw(self):
        font = pygame.font.SysFont('chalkduster.ttf', 24)
        image = font.render(self.text)
