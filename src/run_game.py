from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.settings import settings, screen, manager
import src.systems.state_manager as state_manager
from src.systems.database.users import User
from systems.questions.spelling.spelling_quiz import SpellingQuiz


current_user = ['player']
current_subject = ['maths']

pygame.init()

class Game:
    def __init__(self, username):
        # self.screen = screen
        self.user = User(username)
        self.player = Player(self.user)
        self.stage = 0
        self.running = True

    def next_stage(self):
        self.stage += 1


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
    sm = state_manager.StateManager()
    # sm.state = Stage(sm, game.player, game.stage)
    sm.state = SpellingQuiz(sm, game.user)
    clock = pygame.time.Clock()

    while game.running:
        time_delta = clock.tick(60)/1000.0
        
        sm.state.events(manager)

        manager.update(time_delta)
        
        sm.state.draw(screen, time_delta, manager)
        sm.state.update()
        
        manager.draw_ui(screen)

        pygame.display.flip()
    
    pygame.quit()

if __name__  == 'main':
    start_game()