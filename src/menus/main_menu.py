# from menus.menu_class import Menu
import pygame_menu
from src.settings import settings
from src.menus.users_menu import user_menu
from src.menus.parents_menu import parents_menu
from src.menus.menu_class import custom_theme

music = pygame_menu.sound.Sound()
music.set_sound(pygame_menu.sound.SOUND_TYPE_OPEN_MENU,
                'assets/music/Various Themes/Waiting.ogg')

"""Initialises menu"""
main_menu = pygame_menu.Menu(
    'Main Menu',
    settings.screen_width,
    settings.screen_height,
    theme=custom_theme
)

main_menu.font = pygame_menu.font.FONT_8BIT
main_menu.set_sound(music, recursive=True)
main_menu.add.button('Kids', user_menu)
main_menu.add.button('Parents', parents_menu)
main_menu.center_content()
