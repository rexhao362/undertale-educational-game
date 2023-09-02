import pygame
from src.systems.state import State


class Quiz(State):
    def __init__(self, state_manager, subject):
        self.sm = state_manager
        self.user = self.sm.user
        self.subject = subject
        self.chances = 0
        self.max_chances = 3
        self.answer = None

    def draw_crosses(self, screen):
        cross = pygame.image.load('assets/pictures/x.png').convert_alpha()
        image_rect = cross.get_rect()
        image_width = image_rect.width
        pos_x = 100
        pos_y = 100
        spacing = 10
        for i in range(self.chances):
            screen.blit(cross, (pos_x, pos_y))
            pos_x += image_width + spacing

    def correct_answer(self):
        self.user.correct_answer(self.subject)
        text = f'Correct! {self.answer} is the right answer!'
        self.sm.set_success(True)  # TODO
        self.sm.back_state()

    def wrong_answer(self):
        # font = pygame.font.Font()
        text = ''
        self.chances += 1
        if self.chances > 0 and self.chances < self.max_chances:
            text = 'That was wrong. Try again'
        elif self.chances == self.max_chances:
            self.user.wrong_answer(self.subject)
            text = f'That is the wrong answer. The correct answer is {self.answer}'
            self.sm.set_success(False)
            self.sm.back_state()
