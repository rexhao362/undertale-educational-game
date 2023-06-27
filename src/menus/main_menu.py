# from menus.menu_class import Menu
import pygame_menu
from src.menus.game_menu import game_menu
from src.menus.parents_menu import parents_menu
from src.settings import settings
from src.menus.options import options_menu
from src.menus.menu_class import custom_theme


"""Initialises menu"""
main_menu = pygame_menu.Menu(
    'Main Menu', settings.screen_width, settings.screen_height, theme=custom_theme)

main_menu.font=pygame_menu.font.FONT_8BIT
main_menu.add.button('Kids', game_menu)
main_menu.add.button('Parents', parents_menu)#
main_menu.center_content()


# Create a horizontal frame at the bottom of the screen
main_menu.bottom_frame = main_menu.add.frame_h(
    width=settings.screen_width,
    height=100,
    # vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
    align=pygame_menu.locals.ALIGN_RIGHT,
    position=pygame_menu.locals.POSITION_SOUTHEAST,
    border_width=0
)

# Add three buttons to the frame
main_menu.bottom_frame.pack(main_menu.add.button('Options', options_menu))
main_menu.bottom_frame.pack(
    main_menu.add.button('Back', pygame_menu.events.BACK))
main_menu.bottom_frame.pack(
    main_menu.add.button('Exit', pygame_menu.events.EXIT))
