from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.main import screen
import src.menus.main_menu as m
from settings import settings

current_user = ['player']
current_subject = ['maths']


class Game:
    def __init__(self, screen, subject, user):
        self.screen = screen
        self.user = user
        self.player = Player(self.user)
        self.subject = subject
        self.stage = 0

    def next_stage(self):
        self.stage += 1
        return Stage(self.screen, self.player, self.stage)

    def set_subject(self, subject):
        self.subject = subject


def start_game():
    game = Game(screen, 'maths', current_user[0])
    m.main_menu.disable()
    stage = game.next_stage()
    stage.turn_combat()
    running = True
    while running:
        settings.clock.tick(settings.fps)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Event handling for a range of different key presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    m.main_menu.enable()
                    # Quit this function, then skip to loop of main-menu on line 221
                    return

        stage.draw()
        pygame.display.flip()
