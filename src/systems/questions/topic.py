from src.run_game import current_subject
from random import choice
import pygame


class Subject:
    def __init__(self, name, problems):
        self.name = name
        self.guesses = 0
    
def set_current_subject(value, subject):
    current_subject[0] = subject

class Quiz:
    def __init__(self, screen, subject):
        self.screen = screen
        self.subject = subject
        self.guesses = 0

    def draw_crosses(self):
        for i in range(self.guesses):
            cross = Crosses(50 + i * 30)

            self.guesses += 1

class Crosses:
    def __init__(self, left):
        self.left_pos = left
        self.top_pos = 56
        self.image = pygame.image.load('assets/pictures/x.png').convert_alpha()
        self.image_rect = self.image.get_rect()
        