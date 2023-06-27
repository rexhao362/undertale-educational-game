from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.main import screen

class Game:
    def __init__(self, screen, user):
        self.screen = screen
        self.user = user
        self.player = Player(self.user)
        self.stage = 0

    
    def next_stage(self):
        self.stage += 1
        return Stage(self.screen, self.player, self.stage)

def start_game(user):
    game = Game(screen, user)
    while game.stage < 5:
        game.next_stage()