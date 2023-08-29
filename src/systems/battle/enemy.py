from src.systems.battle.units import Units, HealthBar
import pygame
from random import choice
from os import listdir

class Enemy(Units):
    def __init__(self, name, health=100, attack=20, defence=0):
        super().__init__(health, attack, defence)
        self.name = name
        self.image = pygame.image.load(f'./assets/pictures/units/enemies/{self.name}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (600, 200)
        self.healthbar = HealthBar()

    def draw(self, screen):
        screen.blit(self.enemy)
        self.healthbar.draw(screen, self.current_health)

    def draw_attack(self, screen):
        pass

enemy_pictures = listdir(f'assets/pictures/units/enemies')
enemy_names = [enemy.split('.')[0] for enemy in enemy_pictures]


def create_enemy():
    enemy = choice(enemy_names)
    return Enemy(enemy)
