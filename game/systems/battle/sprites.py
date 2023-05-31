from pygame.sprite import Sprite
import pygame


class Sprites(Sprite):
    def __init__(self, health, attack, defence):
        super.__init__()
        self.total_health = health
        self.current_health = health
        self.attack = attack
        self.defence = defence


class Battle_Screen(Sprite):
    def __init__(self, player, enemy):
        super.__init__()
        self.background = pygame.image.load('assets/pictures/...')