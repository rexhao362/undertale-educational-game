import pygame


def draw_text(screen, text, font, size, left, top):
    img = font.render(text, True, "white")
    screen.blit(img, (left, top))
