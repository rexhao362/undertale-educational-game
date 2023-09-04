from src.systems.battle.player import Player
from systems.battle.combat import Combat
import pygame
from src.settings import settings, screen
from src.manager import manager
import state_manager as state_manager
from src.systems.database.users import User


current_user = ['player']

pygame.init()




def start_game():
    # game = Game(current_user[0])
    sm = state_manager.StateManager(current_user[0])
    sm.set_state('combat')
    clock = pygame.time.Clock()

    while sm.running:
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