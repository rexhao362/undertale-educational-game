import pygame


class Buttons:
    def __init__(self, name, screen):
        self.name = name
        self.screen = screen
        self.image = pygame.load.image(
            f'assets/pictures/buttons/{self.name}.png')
        self.rect = self.image.get_rect()
        
    def draw(self):
        self.screen.blit(self.image, self.rect)

