from src.systems.battle.units import HealthBar, Units
import pygame
import pygame_gui


class Player(Units):
    def __init__(self, name, mana=100, health=100, attack=20, defence=10):
        super().__init__(name, health, attack, defence)
        self.mana = mana
        self.acting = True
        self.healthbar = pygame_gui.elements.UIScreenSpaceHealthBar(
            relative_rect=pygame.Rect(200, 500, 200, 30), sprite_to_monitor=self)
        self.boosted = False
        self.boosted_attr = {}
        self.set_ = False
        self.items = []

    def draw(self, screen):
        text = f'{self.name}    {self.current_health}/{self.health_capacity}'
        font = pygame.font.Font('data/fonts/league_spartan.ttf', 20)
        player = font.render(text, True, 'white')
        screen.blit(player, (100, 500))

    def set_block(self):
        self.defence += 5
        self.set_ = True

    def remove_block(self):
        if self.set_ == True:
            self.defence -= 5
            self.set_ = False

    def post_game_heal(self):
        self.modify_attribute('health', 50)


    def reset_boosted(self):
        if self.boosted == True:
            for attribute, base_value in self.boosted_attr.items():
                self[attribute] = base_value


