import pygame

class Quiz:
    def __init__(self, subject):
        self.subject = subject
        self.guesses = 0
        self.answer = None

    def draw_crosses(self):
        for i in range(self.guesses):
            cross = Crosses(50 + i * 30)
            self.guesses += 1

    def correct_answer(self):
        self.scores[self.subject]['correct'] += 1
        return 'That is the right answer!'

    def wrong_answer(self):
        self.draw_crosses()
        if self.guesses == 3:
            self.scores[self.subject]['wrong'] += 1
            return f'That is the wrong answer. The correct answer is {self.answer}'


class Crosses:
    def __init__(self, left):
        self.left_pos = left
        self.top_pos = 56
        self.image = pygame.image.load('assets/pictures/x.png').convert_alpha()
        self.rect = self.image.get_rect()
        