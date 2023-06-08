from game.systems.battle.enemy import Enemy
from game.systems.battle.player import Game

class Combat:
    def __init__(self, player):
        self.player = player
        self.enemy_name #read enemy folders and choose random one
        self.enemy = Enemy(self.enemy_name)


    def check_win(enemy):
        if enemy.check_enemy_defeat():
            pass


    def game_over(player):
        if player.check_game_over():
            pass

