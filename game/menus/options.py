import pygame_menu
from game.settings import settings


options_menu = pygame_menu.Menu('Options', settings.screen_width,
                                settings.screen_height, theme=pygame_menu.themes.THEME_DARK)

# TODO Add options here 

# Create a horizontal frame at the bottom of the screen
options_menu.bottom_frame = options_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    # vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    # horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
    border_width=0
)

# Add two buttons to the frame
options_menu.bottom_frame.pack(options_menu.add.button(
    'Back', pygame_menu.events.BACK))
options_menu.bottom_frame.pack(options_menu.add.button(
    'Exit', pygame_menu.events.EXIT))
