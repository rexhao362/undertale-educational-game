from game.systems.battle.enemy import create_enemy


class Stage:
    def __init__(self, screen, player, current_stage):
        self.screen = screen
        self.player = player
        self.stage = current_stage
        self.enemy = create_enemy()
        self.image

    def check_win(self):
        if self.enemy.check_is_alive():
            pass

    def game_over(self):
        if self.player.check_is_alive():
            self.screen.blit(defeat_img)