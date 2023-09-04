from systems.state import State
import pygame

class PostGame(State.State):
    def __init__(self, state_manager):
        super().__init__(state_manager)

    def draw(self, screen, time_delta):
        if self.sm.win == True:
            if self.stage == 5:
                pass
            else:
                pass
        else:
            pass

    def update(self):
        pass

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.sm.stage == 5:
                    exit()
                else:
                    self.sm.set_stage('tilemap')

            elif event.type == pygame.KEYDOWN:
                if self.sm.stage == 5:
                    exit()
                else:
                    self.sm.set_stage('tilemap')
