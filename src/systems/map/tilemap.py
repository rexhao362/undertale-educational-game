from systems.state import State
from src.systems.map.sprite_sheet import SpriteSheet
from pytmx.util_pygame import load_pygame
import pygame
from pygame.sprite import Group

class TileMap(State):
    def __init__(self, state_manager, **kwargs):
        super().__init__(state_manager)
        self.stage = self.sm.stage
        self.filename = f'assets/tilemaps/level_{self.stage}.tmx'
        self.map = load_pygame(self.filename)
        self.current_sprite = frisk_walk['up']
        
    def draw_frisk(self, screen, time_delta):
        sprites = Group(self.current_sprite)
        self.current_sprite.animate(time_delta)
        sprites.draw(screen)

    def draw_tilemap(self, screen):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile != None:
                    screen.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))

    def draw(self, screen, time_delta):
        self.draw_tilemap(screen)
        self.draw_frisk(screen, time_delta)

    def update(self):
        pass

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_sprite = frisk_walk['up']
                    elif event.key == pygame.K_DOWN:
                        self.current_sprite = frisk_walk['down']
                    elif event.key == pygame.K_LEFT:
                        self.current_sprite = frisk_walk['left']
                    elif event.key == pygame.K_RIGHT:
                        self.current_sprite = frisk_walk['right']

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

frisk_walk = {
        'up': SpriteSheet('up', 19, 29, 5, 4),
        'left': SpriteSheet('left', 17, 29, 5, 2),
        'right': SpriteSheet('right', 17, 29, 5, 2),
        'down': SpriteSheet('down', 17, 29, 5, 4)
    }