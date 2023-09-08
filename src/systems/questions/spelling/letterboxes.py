import pygame
import pygame_gui
import src.settings as s


class LetterBoxes:
    def __init__(self, word):
        self.word = word
        self.num_boxes = len(self.word)
        self.font = pygame.font.Font('data/fonts/league_spartan.ttf', 28)
        self.font_colour = 'white'
        self.box_size = 50
        self.box_height = 50
        self.box_spacing = 20
        self.input_boxes = {}
        self.redraw = True

    def draw_boxes(self, screen):
        (screen_width, screen_height) = s.screen_values
        box_x = (screen_width - (self.num_boxes *
                 (self.box_size + self.box_spacing))) // 2
        box_y = (screen_height - self.box_height) // 2

        for i, letter in enumerate(self.word):
            if letter == '':
                if self.redraw == True:
                    box_vars = box_x, box_y, self.box_size, self.box_height
                    self.input_boxes[i] = create_input_box(*box_vars
                                                           )
            else:
                box_rect = pygame.Rect(
                    box_x, box_y, self.box_size, self.box_height)
                char_surface = self.font.render(letter, True, self.font_colour)
                char_rect = char_surface.get_rect(center=box_rect.center)
                screen.blit(char_surface, char_rect.topleft)

            box_x += self.box_size + self.box_spacing

        self.redraw = False

    def delete_input_box(self, index):
        del self.input_boxes[index]


def mask_num(word):
    length = len(word)
    if length < 5:
        return 1
    elif length < 8:
        return 2
    else:
        return 3


def create_input_box(box_x, box_y, box_size, box_height):
    input_box = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect(
            box_x, box_y, box_size, box_height),
        placeholder_text='*')
    input_box.set_text_length_limit(1)
    input_box.set_allowed_characters('letters')
    return input_box
