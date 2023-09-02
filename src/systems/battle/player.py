from src.systems.battle.units import HealthBar, Units
import pygame



class Player(Units):
    def __init__(self, state_manager, mana=100, health=100, attack=20, defence=10):
        super().__init__(health, attack, defence)
        self.sm = state_manager
        self.mana = mana
        self.acting = True
        self.healthbar = HealthBar(100, 900, 100, 10, self.total_health)
        self.boosted = False
        self.boosted_attr = {}
        self.block = False
        self.items = []


    def block(self):
        self.defence += 10
        self.block = True

    def remove_block(self):
        if self.block == True:
            self.defence -= 10
            self.block = False

    def post_game_heal(self):
        self.current_health += 50

    def draw(self, screen):
        self.healthbar.draw(screen, self.current_health)

    def alternate_acting(self):
        self.acting = True if self.acting == False else False

    def reset_boosted(self):
        if self.boosted == True:
            for attribute, base_value in self.boosted_attr.items():
                self[attribute] = base_value

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.push(item)

    def remove_item(self, item): #use item
        for i, object in enumerate(self.items):
            if item.name == object.name:
                return self.items.pop(i)




