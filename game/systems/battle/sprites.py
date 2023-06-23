from pygame.sprite import Sprite
import pygame


class Sprites(Sprite):
    def __init__(self, health, attack, defence):
        super.__init__()
        self.total_health = health
        self.current_health = health
        self.attack = attack
        self.defence = defence
        # self.image
        # self.rect = self.image.get_rect()
        # self.rect.center = (left, top)

    def attack_action(self, target):
        target.current_health -= self.attack

    def draw(self, screen):
        screen.blit


class Battle_Screen(Sprite):
    def __init__(self, player, enemy):
        super.__init__()
        self.background = pygame.image.load('assets/pictures/...')  # TODO


class HealthBar:
    def __init__(self, left, top, width, height, total_health):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.current_health = total_health
        self.total_health = total_health

    def draw(self, surface):
        ratio = self.current_health / self.total_health
        pygame.draw.rect(surface, "red", (self.left,
                         self.top, self.width, self.height))
        pygame.draw.rect(surface, "green", (self.left,
                         self.top, self.width * ratio, self.height))
