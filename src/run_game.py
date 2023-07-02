from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.main import screen

class Game:
    def __init__(self, screen, subject, user='guest'):
        self.screen = screen
        self.user = user
        self.player = Player(self.user)
        self.subject = subject
        self.stage = 0

    
    def next_stage(self):
        self.stage += 1
        return Stage(self.screen, self.player, self.stage)
    
    def set_subject(self, subject):
        self.subject = subject

def start_game(user, subject):
    game = Game(screen, subject, user )
    while game.stage < 5:
        game.next_stage()