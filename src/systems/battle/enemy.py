from src.systems.battle.units import Units
import pygame
from random import choice


class Enemy(Units):
    def __init__(self, name, health=100, attack=20, defence=0):
        super().__init__(health, attack, defence)
        self.name = name
        self.image = pygame.load.image(f'./assets/pictures/units/enemies/{self.name}.png')
        self.rect = self.image.get_rect()



enemy_names = ['sans', 'undyne', 'asgore', 'mettaton',
               'muffet', 'papyrus', 'flowey', 'aaron', 'froggit', 'asriel']


def create_enemy():
    enemy_list = enemy_names
    enemy = choice(enemy_list)
    return Enemy(enemy)
