from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.settings import settings, screen, manager
from src.systems.questions.maths.quiz_maths import MathsQuiz
from systems.questions.spelling.spelling_quiz import SpellingQuiz
from src.systems.database.users import User


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
    game.state = Stage(game, game.player, game.stage)

    while game.running:
        settings.time_delta
        
        game.state.events(manager)
        game.state.update()
        game.state.draw(screen, settings.time_delta, manager)
        
        manager.update(settings.time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()

if __name__  == 'main':
    start_game()