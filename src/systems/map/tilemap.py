from systems.battle.items import create_item
from systems.state import State
from pytmx.util_pygame import load_pygame
import pygame
from src.systems.map.tilemap_helpers import frisk_walk
from src.systems.map.tilemap_helpers import gen_random_tiles
from src.systems.map.tilemap_helpers import convert_pixels_to_tile


class TileMap(State):
    def __init__(self, state_manager, **kwargs):
        super().__init__(state_manager)
        self.stage = self.sm.stage
        self.filename = f'assets/tilemaps/level_{self.stage}.tmx'
        self.map = load_pygame(self.filename)
        self.start_pos = kwargs.get('start_pos', (450, 650))
        self.current_sprite = frisk_walk('up', self.start_pos)
        self.steps = 5
        self.combat_tile = (16, 5)
        self.item_tiles = gen_random_tiles(10, 30, 24)
        self.reward = kwargs.get('reward', None)
        self.target = kwargs.get('target', None)

    def draw_frisk(self, screen, time_delta):
        self.current_sprite.animate(time_delta)
        screen.blit(self.current_sprite.image, self.current_sprite.rect)

    def draw_tilemap(self, screen):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile is not None:
                    screen.blit(tile, (x * self.map.tilewidth,
                                y * self.map.tileheight))

    def draw(self, screen, time_delta):
        self.draw_tilemap(screen)
        self.draw_frisk(screen, time_delta)

    def update(self):
        self.current_sprite.update_position()
        self.encounter()
        self.buried_treasure()

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
        (x, y) = (16, 5)
        if 14 * 32 < self.current_sprite.rect.x < 18 * 32:
            if 3 * 32 < self.current_sprite.rect.y < 7 * 32:
                self.sm.set_state('combat')

    def buried_treasure(self):
        (x, y) = (self.current_sprite.rect.x, self.current_sprite.rect.y)
        pos = convert_pixels_to_tile((x, y))
        if pos in self.item_tiles:
            self.item_tiles.remove(pos)
            self.reward = self.sm.inventory.add_item
            self.target = create_item()
            self.sm.set_state('quiz')

    def store_state(self):
        self.sm.previous_state = {
            'name': 'tilemap',
            'start_pos': self.current_sprite.rect,
            'reward': self.reward,
            'target': self.target
        }
