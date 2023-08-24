from src.systems.battle.enemy import create_enemy
import pygame

class Stage:
    def __init__(self, screen, player, current_stage):
        self.screen = screen
        self.player = player
        self.stage = current_stage
        self.enemy = create_enemy()
        self.screen.fill((0, 0, 0))
        self.bg_image = pygame.image.load('assets/pictures/backgrounds/boss_battle_bg.png')
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.center = (600, 400)

    def victory(self):
        if not self.enemy.is_alive():
            victory_img = 'assets/pictures/victory.png'
            # self.screen.blit(victory_img)
            self.player.user.update_user()
            self.game_won()

    def game_over(self):
        if not self.player.is_alive():
            defeat_img = 'assets/pictures/game_over.png'
            # self.screen.blit(defeat_img)

    def game_won(self):
        if self.stage == 5:
            pygame.quit()

    def turn_combat(self):
        self.player.action(self.enemy)
        self.victory()
        self.enemy.attack(self.player)
        self.game_over()

    def draw(self):
        self.screen.blit(self.bg_image, self.bg_rect, self.enemy)

    def events(self):
        pass
