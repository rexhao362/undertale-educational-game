from json import load
import random
import pygame
import pygame_gui
from src.systems.questions.quiz import Quiz
from src.systems.questions.spelling.letterboxes import LetterBoxes, mask_num


word_list = []
with open('data/word_list.json') as f:
    word_list = load(f)['word_list']


class SpellingQuiz(Quiz):
    def __init__(self):
        super().__init__(subject='spelling')
        self.word = [random.choice(word_list)]
        self.masked_word = mask_word(self.word)
        self.solution = {}
        self.letters = None

    def check_solution(self):
        for index, letter in self.solution.items():
            if letter == self.word[index]:
                self.masked_word[index] = self.word[index]
        if self.word == self.masked_word:
            pass

    def events(self, manager):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code("return"):
                    self.check_solution()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                for index, letter in self.letters.input_boxes.items():
                    if event.ui_element == letter:
                        self.solution[index] = event.text

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == start_button:
                self.check_solution()

            manager.process_events(event)

    def update(self):
        pass

    def draw(self, screen):
        text = 'Guess the Missing Letters'
        font = pygame.font.SysFont('data/fonts/league_spartan.ttf', 24)
        question = font.render(text, True, 'white')
        screen.blit(question)
        self.letters = LetterBoxes(self.masked_word)
        self.letters.draw_boxes(screen)



def mask_word(word):
    num_masks = mask_num(word)
    masked_word = word
    while num_masks > 0:
        index = random.randint(0, len(word)-1)
        if masked_word[index] != '' or not ' ':
            masked_word[index] = ''
            num_masks -= 1
    return masked_word



if __name__ == 'main':
    # pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    running = True
    state = SpellingQuiz()
    while running:
        state.events()
        state.draw(screen)

        pygame.display.flip()

    pygame.quit()