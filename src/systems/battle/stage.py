from src.systems.battle.enemy import create_enemy
import pygame

class Stage:
    def __init__(self, screen, player, current_stage):
        self.screen = screen
        self.player = player
        self.stage = current_stage
        self.enemy = create_enemy()
        self.image

    def victory(self):
        if not self.enemy.is_alive():
            self.screen.blit(victory_img)
            self.game_won()

    def game_over(self):
        if not self.player.is_alive():
            self.screen.blit(defeat_img)

    def game_won(self):
        if self.stage == 5:
            pygame.quit()

    def turn_combat(self):
        self.player.action()
        self.victory()
        self.enemy.attack()
        self.game_over()