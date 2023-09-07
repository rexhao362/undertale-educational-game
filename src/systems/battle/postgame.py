import src.systems.state as state
import pygame

class PostGame(state.State):
    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.sm.user.update_user()


    def draw(self, screen, time_delta):
        if self.sm.game_over == False:
            if self.sm.stage > 5:
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
                    self.sm.set_state('tilemap')

            elif event.type == pygame.KEYDOWN:
                if self.sm.stage == 5:
                    exit()
                else:
                    self.sm.set_state('tilemap')
