from random import choice
from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
import src.menus.main_menu as m
from src.settings import settings, screen
from src.systems.questions.maths.quiz_maths import MathsQuiz
from systems.questions.spelling.spelling_quiz import SpellingQuiz
from src.systems.database.users import User


current_user = ['player']
current_subject = ['maths']


class Game:
    def __init__(self, username):
        # self.screen = screen
        self.user = User(username)
        self.player = Player(self.user)
        self.stage = 0
        self.running = True
        self.state_name = None
        self.state = None

    def next_stage(self):
        self.stage += 1
        return Stage(self.player, self.stage)

    def set_state(self, state):
        self.state = state

    def state_manager(self):
        if self.state_name == 'stage':
            self.stage += 1
            self.state = Stage(self.player, self.stage)
        elif self.state_name == 'quiz':
            self.state = choice([MathsQuiz(), SpellingQuiz()])
        elif self.state_name == 'tilemap':
            pass


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Event handling for a range of different key presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    m.main_menu.enable()
                    # Quit this function, then skip to loop of main-menu on line 221
                    

def start_game():
    game = Game(current_user[0])
    m.main_menu.disable()
    game.state = Stage(game.player, game.stage)
    while game.running:
        settings.clock.tick(settings.fps)
        
        game.state.events(manager)

        game.state.draw(screen)
        pygame.display.flip()
