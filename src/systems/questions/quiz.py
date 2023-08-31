import pygame
from src.systems.state import State

class Quiz(State):
    def __init__(self, user, subject):
        self.user = user
        self.subject = subject
        self.guesses = 0
        self.answer = None

    def draw_crosses(self, screen):
        for i in range(self.guesses):
            cross = Crosses(50 + i * 30)
            screen.blit(cross.image, cross.rect)
            self.guesses += 1

    def correct_answer(self):
        self.user.score[self.subject]['correct'] += 1
        return 'That is the right answer!'

    def wrong_answer(self):
        self.draw_crosses()
        if self.guesses == 3:
            self.user.score[self.subject]['wrong'] += 1
            return f'That is the wrong answer. The correct answer is {self.answer}'


class Crosses:
    def __init__(self, left):
        self.left_pos = left
        self.top_pos = 56
        self.image = pygame.image.load('assets/pictures/x.png').convert_alpha()
        self.rect = self.image.get_rect()
        