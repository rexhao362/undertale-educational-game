from sprites import Sprites
import pygame

class Enemy(Sprites):
    def __init__(self, name, health, attack, defence):
        super().__init__(health, attack, defence)
        self.name = name
        self.image = pygame.load.image(f'./assets/pictures/chars/{name}')
        self.rect = self.image.get_rect()

    def check_enemy_defeat(self):
        return self.current_health <= 0