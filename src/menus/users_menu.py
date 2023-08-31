import pygame_menu
from src.run_game import start_game, current_user
from src.settings import settings
from src.menus.menu_class import custom_theme
from src.menus.options import options_menu
from src.systems.database.users import create_user, get_users_names


def set_current_user(value, name):
    current_user[0] = name


user_menu = pygame_menu.Menu(
    'user Menu', settings.screen_width, settings.screen_height, theme=custom_theme)

user_menu.font = pygame_menu.font.FONT_8BIT
user_menu.add.text_input('Create New User  :  ', default='',
                         onreturn=create_user)
user_menu.add.selector(
    'User :', [(name, name) for name in get_users_names()],
    onchange=set_current_user
)
user_menu.add.button('Play', start_game)

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
