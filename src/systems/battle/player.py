from src.systems.battle.units import HealthBar, Units
import pygame



class Player(Units):
    def __init__(self, user, mana=100, health=100, attack=10, defence=10):
        super().__init__(health, attack, defence)
        self.user = user
        self.mana = mana
        self.acting = True
        self.items = {}
        self.healthbar = HealthBar()
        self.boosted = False
        self.boosted_attr = {}


    def action(self, target):
        self.acting = False

    def block(self):
        self.defence += 10

    def draw(self, screen):
        self.healthbar.draw(screen, self.current_health)

    def alternate_acting(self):
        self.acting = True if self.acting == False else False

    def reset_boosted(self):
        if self.boosted == True:
            for attribute, base_value in self.boosted_attr.items():
                self[attribute] = base_value





