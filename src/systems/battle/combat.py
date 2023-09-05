from src.systems.battle.enemy import create_enemy
import src.settings as s
import pygame
import pygame_gui
import logging
from time import sleep
import src.systems.state as state

logger = logging.getLogger()
logging.basicConfig()


class Combat(state.State):
    def __init__(self, state_manager, **kwargs):
        super().__init__(state_manager)
        self.player = self.sm.player
        self.enemy = kwargs.get('enemy', create_enemy())
        self.turn = kwargs.get('turn', 'player')
        self.num_turns = kwargs.get('num_turns', 0)
        self.scene = {'normal': ['fight', 'act', 'items', 'block'],
                      'act': ['poison'],
                      'items': [item.name for item in self.sm.inventory.items]}
        self.background = pygame.image.load(
            'assets/pictures/backgrounds/boss_battle_bg.png')
        self.buttons = create_buttons(self.scene['normal'])
        self.display_buttons = False
        self.text = ''
        self.text_changed = False
        self.text_box = None

    def victory(self):
        if not self.enemy.is_alive():
            self.player.post_game_heal()
            self.sm.set_state('postgame')

    def game_over(self):
        if not self.player.is_alive():
            if self.sm.cont_game() == True:
                self.reward = self.player.post_game_heal
                self.store_state()
                self.sm.set_state('quiz')
                self.player.alive = True
            else:
                self.sm.game_over = True
                self.sm.set_state('postgame')


    def turn_combat(self):
        if self.turn == 'player':
            ui_buttons_on(self.buttons)
            self.victory()
            self.player.affliction()
            self.player.remove_block()
            self.set_text_box(self.player.text)
            self.create_text_box()
        else:
            ui_buttons_off(self.buttons)
            self.game_over()
            self.enemy.affliction()
            self.enemy.attack(self.player)
            self.set_text_box(self.enemy.text)
            self.create_text_box()
            self.num_turns += 1
            self.turn = 'player'

    def draw(self, screen, time_delta):
        screen.fill('black')
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        self.enemy.draw(screen)

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
                    self.turn = 'enemy'
                elif event.ui_element == self.buttons['act']:
                    manager.clear_and_reset()
                    self.buttons = create_buttons(self.scene['act'])
                elif event.ui_element == self.buttons['items']:
                    pass
                elif event.ui_element == self.buttons['block']:
                    self.player.set_block()
                    self.turn = 'enemy'

            manager.process_events(event)

    def update(self):
        self.turn_combat()

    def store_state(self):
        self.sm.previous_state = {
            'name': 'combat',
            'enemy': self.enemy,
            'turn': self.turn,
            'num_turns': self.num_turns,
            'reward': self.reward
        }

    def create_text_box(self):
        if self.text_changed == True:
            text_box = pygame_gui.elements.ui_text_box.UITextBox(
                html_text=self.text, relative_rect=pygame.Rect(200, 600, 400, 200))
            text_box.set_active_effect('TEXT_EFFECT_TYPING_APPEAR')
            self.text_changed = False

    def set_text_box(self, text):
        self.text = text
        self.text_changed = True

    def buttons_on(self):
        if self.display_buttons == True:
            self.buttons = create_buttons(self.scene['normal'])
            self.display_buttons = False

    def buttons_off(self):
        self.buttons = None
        self.display_buttons = True


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
    top = (2 * s.screen_values[1]) // 3

    buttons_dict = {}
    # Draw the four rectangles
    for button in buttons_list:
        rect = pygame.Rect((left, top), (RECT_WIDTH, RECT_HEIGHT))

        buttons_dict[button] = pygame_gui.elements.UIButton(
            relative_rect=rect,
            text=button)

        left += RECT_WIDTH + RECT_DISTANCE

    return buttons_dict


def ui_buttons_off(buttons):
    for button in buttons.values():
        button.disable()
def ui_buttons_on(buttons):
    for button in buttons.values():
        button.enable()