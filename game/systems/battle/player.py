from combat import game_over

class Player:
    def __init__(self, user, health=100):
        super.__init__(self, )

    def check_game_over(self):
        if self.health <= 0:
            game_over()