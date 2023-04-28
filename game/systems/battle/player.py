from systems.battle.sprites import Sprites


class Player(Sprites):
    def __init__(self, user, mana, health=100, attack=10, defence=10):
        super.__init__(self, health, attack, defence)
        self.user = user
        self.mana = mana

    def check_game_over(self):
        return self.health <= 0
