# from src.menus.menu_class import Menu
from src.run_game import start_game
from src.systems.questions.topic import set_subject
import pygame_menu
from src.settings import settings
from src.menus.options import options_menu
from src.menus.menu_class import custom_theme


"""Initialises menu"""
game_menu = pygame_menu.Menu(
    'Main Menu', settings.screen_width, settings.screen_height, theme=custom_theme)

game_menu.add.selector(
    'Subject :', [
        ('maths', 1), ('english', 2), ('science', 3)
    ],
    onchange=set_subject
)
# subject = game_menu.selector.get_value()[0]
game_menu.add.button('Play', start_game)
game_menu.center_content()


# Create a horizontal frame at the bottom of the screen
game_menu.bottom_frame = game_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
    border_width=0
)

# Add three buttons to the frame
game_menu.bottom_frame.pack(game_menu.add.button('Options', options_menu))
game_menu.bottom_frame.pack(
    game_menu.add.button('Back', pygame_menu.events.BACK))
game_menu.bottom_frame.pack(
    game_menu.add.button('Exit', pygame_menu.events.EXIT))
