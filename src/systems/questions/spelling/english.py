from json import load
import random
import pygame
import pygame_gui
import src.manager as man
from src.systems.questions.quiz import Quiz


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

    def events(self):
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

            # elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == start_button:
            #         self.check_solution()

            man.manager.process_events(event)

    def update(self):
        pass

    def draw(self, screen):
        self.letters = LetterBoxes(self.masked_word)
        self.letters.draw_boxes(screen)


class LetterBoxes:
    def __init__(self, word):
        self.word = word
        self.num_boxes = len(self.word)
        self.font = pygame.font.SysFont('data/fonts/league_spartan.ttf', 24)
        self.font_colour = 'black'
        self.box_size = 50
        self.box_height = 50
        self.box_spacing = 20
        self.input_boxes = {}
        # self.active_box = 0
        # self.active_box_colour
        # self.input_box_colour
        # self.outline_colour

    def draw_boxes(self, screen):
        (screen_width, screen_height) = screen.get_window_size()
        box_x = (screen_width - (self.num_boxes *
                 (self.box_size + self.box_spacing))) // 2
        box_y = (screen_height - self.box_height) // 2

        for i, letter in enumerate(self.word):
            if letter == '':
                self.input_boxes[i] = create_input_box(
                    box_x, box_y, self.box_size, self.box_height)
                # box_colour = self.active_box_colour if i == self.active_box else self.input_box_colour
                # pygame.draw.rect(screen, box_colour, box_rect)
                # pygame.draw.rect(screen, self.outline_colour, box_rect, 2)
                # letter_surface = self.font.render(
                #     letter, True, self.font_colour)
                # letter_rect = letter_surface.get_rect(center=box_rect.center)
                # screen.blit(letter_surface, letter_rect.topleft)
            else:
                box_rect = pygame.Rect(
                    box_x, box_y, self.box_size, self.box_height)
                char_surface = self.font.render(letter, True, self.font_colour)
                char_rect = char_surface.get_rect(center=box_rect.center)
                screen.blit(char_surface, char_rect.topleft)

            box_x += self.box_size + self.box_spacing


def mask_num(word):
    length = len(word)
    if length < 5:
        return 1
    elif length < 8:
        return 2
    else:
        return 3


def mask_word(word):
    num_masks = mask_num(word)
    masked_word = word
    while num_masks > 0:
        index = random.randint(0, len(word)-1)
        if masked_word[index] != '' or not ' ':
            masked_word[index] = ''
            num_masks -= 1
    return masked_word


def create_input_box(box_x, box_y, box_size, box_height):
    input_box = pygame_gui.elements.UITextEntryBox(relative_rect=(
        box_x, box_y, box_size, box_height), placeholder_text='*')
    input_box.set_text_length_limit(1)
    input_box.set_forbidden_characters('numbers')
    return input_box


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
