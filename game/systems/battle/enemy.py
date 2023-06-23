from sprites import Sprites
import pygame
from random import choice


class Enemy(Sprites):
    def __init__(self, name, health=100, attack=20, defence=0):
        super().__init__(health, attack, defence)
        self.name = name
        self.image = pygame.load.image(f'./assets/pictures/chars/{name}')
        self.rect = self.image.get_rect()

    def check_enemy_defeat(self):
        return self.current_health <= 0


enemy_names = ['sans', 'undyne', 'asgore', 'mettaton',
               'muffet', 'papyrus', 'flowey', 'aaron', 'froggit', 'asriel']


def create_enemy():
    enemy_list = enemy_names
    enemy = choice(enemy_list)
    return Enemy(enemy)
