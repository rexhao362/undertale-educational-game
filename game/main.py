import pygame
pygame.init()
from game.settings import Settings
from game.menus.main_menu import main_menu


class Game:
    def __init__(self):
        settings = Settings()
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

    def main(self):
        screen = pygame.display.set_mode((
            self.screen_width,
            self.screen_height
        ))
        # Main game loop
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if main_menu.is_enabled():
                main_menu.update(events)
                main_menu.draw(screen)
        
            pygame.display.update()
        # pygame.display.set_caption('')


game = Game()
game.main()
