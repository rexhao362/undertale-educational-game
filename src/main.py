import pygame
from src.settings import settings
# from src.menus.main_menu import main_menu
from importlib import import_module

pygame.init()
screen = pygame.display.set_mode((
    settings.screen_width,
    settings.screen_height
))
clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption('Game')


def main():
    mod = import_module('src.menus.main_menu')
    main_menu = mod.main_menu

    # Main game loop
    running = True
    while running:
        clock.tick(fps)
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

        mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
        if settings.screen_width/2 <= mouse[0] <= settings.screen_width/2+140 and settings.screen_height/2 <= mouse[1] <= settings.screen_height/2+40:
            pygame.draw.rect(screen, "white", [
                             settings.screen_width/2, settings.screen_height/2, 140, 40])
            
        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
