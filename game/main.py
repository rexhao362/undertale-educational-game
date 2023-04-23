import pygame
from settings import Settings
from menus.main_menu import main_menu

class Game:
    def __init__(self):
        settings = Settings()
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((
            self.screen_width,
            self.screen_height
        ))
        pygame.display.set_caption('')
        # Main game loop
        running = True
        current_menu = main_menu
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Draw menu on screen
            current_menu.mainloop(screen)
            
            # Update Pygame display
            pygame.display.update()

        # Quit Pygame
        pygame.quit()

game = Game()
game.main()
