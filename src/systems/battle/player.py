from src.systems.battle.units import HealthBar, Units
import pygame
import pygame_gui


class Player(Units):
    def __init__(self, name, mana=100, health=100, attack=20, defence=10):
        super().__init__(name, health, attack, defence)
        self.mana = mana
        self.acting = True
        self.healthbar = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect(100, 500, 150, 30), sprite_to_monitor=self)
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

    # def draw(self, screen):
    #     self.healthbar.draw(screen, self.current_health)

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

    def remove_item(self, item):  # use item
        for i, object in enumerate(self.items):
            if item.name == object.name:
                return self.items.pop(i)
