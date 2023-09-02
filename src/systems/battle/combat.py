from src.systems.battle.enemy import create_enemy
import src.settings as s
import pygame
import pygame_gui
import logging

import src.systems.state as state

logger = logging.getLogger()
logging.basicConfig()


class Combat(state.State):
    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.player = self.sm.player
        self.stage = self.sm.stage
        self.enemy = create_enemy()
        self.turn = 'player'
        self.num_turns = 1
        self.scene = {'normal': ['fight', 'act', 'items'],
                      'act': ['poison'],
                      'items': []}
        self.bg_image = pygame.image.load(
            'assets/pictures/backgrounds/boss_battle_bg.png')
        self.background = pygame.transform.scale(
            self.bg_image, s.screen_values)
        self.buttons = create_buttons(self.scene['normal'])

    def victory(self, screen):
        if not self.enemy.is_alive():
            screen.fill('black')
            # victory_img = 'assets/pictures/victory.png'
            # victory_bg = pygame.image.load(victory_img)
            # screen.blit(victory_bg, (0, 0))
            self.sm.user.update_user()
            self.player.post_game_heal()
            # self.sm.next_state()
            self.game_won()

    def game_over(self, screen):
        if not self.player.is_alive():
            screen.fill('black')
            self.sm.user.update_user()
            # defeat_img = 'assets/pictures/game_over.png'
            # defeat_bg = pygame.image.load(defeat_img)
            # screen.blit(defeat_bg, (0, 0))

    def game_won(self):
        if self.stage == 5:
            pygame.quit()

    def turn_combat(self):
        if self.turn == 'player':
            # self.victory()
            pass
        else:
            self.enemy.attack(self.player)
            self.turn = 'player'
            # self.player.acting = True

    def draw(self, screen, time_delta,):
        screen.fill('black')
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        self.enemy.draw(screen)
        if self.turn == 'player':
            self.victory(screen)
        else:
            self.game_over(screen)
            self.enemy.draw_attack(screen, time_delta)




    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                pass

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.buttons['fight']:
                    self.player.attack(self.enemy)
                elif event.ui_element == self.buttons['act']:
                    self.buttons = create_buttons(self.scene['act'])
                elif event.ui_element == self.buttons['items']:
                    self.sm.next_stage('inventory')
                self.turn = 'enemy'

            manager.process_events(event)

    def update(self):
        self.turn_combat()

def create_buttons(buttons_list):
    # Constants
    RECT_WIDTH = 100
    RECT_HEIGHT = 50
    RECT_DISTANCE = 50

    num_buttons = len(buttons_list)
    # Calculate the x-coordinate for the first rectangle
    total_rect_width = num_buttons * RECT_WIDTH + \
        (num_buttons-1) * RECT_DISTANCE
    left = (s.screen_values[0] - total_rect_width) // 2
    top = (3 * s.screen_values[1]) // 4

    buttons_dict = {}
    # Draw the four rectangles
    for button in buttons_list:
        rect = pygame.Rect((left, top), (RECT_WIDTH, RECT_HEIGHT))

        buttons_dict[button] = pygame_gui.elements.UIButton(
            relative_rect=rect,
            text=button)

        left += RECT_WIDTH + RECT_DISTANCE
    
    return buttons_dict
