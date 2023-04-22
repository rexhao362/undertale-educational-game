import pygame
import pygame_menu

class Menu(pygame_menu.Menu):
    """Class that sets default menu format"""
    def __init__(self, name, screen):
        """Initialises menu"""
        super().__init__(title=name, theme=pygame_menu.themes.THEME_DARK)
        self.add.button('Go to Start', pygame_menu.events.RESET)
        self.add.button('Exit', pygame_menu.events.EXIT)

class Button():
    def __init__(self, name, size='big'):
        name = self.name
        size = self.size