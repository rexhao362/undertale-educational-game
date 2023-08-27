import pygame
from src.settings import settings, screen
import src.menus.main_menu as m


pygame.init()



def main():
    # Main game loop
    running = True
    while running:
        settings.clock.tick(settings.fps)
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

        if m.main_menu.is_enabled():
            m.main_menu.update(events)
            m.main_menu.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

