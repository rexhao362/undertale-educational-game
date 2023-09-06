from systems.state import State
from src.systems.map.frisk_walking import FriskWalk
from pytmx.util_pygame import load_pygame
import pygame
from pygame.sprite import Group


class TileMap(State):
    def __init__(self, state_manager, **kwargs):
        super().__init__(state_manager)
        self.stage = self.sm.stage
        self.filename = f'assets/tilemaps/level_{self.stage}.tmx'
        self.map = load_pygame(self.filename)
        self.current_sprite = self.frisk_walk('up', (450, 650))
        self.steps = 5

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

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.current_sprite = self.frisk_walk(
                        'up', self.current_sprite.rect)
                    self.current_sprite.move(0, -self.steps)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.current_sprite = self.frisk_walk(
                        'down', self.current_sprite.rect)
                    self.current_sprite.move(0, self.steps)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.current_sprite = self.frisk_walk(
                        'left', self.current_sprite.rect)
                    self.current_sprite.move(-self.steps, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.current_sprite = self.frisk_walk('right', self.current_sprite.rect)
                    self.current_sprite.move(
                        self.steps, 0)

            elif event.type == pygame.KEYUP:
                self.current_sprite.move(0, 0)

            manager.process_events(event)

    def reward_check(self):
        if self.reward != None:
            if self.sm.get_success():
                self.reward()
            elif not self.sm.get_success():
                pass
            self.reward = None
            self.sm.set_success(None)

    def success_check(self):
        if self.sm.get_success():
            pass
            # self.sm.set_success(False)

    def store_state(self):
        pass

    def frisk_walk(self, direction, pos):
        walk = {
            'up': FriskWalk('up', 19, 4, pos),
            'left': FriskWalk('left', 17, 2, pos),
            'right': FriskWalk('right', 17, 2, pos),
            'down': FriskWalk('down', 19, 4, pos)
        }
        return walk[direction]
