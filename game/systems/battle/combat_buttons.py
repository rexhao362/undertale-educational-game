import pygame


class Buttons:
    def __init__(self, name, screen):
        self.name = name
        self.image = pygame.load.image(
            f'assets/pictures/buttons/{self.name}.png')
        self.rect = self.image.get_rect()
        
