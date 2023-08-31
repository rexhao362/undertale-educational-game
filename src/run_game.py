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
        self.state = None
        self.previous_state = None

    def next_stage(self):
        self.stage += 1

    def set_state(self, state):
        self.previous_state = self.state
        self.state = state


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
                    # Quit this function, then skip to loop of main-menu on line 221
                    

def start_game():
    game = Game(current_user[0])
    sm = state_manager.StateManager()
    # sm.current_state = Stage(game, game.player, game.stage)
    sm.current_state = SpellingQuiz(User('player'))
    clock = pygame.time.Clock()

    while game.running:
        time_delta = clock.tick(60)/1000.0
        
        sm.current_state.events(manager)
        sm.current_state.update()
        sm.current_state.draw(screen, time_delta, manager)
        
        manager.draw_ui(screen)
        manager.update(time_delta)

        pygame.display.flip()

if __name__  == 'main':
    start_game()