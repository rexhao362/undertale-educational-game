from src.systems.battle.player import Player
from systems.battle.combat import Combat
import pygame
from src.settings import settings, screen
from src.manager import manager
import state_manager as state_manager
from src.systems.database.users import User


current_user = ['player']

pygame.init()

class Game:
    def __init__(self, username):
        # self.screen = screen
        self.user = User(username)
        self.player = Player(self.user)
        self.stage = 0
        self.running = True



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Event handling for a range of different key presses
            elif event.type == pygame.KEYDOWN:
                pass
                # if event.key == pygame.K_ESCAPE:
                #     m.main_menu.enable()


def start_game():
    game = Game(current_user[0])
    sm = state_manager.StateManager(current_user[0])
    sm.next_state('quiz')
    clock = pygame.time.Clock()

    while game.running:
        time_delta = clock.tick(60)/1000.0
        screen.fill('black')
        sm.state.events(manager)

        manager.update(time_delta)
        sm.state.draw(screen, time_delta)
        sm.state.update()
        
        manager.draw_ui(screen)

        pygame.display.flip()
    
    pygame.quit()

if __name__  == 'main':
    start_game()