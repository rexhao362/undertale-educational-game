import pygame
from random import choice
from systems.battle.combat import Combat
from systems.battle.player import Player
from systems.database.users import User
from systems.map.inventory import Inventory
from systems.questions.maths.quiz_maths import MathsQuiz
from systems.questions.spelling.spelling_quiz import SpellingQuiz


class StateManager:
    def __init__(self, username):
        self.state = None
        self.state_name = None
        self.stage = 1
        self.previous_state = None
        self.success = None
        self.running = True
        self.inventory = Inventory(self)
        self.user = User(username)
        self.player = Player(self.user)


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

    def set_state(self, new_state):
        # if new_state == 'map':
        #     self.state = Map(self)
        if new_state == 'combat':
            self.state = Combat(self)
        elif new_state == 'quiz':
            selection = choice(['spelling', 'maths'])
            self.state = SpellingQuiz(
                self) if selection == 'spelling' else MathsQuiz(self)
        elif new_state == 'inventory':
            self.state = self.inventory

    def reload_state(self):
        if self.previous_state['name'] == 'combat':
            self.state = Combat(self, **self.previous_state)
    
        self.state.reward_check()

    def next_stage(self):
        self.stage += 1

    def set_success(self, bool):
        self.success = bool

    def get_success(self):
        return self.success
