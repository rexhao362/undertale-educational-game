import pygame_menu


class Options(pygame_menu.Menu):
    def __init__(self):#, screen):
        """Initialises menu"""
        super().__init__('Options', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        # Options #TODO

        # Create menu bar for banner
        self.menu_bar = pygame_menu.MenuBar(
            300, 50, pygame_menu.menu.MenuBarPosition.BOTTOM)
        self.menu.add_widget(self.menu_bar)

        # Add buttons to menu bar
        self.menu_bar.add.button('Back', pygame_menu.events.BACK)
        self.menu_bar.add.button('Exit', pygame_menu.events.EXIT)


options_menu = Options()
