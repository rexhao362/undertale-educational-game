import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
BOX_SIZE = 50
BG_COLOR = (255, 255, 255)
INPUT_BOX_COLOR = (150, 150, 150)
SELECTED_BOX_COLOR = (0, 255, 0)
OUTLINE_COLOR = (0, 0, 0)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 24

# Create the screen
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Input Text Boxes")

# Font for text rendering
font = pygame.font.Font(None, FONT_SIZE)

# Boxes
characters = ['*', 'a', 'b', '*', 'c', '*', 'd', 'e', '*', 'f']

# Input boxes
input_boxes = ['' if char == '*' else char for char in characters]
num_boxes = len(input_boxes)
box_height = 50
box_spacing = 20
active_box = 0  # Start with the first box selected

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            box_x = (WIDTH - (num_boxes * (BOX_SIZE + box_spacing))) // 2
            for i in range(num_boxes):
                box_rect = pygame.Rect(box_x, (HEIGHT - box_height) // 2, BOX_SIZE, box_height)
                if box_rect.collidepoint(mouse_x, mouse_y):
                    active_box = i
                box_x += BOX_SIZE + box_spacing
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                active_box = (active_box - 1) % num_boxes
            elif event.key == pygame.K_RIGHT:
                active_box = (active_box + 1) % num_boxes
            elif event.key == pygame.K_BACKSPACE:
                if characters[active_box] == '*':
                    input_boxes[active_box] = ''
            else:
                if characters[active_box] == '*' and len(event.unicode) == 1:
                    input_boxes[active_box] = event.unicode
                    active_box = (active_box + 1) % num_boxes

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw boxes
    box_x = (WIDTH - (num_boxes * (BOX_SIZE + box_spacing))) // 2
    box_y = (HEIGHT - box_height) // 2

    for i, text in enumerate(input_boxes):
        box_rect = pygame.Rect(box_x, box_y, BOX_SIZE, box_height)
        if characters[i] == '*':
            box_color = SELECTED_BOX_COLOR if i == active_box else INPUT_BOX_COLOR
            pygame.draw.rect(screen, box_color, box_rect)
            pygame.draw.rect(screen, OUTLINE_COLOR, box_rect, 2)  # Black outline
            text_surface = font.render(text, True, FONT_COLOR)
            text_rect = text_surface.get_rect(center=box_rect.center)
            screen.blit(text_surface, text_rect.topleft)
        else:
            char_surface = font.render(text, True, FONT_COLOR)
            char_rect = char_surface.get_rect(center=box_rect.center)
            screen.blit(char_surface, char_rect.topleft)

        box_x += BOX_SIZE + box_spacing

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
