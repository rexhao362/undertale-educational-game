from game.systems.battle.enemy import Enemy


class Stage:
    def __init__(self, player, current_stage) -> None:
        self.player = player
        self.stage = current_stage
        self.enemy

    def make_enemy(self):
        enemy_name  # read enemy folders and choose random one
        self.enemy = Enemy(enemy_name)