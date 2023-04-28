from pygame.sprite import Sprite


class Sprites(Sprite):
    def __init__(self, health, attack, defence):
        self.total_health = health
        self.current_health = health
        self.attack = attack
        self.defence = defence