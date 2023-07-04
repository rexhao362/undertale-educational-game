from src.systems.battle.units import Units
import pygame


class Player(Units):
    def __init__(self, user, mana=100, health=100, attack=10, defence=10):
        super().__init__(health, attack, defence)
        self.user = user
        self.mana = mana
        self.acting = False
        


    def action(self, target):
        pass

    def block(self):
        self.defence += 10

    


