import pygame
from settings import settings
from importlib import import_module

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        self.screen = pygame.display.set_mode((
            self.screen_width,
            self.screen_height
        ))
        pygame.display.set_caption('Game')

    def main(self):
        mod = import_module('game.menus.main_menu')
        main_menu = mod.main_menu
        
        # Main game loop
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            if main_menu.is_enabled():
                main_menu.update(events)
                main_menu.draw(self.screen)

            pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.main()
