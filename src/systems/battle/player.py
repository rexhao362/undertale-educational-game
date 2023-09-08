from src.systems.battle.units import HealthBar, Units
import pygame


class Player(Units):
    def __init__(self, name, mana=2, health=200, attack=20, defence=10):
        super().__init__(name, health, attack, defence)
        self.mana = mana
        self.healthbar = HealthBar(300, 450, 200, 20, self.health_capacity)
        self.boosted = False
        self.boosted_attr = {}
        self.block = False
        self.items = []

    def draw(self, screen):
        self.healthbar.draw(screen, self.current_health)
        self.draw_status(300, 430, screen)
        self.draw_mana(screen)

    def set_block(self):
        self.defence += 5
        self.block = True
        text = f'{self.name} has blocked'
        self.text_entry.append(text)

    def remove_block(self):
        if self.block:
            self.defence -= 5
            self.block = False

    def post_game_heal(self):
        self.modify_attribute('health', 50)
        self.mana = 2
        self.status = None

    def reset_boosted(self):
        if self.boosted:
            for attribute, base_value in self.boosted_attr.items():
                self[attribute] = base_value

    def draw_attack(self, screen, time_delta):
        if self.hit['move'] is not None and not self.hit['move'].fin:
            self.hit['move'].play(screen, time_delta, (400, 300))

    def draw_mana(self, screen):
        mana = pygame.image.load(
            'assets/pictures/mana_star.png').convert_alpha()
        image_rect = mana.get_rect()
        image_width = image_rect.width
        pos_x = 50
        pos_y = 450
        spacing = 10
        for i in range(self.mana):
            screen.blit(mana, (pos_x, pos_y))
            pos_x += image_width + spacing
