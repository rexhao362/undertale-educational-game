import pygame
from src.settings import settings
import src.menus.main_menu as m
from importlib import import_module


pygame.init()
screen = pygame.display.set_mode((
    settings.screen_width,
    settings.screen_height
))
pygame.display.set_caption('Game')


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
 
#  mouse = pygame.mouse.get_pos()

    # # if mouse is hovered on a button it
    # # changes to lighter shade
    #     if settings.screen_width/2 <= mouse[0] <= settings.screen_width/2+140 and settings.screen_height/2 <= mouse[1] <= settings.screen_height/2+40:
    #         pygame.draw.rect(screen, "white", [
    #                          settings.screen_width/2, settings.screen_height/2, 140, 40])