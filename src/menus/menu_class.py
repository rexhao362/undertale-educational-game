import pygame_menu
from src.settings import settings
from src.menus.options import options_menu

# Create a custom theme to add a background image
custom_theme = pygame_menu.themes.THEME_DARK.copy()
image = pygame_menu.baseimage.BaseImage(
    image_path='./assets/pictures/menu_bg.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)
custom_theme.background_color = image
custom_theme.font = pygame_menu.font.FONT_8BIT


class Menu(pygame_menu.Menu):
    """Class that sets default menu format"""

    def __init__(self, name):  # , screen):
        """Initialises menu"""
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        super().__init__(name, self.screen_width/2, self.screen_height/2, theme=custom_theme)

        # Create a horizontal frame at the bottom of the screen
        self.bottom_frame = self.add.frame_h(
            width=self.screen_width,
            height=100,
            vertical_alignment=pygame_menu.locals.POSITION_SOUTH,
            horizontal_alignment=pygame_menu.locals.ALIGN_CENTER,
            border_width=0
        )

        # Add three buttons to the frame
        self.bottom_frame.pack(self.add.button('Options', options_menu))
        self.bottom_frame.pack(self.add.button(
            'Back', pygame_menu.events.BACK))
        self.bottom_frame.pack(self.add.button(
            'Exit', pygame_menu.events.EXIT))
