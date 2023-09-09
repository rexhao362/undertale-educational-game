import pygame_menu
from app import run_app, current_user
from src.settings import settings
from src.menus.menu_class import custom_theme
from src.systems.database.users import create_user, get_users_names


def set_current_user(value, name):
    current_user[0] = name


user_menu = pygame_menu.Menu(
    'user Menu',
    settings.screen_width,
    settings.screen_height,
    theme=custom_theme
)

user_menu.font = pygame_menu.font.FONT_8BIT
user_menu.add.selector(
    'User :', [(name, name) for name in get_users_names()],
    onchange=set_current_user
)
user_menu.add.button('Play', run_app)
user_menu.add.text_input('Create New User  :  ', default='',
                         onreturn=create_user)

user_menu.center_content()
