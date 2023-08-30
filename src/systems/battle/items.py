from pygame.sprite import Sprite
import pygame
from random import choice

class Items(Sprite):
    def __init__(self, name, target, description, attribute, effect):
        super.__init__()
        self.name = name
        self.description = description
        self.image = pygame.load.image(f'assets/pictures/items/{self.name}.png')
        self.attribute = attribute
        self.effect = effect
        self.target = 'player' if self.effect > 0 else 'enemy'

    def apply_effect(self, target):
        target.modify_attribute(self.attribute, self.effect)


    def display_info(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Target': self.target,
            'Attribute': self.attribute,
            'Effect': self.effect
        }

    def draw(self):
        pass