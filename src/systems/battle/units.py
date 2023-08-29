from pygame.sprite import Sprite
import pygame


class Units(Sprite):
    def __init__(self, health, attack, defence):
        super().__init__()
        self.total_health = health
        self.current_health = health
        self.attack_power = attack
        self.defence = defence
        self.alive = True
        self.healthbar = HealthBar()
        # self.image
        # self.rect = self.image.get_rect()
        # self.rect.center = (left, top)

    def attack(self, target):
        target.current_health = max(
            0, target.current_health - self.attack_power)
        if target.current_health <= 0:
            target.alive = False

    def draw(self, screen, time_delta):
        screen.blit(self.image, self.rect)

    def is_alive(self):
        return self.alive

    def modify_attribute(self, attribute, effect):
        if attribute == 'health':
            self.current_health = min(
                self.total_health, self.current_health + self.effect)
        elif attribute in ['attack_power', 'defence']:
            self[attribute] = max(0, self[attribute] + effect)


class HealthBar():
    def __init__(self, left, top, width, height, total_health):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.total_health = total_health

    def draw(self, screen, current_health):
        ratio = current_health / self.total_health
        pygame.draw.rect(screen, 'red', (self.left,
                         self.top, self.width, self.height))
        pygame.draw.rect(screen, 'green', (self.left,
                         self.top, self.width * ratio, self.height))
