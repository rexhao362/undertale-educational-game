from game.systems.battle.player import Game


class Combat:
    def __init__(self, screen, player, enemy):
        self.screen = screen
        self.player = player
        self.enemy = enemy

    def check_win(self):
        if self.enemy.check_enemy_defeat():
            pass

    def game_over(self):
        if self.player.check_game_over():
            self.screen.blit(defeat_img)
