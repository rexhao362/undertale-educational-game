import pygame
import pygame_menu


class Options(pygame_menu.Menu):
    def __init__(self):#, screen):
        """Initialises menu"""
        super().__init__('Options', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        # Options #TODO


        # Create menu bar for banner
        self.menu_bar = self.add.frame_h(400, 30)
        self.menu_bar.set_max_height(21)
        # self.menu.add_widget(self.menu_bar)

        # Add buttons to menu bar
        self.menu_bar.pack(self.add.button('Back', pygame_menu.events.BACK))
        self.menu_bar.pack(self.add.button('Exit', pygame_menu.events.EXIT))


options_menu = Options()