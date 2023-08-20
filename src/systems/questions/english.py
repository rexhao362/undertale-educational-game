from json import load
import random
import pygame

word_list = []
with open('src/systems/questions/word_list.json') as f:
    word_list = load(f)['word_list']


class GuessWordGame:
    def __init__(self, screen):
        self.screen = screen
        self.word = [random.choice(word_list)]
        self.masked_word = self.word
        # self.background
        self.letters_indices = {}
        self.guesses = 0

    def mask_word(self):
        length = len(self.word)
        if length < 5:
            times = 1
        elif length < 8:
            times = 2
        else:
            times = 3

        while times > 0:
            index = random.randint(0, length-1)
            if self.masked_word[index] != '' or not ' ':
                self.letters_indices[index] = self.masked_word[index]
                self.masked_word[index] = ''
                times -= 1

    def unmask(self, index):
        self.masked_word[index] = self.word[index]

    def check_answer(self):
        pass

    def draw_guessing(self):
        num_boxes = len(self.masked_word)
        
        



    def draw_crosses(self):
        pass


class LetterBoxes:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont('chalkduster.ttf', 36)
        self.box_height = 50
        self.box_spacing = 20


class Crosses:
    def __init__(self, x):
        self.x_pos = x
        self.font = pygame.font.Font('', 54)