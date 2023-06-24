from pygame.sprite import Sprite
import pygame


class Units(Sprite):
    def __init__(self, health, attack, defence):
        super.__init__()
        self.total_health = health
        self.current_health = health
        self.attack = attack
        self.defence = defence
        self.alive = True
        # self.image
        # self.rect = self.image.get_rect()
        # self.rect.center = (left, top)

    def attack_action(self, target):
        target.current_health -= self.attack
        if target.current_health <= 0:
            target.alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_alive(self):
        return self.alive


class HealthBar(Sprite):
    def __init__(self, left, top, width, height, total_health):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.current_health = total_health
        self.total_health = total_health

    def draw(self, surface):
        ratio = self.current_health / self.total_health
        pygame.draw.rect(surface, "red", (self.left,
                         self.top, self.width, self.height))
        pygame.draw.rect(surface, "green", (self.left,
                         self.top, self.width * ratio, self.height))
