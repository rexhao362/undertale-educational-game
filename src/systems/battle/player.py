from src.systems.battle.units import HealthBar, Units
from src.systems.sprite_sheet import SpriteSheet
from pygame.sprite import Sprite, Group


class Player(Units):
    def __init__(self, name, mana=100, health=100, attack=20, defence=10):
        super().__init__(name, health, attack, defence)
        self.mana = mana
        self.acting = True
        self.healthbar = HealthBar(300, 450, 200, 20, self.health_capacity)
        self.boosted = False
        self.boosted_attr = {}
        self.set_ = False
        self.items = []
        self.fight_animation = SpriteSheet(
            'assets/pictures/spritesheets/attack.png', 99, 152, 3, 6)

    def draw(self, screen):
        self.healthbar.draw(screen, self.current_health)
        self.draw_status(300, 430, screen)

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

    def draw_attack(self, screen, time_delta):
        if self.fight_animation.fin == False:
            self.fight_animation.play( screen, time_delta, (400,300))
