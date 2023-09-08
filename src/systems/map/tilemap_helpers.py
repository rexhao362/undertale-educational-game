from random import randint
from src.systems.map.frisk_walking import FriskWalk


def frisk_walk(direction, pos):
    walk = {
        'up': FriskWalk('up', 19, 4, pos),
        'left': FriskWalk('left', 17, 2, pos),
        'right': FriskWalk('right', 17, 2, pos),
        'down': FriskWalk('down', 19, 4, pos)
    }
    return walk[direction]


def convert_tile_to_pixels(tile):
    tile_width = 32
    tile_height = 32
    return (
        tile[0] * tile_width,
        tile[1] * tile_height
    )


def convert_pixels_to_tile(pixels):
    tile_width = 32
    tile_height = 32
    return (
        pixels[0] // tile_width,
        pixels[1] // tile_height
    )


def gen_random_tiles(num_tiles, map_width, map_height):
    unique_tiles = set()
    random_tiles = []

    while len(unique_tiles) < num_tiles:
        # Generate random tile coordinates (x, y)
        tile = (randint(1, map_width), randint(1, map_height))
        # Ensure the generated tile is unique
        if tile not in unique_tiles:
            unique_tiles.add(tile)
            random_tiles.append(tile)

    # Now, convert each random tile coordinate to pixel coordinates


    return random_tiles
