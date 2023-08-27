from src.run_game import current_subject
from random import choice
import pygame


class Subject:
    def __init__(self, name, problems):
        self.name = name
        self.guesses = 0
    
def set_current_subject(value, subject):
    current_subject[0] = subject

