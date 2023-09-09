import pygame_menu
from src.menus.menu_class import custom_theme
from src.menus.users_menu import set_current_user
from src.settings import settings
from src.systems.database.users import get_users_names
from src.systems.database.donut_graph import donut_graph_draw

current_subject = ['maths']


def set_current_subject(value, subject):
    current_subject[0] = subject


"""Initialises menu"""
parents_menu = pygame_menu.Menu(
    'Database',
    settings.screen_width,
    settings.screen_height,
    theme=custom_theme
)

parents_menu.add.selector(
    'User :', [(name, name) for name in get_users_names()],
    onchange=set_current_user
)
parents_menu.add.selector(
    'Subject :', [('Maths', 'maths'), ('Spelling', 'spelling')],
    onchange=set_current_subject
)

parents_menu.add.button('Graph', donut_graph_draw)

