from pygame.sprite import Sprite
import pygame
from random import choice, randint


class Items(Sprite):
    def __init__(self, attribute, effect):
        super().__init__()
        self.attribute = attribute
        self.effect = effect
        self.target = 'player' if self.effect > 0 else 'enemy'
        self.name = gen_name(attribute, self.target)
        self.description = description[self.name]
        self.image = pygame.image.load(
            f'assets/pictures/items/{self.name}.png').convert_alpha()

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
    attribute = choice(['health', 'attack', 'defence'])
    effect = None
    if attribute == 'health':
        effect = randint(15, 30)
    else:
        effect = randint(-7, 7)
    return Items(attribute, effect)


def gen_name(attribute, target):
    if target == 'player':
        return (attribute.replace('_', ' ')).upper() + ' UP'
    else:
        return (attribute.replace('_', ' ')).upper() + ' DOWN'


description = {
    'HEALTH UP': 'Raises your current health',
    'ATTACK UP': 'Increases your attack , making you hit harder',
    'ATTACK DOWN': """Decreases the enemy's attack power,
                    making them hit for less""",
    'DEFENCE UP': """Increases your defence power,
                    allowing you to take more hits""",
    'DEFENCE DOWN': """Decreases the enemy's defence power,
                    allowing you to hit harder"""
}
