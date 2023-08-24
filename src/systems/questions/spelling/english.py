from json import load
import random
import pygame
import pygame_gui
from src.manager import manager
from src.systems.questions.topic import Quiz

word_list = []
with open('data/word_list.json') as f:
    word_list = load(f)['word_list']


class SpellingQuiz(Quiz):
    def __init__(self):
        super().__init__(subject='spelling')
        self.word = [random.choice(word_list)]
        self.masked_word = self.word
        self.letters_indices = {}

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

    def draw_cross(self):
        pass

    def events(self):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code("return"):
                    self.mark()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == num_box:
                    self.guess = event.text

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    self.mark()

            manager.process_events(event)
    
    def update_score(self, user):
        pass


class LetterBoxes:
    def __init__(self, word):
        self.word = word
        self.font = pygame.font.SysFont('chalkduster.ttf', 36)
        self.height = 50
        self.spacing = 20
        # self.width =



