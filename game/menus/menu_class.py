import pygame_menu
from game.menus.options_menu import options_menu

custom_theme = pygame_menu.themes.THEME_DARK.copy()
image = pygame_menu.baseimage.BaseImage(
    image_path='./assets/pictures/undertale_bg.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    offset=(0, 0)
)
custom_theme.background_color = image



class Menu(pygame_menu.Menu):
    """Class that sets default menu format"""

    def __init__(self, name):#, screen):
        """Initialises menu"""
        super().__init__(name, 400, 300, theme=custom_theme)

        # Create menu bar for banner
        self.menu_bar = pygame_menu.MenuBar(300, 50, pygame_menu.menu.MenuBarPosition.BOTTOM)
        self.menu.add_widget(self.menu_bar)

        # Add buttons to menu bar
        self.menu_bar.add.button('Options', options_menu)
        self.menu_bar.add.button('Back', pygame_menu.events.BACK)
        self.menu_bar.add.button('Exit', pygame_menu.events.EXIT)

