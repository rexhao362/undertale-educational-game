from src.systems.battle.player import Player
from src.systems.battle.stage import Stage
import pygame
from src.main import screen
from src.menus.main_menu import main_menu

current_user = ['player']


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
    main_menu.disable()
    running = True
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 221
                    return

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)
        stage = game.next_stage()
        stage.turn_combat()
        