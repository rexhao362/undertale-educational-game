from pygame.sprite import Sprite


class Sprites(Sprite):
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense