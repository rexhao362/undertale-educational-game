class Player:
    def __init__(self, user, health=100):
        self.user = user
        self.heath = health

    def check_game_over(self):
        if self.health <= 0:
            game_over()
            pygame.