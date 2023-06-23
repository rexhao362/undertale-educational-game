from game.systems.battle.enemy import create_enemy


class Stage:
    def __init__(self, screen, player, current_stage):
        self.screen = screen
        self.player = player
        self.stage = current_stage
        self.enemy = create_enemy()
        self.image

    def check_win(self):
        if self.enemy.check_enemy_defeat():
            pass

    def game_over(self):
        if self.player.check_game_over():
            self.screen.blit(defeat_img)