import pygame
from random import choice
from src.systems.battle.combat import Combat
from src.systems.battle.player import Player
from src.systems.battle.postgame import PostGame
from src.systems.database.users import User
from src.systems.map.inventory import Inventory
from src.systems.map.tilemap import TileMap
from src.systems.questions.maths.quiz_maths import MathsQuiz
from src.systems.questions.spelling.spelling_quiz import SpellingQuiz


class StateManager:
    def __init__(self, username, screen, manager):
        self.screen = screen
        self.manager = manager
        self.stage = 0
        self.state = None
        self.previous_state = None
        self.success = None
        self.running = True
        self.inventory = Inventory(self)
        self.user = User(username)
        self.player = Player(username)
        self.game_over = False
        self.cont_game = True

    def run(self, screen, manager):
        clock = pygame.time.Clock()
        self.set_state('tilemap')

        while self.running:
            time_delta = clock.tick(60)/1000.0
            screen.fill('black')

            self.state.events(manager)

            manager.update(time_delta)

            self.state.update()
            self.state.draw(screen, time_delta)

            manager.draw_ui(screen)

            pygame.display.flip()

        pygame.quit()

    def set_state(self, new_state):
        self.manager.clear_and_reset()
        if new_state == 'tilemap':
            self.stage += 1
            self.state = TileMap(self)
        elif new_state == 'combat':
            self.state = Combat(self)
        elif new_state == 'quiz':
            self.state.store_state()
            selection = choice(['spelling', 'maths'])
            self.state = SpellingQuiz(
                self) if selection == 'spelling' else MathsQuiz(self)
        elif new_state == 'inventory':
            self.state = self.inventory
        elif new_state == 'postgame':
            self.state = PostGame(self)

    def reload_state(self):
        self.manager.clear_and_reset()
        if self.previous_state['name'] == 'combat':
            self.state = Combat(self, **self.previous_state)
        elif self.previous_state['name'] == 'tilemap':
            self.state = TileMap(self, **self.previous_state)

        self.state.reward_check()

    def set_success(self, bool):
        self.success = bool

    def get_success(self):
        return self.success
