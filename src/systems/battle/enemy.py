from src.systems.battle.units import HealthBar, Units
import pygame
from random import choice, randint
from os import listdir


class Enemy(Units):
    def __init__(self, name, health=100, attack=20, defence=5):
        super().__init__(name, health, attack, defence)
        self.image = pygame.image.load(
            f'./assets/pictures/units/enemies/{self.name}.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (335, 100)
        self.healthbar = HealthBar(350, 10, 250, 30, self.health_capacity)

    def draw(self, screen):
        self.draw_status(350, 50, screen)
        self.healthbar.draw(screen, self.current_health)
        screen.blit(self.image, self.rect.center)

    def draw_attack(self, screen, time_delta):
        if not self.hit['move'].fin:
            self.hit['move'].play(screen, time_delta, (400, 600))

    def hit_player(self, target):
        num = randint(1, 100)
        if num <= 79:
            self.attack(target)
        elif num <= 86:
            self.fire_spell(target)
        elif num <= 93:
            self.thunder_spell(target)
        elif num <= 100:
            self.poison_spell(target)


enemy_pictures = listdir(f'assets/pictures/units/enemies')
enemy_names = [enemy.split('.')[0] for enemy in enemy_pictures]


def create_enemy():
    enemy = choice(enemy_names)
    return Enemy(enemy)
