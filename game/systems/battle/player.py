from game.systems.battle.units import Units
import pygame


class Player(Units):
    def __init__(self, user, mana, health=100, attack=10, defence=10):
        super.__init__(self, health, attack, defence)
        self.user = user
        self.mana = mana
        self.acting = False

    def update_user(self):
        pass


