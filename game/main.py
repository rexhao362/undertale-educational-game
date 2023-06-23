import pygame
from settings import settings
from importlib import import_module


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((
            settings.screen_width,
            settings.screen_height
        ))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.stage = 0
        pygame.display.set_caption('Game')

    def main(self):
        mod = import_module('game.menus.main_menu')
        main_menu = mod.main_menu

        # Main game loop
        running = True
        while running:
            self.clock.tick(self.fps)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            # Event handling for a range of different key presses
                elif event.type == pygame.KEYDOWN:
                    pass

            if main_menu.is_enabled():
                main_menu.update(events)
                main_menu.draw(self.screen)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.main()
