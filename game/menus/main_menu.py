# from menus.menu_class import Menu
from menus.game_menu import game_menu
from menus.parents_menu import parents_menu
from game.settings import settings
import pygame_menu
from game.menus.options import options_menu
from game.menus.menu_class import custom_theme


main_menu = pygame_menu.Menu(
    'Main Menu', settings.screen_width/2, settings.screen_height/2, theme=custom_theme)

main_menu.add.button('Kids', game_menu)
main_menu.add.button('Parents', parents_menu)
"""Initialises menu"""


# Create a horizontal frame at the bottom of the screen
main_menu.bottom_frame = main_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
    border_width=0
)

# Add three buttons to the frame
main_menu.bottom_frame.pack(main_menu.add.button('Options', options_menu))
main_menu.bottom_frame.pack(
    main_menu.add.button('Back', pygame_menu.events.BACK))
main_menu.bottom_frame.pack(
    main_menu.add.button('Exit', pygame_menu.events.EXIT))
