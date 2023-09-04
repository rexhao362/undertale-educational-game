from src.systems.battle.units import Units, HealthBar
import pygame
import pygame_gui
from random import choice
from os import listdir

class Enemy(Units):
    def __init__(self, name, health=100, attack=10, defence=0):
        super().__init__(name, health, attack, defence)
        self.image = pygame.image.load(f'./assets/pictures/units/enemies/{self.name}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (430, 200)
        self.healthbar = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect(100, 500, 150, 30), sprite_to_monitor=self)


    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
        # self.healthbar.draw(screen, self.current_health)

    def draw_attack(self, screen, time_delta):
        pass

enemy_pictures = listdir(f'assets/pictures/units/enemies')
enemy_names = [enemy.split('.')[0] for enemy in enemy_pictures]


def create_enemy():
    enemy = choice(enemy_names)
    return Enemy(enemy)
