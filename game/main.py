import pygame
from settings import settings
# from menus.main_menu import main_menu
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        self.screen = pygame.display.set_mode((
            self.screen_width,
            self.screen_height
        ))

    def main(self):
        module = __import__('game.menus.main_menu')
        main_menu = getattr(module, 'main_menu')
        # Main game loop
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if main_menu.is_enabled():
                main_menu.update(events)
                main_menu.draw(self.screen)

            pygame.display.update()
            pygame.display.set_caption('')



if __name__ == '__main__':
    game = Game()
    game.main()
