import pygame

class Settings:
    """Class that stores game settings."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.clock = pygame.time.Clock()
        self.fps = 60
        # self.bg_colour = (0, 0, 0)
    
    def set_resolution(self, value, width_height):
        self.screen_width = width
        self.screen_height = height

settings = Settings()