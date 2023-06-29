import pygame_menu
from src.settings import settings
import shelve
import pygame
from src.menus.menu_class import custom_theme
from src.menus.game_menu import game_menu
from src.menus.options import options_menu

filename = ''

def get_user_names():
    with shelve.open(filename) as f:
        return dict.keys(f)


def set_user_name(name):
    pass



pygame_menu.widgets.TextInput('Create New User', textinput_id='new_user', maxchar=50, onreturn=create_user)

user_menu = pygame_menu.Menu(
    'user Menu', settings.screen_width, settings.screen_height, theme=custom_theme)

user_menu.font = pygame_menu.font.FONT_8BIT
for name in get_user_names:
    user_menu.add.button('name', set_user_name, game_menu)
user_menu.add.button('Create New User', create_user)
user_menu.center_content()


# Create a horizontal frame at the bottom of the screen
user_menu.bottom_frame = user_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    # vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    align=pygame_menu.locals.ALIGN_RIGHT,
    position=pygame_menu.locals.POSITION_SOUTHEAST,
    border_width=0
)

# Add three buttons to the frame
user_menu.bottom_frame.pack(user_menu.add.button('Options', options_menu))
user_menu.bottom_frame.pack(
    user_menu.add.button('Back', pygame_menu.events.BACK))
user_menu.bottom_frame.pack(
    user_menu.add.button('Exit', pygame_menu.events.EXIT))
