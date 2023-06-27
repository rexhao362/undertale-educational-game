from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame


class Game:
    def __init__(self, screen, user):
        self.screen = screen
        self.user = user
        self.player = Player(self.user)
        self.stage = 0

    
    def next_stage(self):
        self.stage += 1
        return Stage(self.screen, self.player, self.stage)

def start_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update Pygame display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()