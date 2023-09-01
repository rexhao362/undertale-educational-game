import pygame
from src.systems.state import State

class Quiz(State):
    def __init__(self, state_manager, user, subject):
        self.sm = state_manager
        self.user = user
        self.subject = subject
        self.chances = 0
        self.answer = None

    def draw_crosses(self, screen):
        for i in range(self.chances):
            cross = Crosses(50 + i * 30)
            screen.blit(cross.image, cross.rect)

    def correct_answer(self):
        self.user.score[self.subject]['correct'] += 1
        text = f'Correct! {self.answer} is the right answer!'
        self.sm.set_success(True)#TODO
        self.sm.back_state()

    def wrong_answer(self):
        # font = pygame.font.Font()
        text = ''
        self.chances += 1
        if self.chances > 0 and self.chances < 3:
            text = 'That was wrong. Try again'
        elif self.chances == 3:
            self.user.score[self.subject]['wrong'] += 1
            text =  f'That is the wrong answer. The correct answer is {self.answer}'
            self.sm.set_success(False)
            self.sm.back_state()


class Crosses:
    def __init__(self, left):
        self.left_pos = left
        self.top_pos = 56
        self.image = pygame.image.load('assets/pictures/x.png').convert_alpha()
        self.rect = self.image.get_rect()
        