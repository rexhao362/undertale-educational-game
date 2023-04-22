import pygame_menu
from options_menu import options_menu

custom_theme = pygame_menu.themes.THEME_DARK.copy()
image = pygame_menu.baseimage.BaseImage(
    image_path='./undertale_bg.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    offset=(0, 0)
)
custom_theme.background_color = image



class Menu(pygame_menu.Menu):
    """Class that sets default menu format"""

    def __init__(self, name, screen):
        """Initialises menu"""
        super().__init__(name, 400, 300, theme=custom_theme)
        self.add.button('Options', options_menu)
        self.add.button('Back', pygame_menu.events.BACK)
        self.add.button('Exit', pygame_menu.events.EXIT)

# class Button():
#     def __init__(self, name, size='big'):
#         name = self.name
#         size = self.size
