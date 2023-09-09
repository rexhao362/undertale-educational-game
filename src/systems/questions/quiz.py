import pygame
import pygame_gui
from src.systems.state import State


class Quiz(State):
    def __init__(self, state_manager, subject):
        self.sm = state_manager
        self.user = self.sm.user
        self.subject = subject
        self.chances = 0
        self.max_chances = 3
        self.answer = None
        self.message = None

    def draw_crosses(self, screen):
        cross = pygame.image.load('assets/pictures/x.png').convert_alpha()
        image_rect = cross.get_rect()
        image_width = image_rect.width
        pos_x = 200
        pos_y = 600
        spacing = 10
        for i in range(self.chances):
            screen.blit(cross, (pos_x, pos_y))
            pos_x += image_width + spacing

    def correct_answer(self):
        self.user.correct_answer(self.subject)
        self.message = f'Correct! {self.answer} is the right answer!'
        self.sm.set_success(True)
        self.create_text_box()

    def wrong_answer(self):
        self.chances += 1
        if self.chances > 0 and self.chances < self.max_chances:
            pass
        elif self.chances == self.max_chances:
            self.user.wrong_answer(self.subject)
            self.message = f"""That is the wrong answer.
                    The correct answer is {self.answer}"""
            self.sm.set_success(False)
            self.create_text_box()


    def create_text_box(self):
        self.text_box = pygame_gui.elements.ui_text_box.UITextBox(
            html_text=self.message,
            relative_rect=pygame.Rect(230, 400, 400, 75))

def create_start_box():
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((800, 600), (100, 50)),
        text='GO')
