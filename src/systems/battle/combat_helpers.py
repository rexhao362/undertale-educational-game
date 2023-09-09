import src.settings as s
import pygame
import pygame_gui


def create_buttons(buttons_list, spacing=0, object_id=False):
    # Constants
    RECT_WIDTH = 100
    RECT_HEIGHT = 50
    RECT_DISTANCE = 50

    num_buttons = len(buttons_list)
    # Calculate the x-coordinate for the first rectangle
    total_rect_width = num_buttons * RECT_WIDTH + \
        (num_buttons-1) * RECT_DISTANCE
    left = (s.screen_values[0] - total_rect_width) // 2
    top = (2 * s.screen_values[1]) // 3 + spacing

    buttons_dict = {}
    # Draw the four rectangles
    for button in buttons_list:
        rect = pygame.Rect((left, top), (RECT_WIDTH, RECT_HEIGHT))

        buttons_dict[button] = pygame_gui.elements.UIButton(
            relative_rect=rect,
            text=button)

        left += RECT_WIDTH + RECT_DISTANCE

    return buttons_dict


def disable_hide_buttons(buttons):
    for button in buttons.values():
        button.disable()
        button.hide()


def enable_show_buttons(buttons):
    for button in buttons.values():
        button.enable()
        button.show()


def songs(stage):
    songs = {
        1: 'Battle/Battle Mage',
        2: 'Battle/Battle with Beasts',
        3: 'Battle/I\'ve Got Your Back! (Full)',
        4: 'Battle/If It\'s a Fight You Want',
        5: 'Battle/It\'s Bossing Time'
    }
    return songs[stage]
