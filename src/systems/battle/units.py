from pygame.sprite import Sprite
import pygame
from random import randint


class Units(Sprite):
    def __init__(self, name, health, attack, defence):
        super().__init__()
        self.name = name
        self.health_capacity = health
        self.current_health = health
        self.attack_power = attack
        self.defence = defence
        self.alive = True
        self.healthbar = None
        self.status = None
        self.text = ''

    def attack(self, target):
        critical_chance = randint(1, 100)
        critical_hit = 0.5 * self.attack_power if critical_chance > 95 else 0
        damage = self.attack_power * randint(70, 130) // 100 + critical_hit
        target.current_health = max(
            0, target.current_health - damage)
        if target.current_health <= 0:
            target.alive = False

        if critical_hit > 0:
            self.text = f'{target.name} was critically hit for {damage}'
        else:
            self.text = f'{self.name} has attacked {target.name} for {damage}'

    def draw(self, screen, time_delta):
        pass

    def is_alive(self):
        return self.alive

    def modify_attribute(self, attribute, effect):
        if attribute == 'health':
            self.current_health = min(
                self.health_capacity, self.current_health + self.effect)
        elif attribute in ['attack_power', 'defence']:
            self[attribute] = max(0, self[attribute] + effect)

    def set_status(self, affliction):
        if affliction in ['poison', 'block']:
            self.status = affliction

    def affliction(self):
        if self.status == 'poison':
            damage = random.randint(1, 7)
            self.current_health -= damage
            self.text += f"Poison has done {damage} to {self.name}'s health"


class HealthBar():
    def __init__(self, left, top, width, height, health_capacity):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.health_capacity = health_capacity

    def draw(self, screen, current_health):
        ratio = current_health / self.health_capacity
        pygame.draw.rect(screen, 'red', (self.left,
                         self.top, self.width, self.height))
        pygame.draw.rect(screen, 'green', (self.left,
                         self.top, self.width * ratio, self.height))
