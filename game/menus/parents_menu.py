from menus.menu_class import custom_theme
import pygame_menu
from game.settings import settings
from game.menus.options import options_menu


"""Initialises menu"""
parents_menu = pygame_menu.Menu(
    'Database', settings.screen_width, settings.screen_height, theme=custom_theme)


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
