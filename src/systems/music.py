from pygame.mixer import music

def play_music(song):
    music.unload()
    music.load(f'assets/music/{song}.ogg')
    music.play(loops=-1, fade_ms=3000)