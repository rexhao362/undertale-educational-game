import pygame_menu
from src.menus.menu_class import custom_theme
from src.menus.users_menu import set_current_user
from src.settings import settings
from src.menus.options import options_menu
from src.systems.database.users import get_users_names
from src.systems.database.donut_graph import donut_graph_draw

current_subject = ['maths']

def set_current_subject(value, subject):
    current_subject[0] = subject


"""Initialises menu"""
parents_menu = pygame_menu.Menu(
    'Database', settings.screen_width, settings.screen_height, theme=custom_theme)

parents_menu.add.selector(
    'User :', [(name, name) for name in get_users_names()],
    onchange=set_current_user
)
parents_menu.add.selector(
    'Subject :', [('Maths', 'maths'), ('Spelling', 'spelling')],
    onchange=set_current_subject
)

parents_menu.add.button('Graph', donut_graph_draw)
# Create a horizontal frame at the bottom of the screen
parents_menu.bottom_frame = parents_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
    border_width=0
)

# Add three buttons to the frame
parents_menu.bottom_frame.pack(
    parents_menu.add.button('Options', options_menu))
parents_menu.bottom_frame.pack(
    parents_menu.add.button('Back', pygame_menu.events.BACK))
parents_menu.bottom_frame.pack(
    parents_menu.add.button('Exit', pygame_menu.events.EXIT))
