import pygame_menu
from game.settings import settings


class Options(pygame_menu.Menu):
    def __init__(self):
        """Initialises menu"""
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        super().__init__('Options', self.screen_width/2,
                         self.screen_height/2, theme=pygame_menu.themes.THEME_DARK)
        # Options #TODO

        self.bottom_frame = self.add.frame_h(
            width=self.screen_width,
            height=100,
            vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
            horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
            border_width=0
        )

        # Add three buttons to the frame
        self.bottom_frame.pack(self.add.button(
            'Back', pygame_menu.events.BACK))
        self.bottom_frame.pack(self.add.button(
            'Exit', pygame_menu.events.EXIT))
        # # Create menu bar for banner
        # self.menu_bar = self.add.frame_h(400, 30)
        # self.menu_bar.set_max_height(21)
        # # self.menu.add_widget(self.menu_bar)

        # # Add buttons to menu bar
        # self.menu_bar.pack(self.add.button('Back', pygame_menu.events.BACK))
        # self.menu_bar.pack(self.add.button('Exit', pygame_menu.events.EXIT))


options_menu = Options()
print(dir(Options()))
