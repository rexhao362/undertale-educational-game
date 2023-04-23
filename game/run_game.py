import pygame

def start_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update Pygame display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()