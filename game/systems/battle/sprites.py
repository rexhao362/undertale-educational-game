from pygame.sprite import Sprite


class Sprites(Sprite):
    def __init__(self, health, attack, defence):
        self.health = health
        self.attack = attack
        self.defence = defence