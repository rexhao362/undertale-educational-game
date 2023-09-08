from pygame.sprite import Sprite
import pygame
from random import choice, randint


class Items(Sprite):
    def __init__(self, attribute, effect):
        super().__init__()
        self.target = 'player' if self.effect > 0 else 'enemy'
        self.name = attribute.toUpper(
        ) + ' UP' if self.target == 'player' else attribute.toUpper() + ' DOWN'
        self.description = description[attribute]
        self.image = pygame.load.image(
            f'assets/pictures/items/{self.name}.png')
        self.attribute = attribute
        self.effect = effect

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


def create_item():
    attribute = choice(['health', 'attack_power', 'defence'])
    effect = None
    if attribute == 'health':
        effect = randint(15, 30)
    else:
        effect = randint(3, 7)
    return Items(attribute, effect)


description = {
    'health': '',
    'attack_power': '',
    'defence': ''
}
