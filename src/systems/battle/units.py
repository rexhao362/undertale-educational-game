from pygame.sprite import Sprite
import pygame
from random import randint

from systems.sprite_sheet import SpriteSheet


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
        self.text_entry = []
        self.hit = {
            'damage': 0,
            'move': None
        }

    def attack(self, target):
        critical_chance = randint(1, 100)
        critical_hit = 0.5 * self.attack_power if critical_chance > 95 else 0
        self.hit['damage'] = self.attack_power * \
            randint(70, 130) // 100 + critical_hit - target.defence

        if critical_hit > 0:
            text = f'{target.name} was critically hit for {self.hit["damage"]}'
            self.text_entry.append(text)
        else:
            text = f'{self.name} has attacked {target.name} for {self.hit["damage"]}'
            self.text_entry.append(text)

        self.hit['move'] = set_animation('fight')

    def fire_spell(self, target, success=None):
        self.hit["damage"] = self.attack_power * 2 * \
randint(50, 110) // 100 - target.defence
        if hasattr(self, 'mana'):
            self.mana -= 1
            if not success:
                self.hit['damage'] // 2
        text = f'{self.name} has hit {target.name} with Fire for {self.hit["damage"]}'
        self.text_entry.append(text)

        self.hit['move'] = set_animation('fire')

    def damage_application(self, target):
        target.current_health = max(
            0, target.current_health - self.hit["damage"])
        if target.current_health <= 0:
            target.alive = False

    def thunder_spell(self, target, success=None):
        self.hit["damage"] = self.attack_power * 1.5 * randint(70, 130) // 100
        if hasattr(self, 'mana'):
            self.mana -= 1
            if not success:
                self.hit['damage'] // 2
        text = f'{self.name} has hit {target.name} with Thunder for {self.hit["damage"]}'
        self.text_entry.append(text)

        self.hit['move'] = set_animation('thunder')

    def poison_spell(self, target):
        if hasattr(self, 'mana'):
            self.mana -= 1
        target.status = 'poison'
        self.hit['move'] = set_animation('poison')
        text = f'{target.name} has been poisoned'
        self.text_entry.append(text)

    def draw(self, screen, time_delta):
        pass

    def is_alive(self):
        return self.alive

    def modify_attribute(self, attribute, effect):
        if attribute == 'health':
            self.current_health = min(
                self.health_capacity, self.current_health + effect)
        elif attribute in ['attack_power', 'defence']:
            self[attribute] = max(0, self[attribute] + effect)

    def affliction(self):
        if self.status == 'poison':
            damage = randint(2, 9)
            text = f"Poison has done {damage} to {self.name}'s health"
            self.text_entry.append(text)

            self.current_health = max(
                0, self.current_health - damage)
            if self.current_health <= 0:
                self.alive = False

    def draw_status(self, x, y, screen):
        text = f'{self.name}    {self.current_health}/{self.health_capacity}'
        font = pygame.font.Font('data/fonts/league_spartan.ttf', 20)
        player = font.render(text, True, 'white')
        screen.blit(player, (x, y))


def set_animation(move):
    animations = {
        'fight': SpriteSheet('fight', 100, 100, 0, 7),
        'poison': SpriteSheet('poison', 99.625, 100, 0, 15),
        'fire': SpriteSheet('fire', 100, 100, 0, 18),
        'thunder': SpriteSheet('thunder', 100, 100, 0, 13)
    }
    return animations[move]


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
