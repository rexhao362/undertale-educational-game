import pygame
from pygame.sprite import Sprite, Group


class SpriteSheet(Sprite):
    def __init__(self, name, width, height, spacing, num_sprites):
        super().__init__()
        self.sheet = pygame.image.load(
            f'assets/pictures/spritesheets/{name}.png')
        self.width = width
        self.height = height
        self.spacing = spacing
        self.num_sprites = num_sprites
        self.sprites = self.load_sprites()
        self.time = 0
        self.animation_speed = 0.4
        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.fin = False

    def get_image(self, x):
        rect = pygame.Rect(x, 0, self.width, self.height)
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image

    def load_sprites(self):
        x = 0
        frames = []
        for i in range(self.num_sprites):
            frames.append(self.get_image(x))
            x += self.width + self.spacing
        return frames

    def animate(self, time_delta):
        # Calculate elapsed time
        self.time += time_delta

        if self.time >= self.animation_speed:
            # Update sprite index
            self.index = (self.index + 1) % len(self.sprites)
            self.image = self.sprites[self.index]
            self.time = 0

    def play(self, screen, time_delta, rect):
        self.animate(time_delta)
        self.rect.center = rect
        screen.blit(self.image, self.rect)

        if self.index >= self.num_sprites - 1:
            self.fin = True


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    frisk = SpriteSheet('up', 19, 29, 5, 4)
    clock = pygame.time.Clock()
    all_sprites = Group(frisk)
    while True:
        time_delta = clock.tick(60)/1000.0
        frisk.animate(time_delta)
        all_sprites.draw(screen)
        pygame.display.flip()
