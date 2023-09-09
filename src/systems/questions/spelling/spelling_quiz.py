from json import load
from random import choice, randint
import pygame
import pygame_gui
from src.systems.questions.quiz import Quiz, create_start_box
from src.systems.questions.spelling.letterboxes import LetterBoxes, mask_num


word_list = []
with open('data/word_list.json') as f:
    word_list = load(f)['word_list']


class SpellingQuiz(Quiz):
    def __init__(self, state_manager):
        super().__init__(state_manager, 'spelling')
        self.word = [*choice(word_list)]
        self.masked_word = mask_word(self.word)
        self.answer = ''.join(self.word)
        self.solution = {}
        self.letters = LetterBoxes(self.masked_word)
        self.ui_button = create_start_box()

    def check_solution(self):
        for index, letter in self.solution.items():
            if letter is not None:
                if letter == self.word[index]:
                    self.masked_word[index] = self.word[index]
                    self.letters.delete_input_box(index)
                    self.solution[index] = None
                else:
                    self.wrong_answer()
        self.letters.redraw = True
        if self.word == self.masked_word:
            self.correct_answer()

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.message is not None:
                    self.sm.reload_state()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.message is not None:
                        self.sm.reload_state()
                    else:
                        manager.clear_and_reset()
                        self.check_solution()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                for index, text_box in self.letters.input_boxes.items():
                    if event.ui_element == text_box:
                        self.solution[index] = event.text

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                manager.clear_and_reset()
                self.check_solution()

            manager.process_events(event)

    def update(self):
        pass

    def draw(self, screen, time_delta):
        screen.fill('black')
        text = 'Guess the Missing Letters'
        font = pygame.font.Font('data/fonts/league_spartan.ttf', 24)
        question = font.render(text, True, 'white')
        screen.blit(question, (200, 100))
        self.letters.draw_boxes(screen)
        self.draw_crosses(screen)

    def delete_solution(self, index):
        del self.solution[index]

    


def mask_word(word):
    num_masks = mask_num(word)
    masked_word = word.copy()
    while num_masks > 0:
        index = randint(0, len(word)-1)
        if masked_word[index] != '' or not ' ':
            masked_word[index] = ''
            num_masks -= 1
    return masked_word
