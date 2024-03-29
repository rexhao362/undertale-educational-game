import pygame

pygame.init()
pygame.mixer.init()


class Settings:
    """Class that stores game settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 710
        self.clock = pygame.time.Clock()
        self.time_delta = self.clock.tick(60)/1000.0


settings = Settings()
screen_values = (
    settings.screen_width,
    settings.screen_height
)
screen = pygame.display.set_mode(screen_values)

pygame.display.set_caption('Learning with Undertale')


def transform_background(filename):
    pygame.transform.scale(pygame.image.load(filename), screen_values)
