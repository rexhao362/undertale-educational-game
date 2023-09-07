from random import randint
from systems.battle.items import create_item
from systems.state import State
from src.systems.map.frisk_walking import FriskWalk
from pytmx.util_pygame import load_pygame
import pygame


class TileMap(State):
    def __init__(self, state_manager, **kwargs):
        super().__init__(state_manager)
        self.stage = self.sm.stage
        self.filename = f'assets/tilemaps/level_{self.stage}.tmx'
        self.map = load_pygame(self.filename)
        self.start_pos = (450, 650)
        self.current_sprite = frisk_walk('up', self.start_pos)
        self.steps = 5
        self.combat_tile = (16, 5)
        self.item_tile_1 = random_tile()
        self.item_tile_2 = random_tile()

    def draw_frisk(self, screen, time_delta):
        self.current_sprite.animate(time_delta)
        screen.blit(self.current_sprite.image, self.current_sprite.rect)

    def draw_tilemap(self, screen):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile != None:
                    screen.blit(tile, (x * self.map.tilewidth,
                                y * self.map.tileheight))

    def draw(self, screen, time_delta):
        self.draw_tilemap(screen)
        self.draw_frisk(screen, time_delta)

    def update(self):
        self.current_sprite.update_position()
        self.encounter()

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.current_sprite = frisk_walk(
                        'up', self.current_sprite.rect)
                    self.current_sprite.move(0, -self.steps)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.current_sprite = frisk_walk(
                        'down', self.current_sprite.rect)
                    self.current_sprite.move(0, self.steps)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.current_sprite = frisk_walk(
                        'left', self.current_sprite.rect)
                    self.current_sprite.move(-self.steps, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.current_sprite = frisk_walk(
                        'right', self.current_sprite.rect)
                    self.current_sprite.move(
                        self.steps, 0)

            elif event.type == pygame.KEYUP:
                self.current_sprite.move(0, 0)

            manager.process_events(event)

    def encounter(self):
        tile = (16, 5)
        if 14 * 32 < self.current_sprite.rect.x  < 18 *32:
            if 3 * 32 < self.current_sprite.rect.y  < 7 *32:
            
                self.sm.set_state('combat')

    def buried_treasure(self):
        if self.current_sprite.rect in [self.item_tile_1, self.item_tile_2]:
            self.reward = create_item
            self.sm.set_state('quiz')

    def store_state(self):
        self.sm.previous_state = {
            'name': 'tilemap',
            'start_pos': self.current_sprite.rect
        }


def frisk_walk(direction, pos):
    walk = {
        'up': FriskWalk('up', 19, 4, pos),
        'left': FriskWalk('left', 17, 2, pos),
        'right': FriskWalk('right', 17, 2, pos),
        'down': FriskWalk('down', 19, 4, pos)
    }
    return walk[direction]


def convert_tile_to_pixels(x, y):
    tile_width = 32
    tile_height = 32
    return (
        x * tile_width,
        y * tile_height
    )


def random_tile():
    x = randint(1, 30)
    y = randint(1, 24)
    return convert_tile_to_pixels(x, y)
