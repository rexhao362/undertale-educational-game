from combat import game_over
from systems.battle.sprites import Sprites


class Player(Sprites):
    def __init__(self, user, health=100, attack=10, defence=10):
        super.__init__(self, health, attack, defence)
        self.user = user

    def check_game_over(self):
        if self.health <= 0:
            game_over()