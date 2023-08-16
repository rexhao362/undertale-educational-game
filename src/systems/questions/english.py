from json import load
import random
import pygame

word_list = []
with open('src/systems/questions/word_list.json') as f:
    word_list = load(f)['word_list']


class GuessWordGame:
    def __init__(self):
        self.word = [*random.choice(word_list)]
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
            if self.masked_word[index] != '*' or not ' ':
                self.letters_indices[index] = self.masked_word[index]
                self.masked_word[index] = '*'
                times -= 1

    def unmask(self, index):
        self.masked_word[index] = self.word[index]

    def check_answer(self):
        pass

    def draw_guessing(self):
        num_boxes = len(self.masked_word)
        font = pygame.font.SysFont('chalkduster.ttf', 72)
        word_image = []
        index = -1
        for char in self.masked_word:
            index += 1
            image = font.render(char, True, WHITE)
            rect = image.get_rect()
            if char != '*':
                word_image.push(image)
            else:
                rect = image.get_rect()
                word_image.push(char)
        



    def draw_crosses(self):
        pass
