import pygame
from random import choice
from copy import deepcopy
from systems.battle.combat import Combat
from systems.battle.player import Player
from systems.database.users import User
from systems.map.inventory import Inventory
from systems.questions.maths.quiz_maths import MathsQuiz

from systems.questions.spelling.spelling_quiz import SpellingQuiz


class StateManager:
    def __init__(self, username):  # , state):
        self.state = None
        self.stage = 1
        self.previous_state = None
        self.success = None
        self.running = True
        self.inventory = Inventory(self)
        self.user = User(username)
        self.player = Player(self.user)
        # self.state_dict = set_state_dict(self)

    def run(self, screen, manager):
        clock = pygame.time.Clock()

        while self.running:
            time_delta = clock.tick(60)/1000.0
            screen.fill('black')

            self.state.events(manager)

            manager.update(time_delta)

            self.state.draw(screen, time_delta)
            self.state.update()

            manager.draw_ui(screen)

            pygame.display.flip()

        pygame.quit()

    def next_state(self, new_state):
        self.previous_state = deepcopy(self.state)
        # self.state = self.state_dict[new_state]
        # if new_state == 'map':
        #     self.state = Map(self)
        if new_state == 'combat':
            self.state = Combat(self)
        elif new_state == 'quiz':
            selection = choice(['spelling', 'maths'])
            # if selection == 'spelling:7
            self.state = SpellingQuiz(
                self) if selection == 'spelling' else MathsQuiz(self)
        elif new_state == 'inventory':
            self.state = self.inventory

        
    def back_state(self):
        self.state = deepcopy(self.previous_state)


    def next_stage(self):
        self.stage += 1

    def set_success(self, bool):
        self.success = bool

    def get_success(self):
        return self.success


def set_state_dict(state_manager):
    return {
        'map': '',
        'combat': Combat(state_manager),
        'quiz': choice([SpellingQuiz(state_manager), MathsQuiz(state_manager)]),
        'inventory': state_manager.inventory
    }
