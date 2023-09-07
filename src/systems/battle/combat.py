from src.systems.battle.enemy import create_enemy
import src.settings as s
import pygame
import pygame_gui
import logging
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
        self.buttons_normal = create_buttons(self.scene['normal'])
        self.buttons_act = create_buttons(self.scene['act'], 75)
        self.buttons_items = create_buttons(self.scene['items'], 75)
        disable_hide_buttons(self.buttons_act)
        disable_hide_buttons(self.buttons_items)
        self.message_queue = []
        self.text_box = None

    def victory(self):
        if not self.enemy.is_alive():
            self.player.post_game_heal()
            self.sm.set_state('postgame')

    def game_over(self):
        if not self.player.is_alive():
            if self.sm.cont_game == True:
                self.cont_game = False
                self.reward = self.player.post_game_heal
                self.player.alive = True
                self.sm.set_state('quiz')
            else:
                self.sm.game_over = True
                self.sm.set_state('postgame')

    def turn_combat(self):
        if self.turn == 'player':
            self.victory()
            self.player.affliction()
            self.player.remove_block()
            self.set_text_box(self.player.text_entry)
        else:
            disable_hide_buttons(self.buttons_normal)
            self.game_over()
            self.enemy.affliction()
            self.enemy.attack(self.player)
            self.set_text_box(self.enemy.text_entry)
            self.num_turns += 1
            enable_show_buttons(self.buttons_normal)
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
                self.create_text_box()

            elif event.type == pygame.KEYDOWN:
                pass

            if self.turn == 'player':
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttons_normal['fight']:
                        self.player.attack(self.enemy)
                        self.player.draw_attack(
                            self.sm.screen, s.settings.time_delta)
                        self.turn = 'enemy'
                    elif event.ui_element == self.buttons_normal['act']:
                        enable_show_buttons(self.buttons_act)
                    elif event.ui_element == self.buttons_normal['items']:
                        enable_show_buttons(self.buttons_items)
                    elif event.ui_element == self.buttons_normal['block']:
                        self.player.set_block()
                        self.turn = 'enemy'
                    elif event.ui_element == self.buttons_act['poison']:
                        self.reward = self.enemy.set_status('poison')
                        disable_hide_buttons(self.buttons_act)
                        self.sm.set_state('quiz')

            manager.process_events(event)

    def update(self):
        if self.message_queue_empty():
            self.turn_combat()
            # self.turn = 'player' if self.turn == 'enemy' else 'enemy'

    def store_state(self):
        self.sm.previous_state = {
            'name': 'combat',
            'enemy': self.enemy,
            'turn': self.turn,
            'num_turns': self.num_turns,
            'reward': self.reward
        }

    def create_text_box(self):
        if len(self.message_queue) > 0:
            self.text_box = pygame_gui.elements.ui_text_box.UITextBox(
                html_text=self.message_queue.pop(0), relative_rect=pygame.Rect(220, 600, 540, 100))
            self.text_box.set_active_effect('TEXT_EFFECT_TYPING_APPEAR')

    def set_text_box(self, text):
        if text != None:
            self.message_queue.append(text)
            text = None

    def message_queue_empty(self):
        return len(self.message_queue) == 0


def create_buttons(buttons_list, spacing=0):
    # Constants
    RECT_WIDTH = 100
    RECT_HEIGHT = 50
    RECT_DISTANCE = 50

    num_buttons = len(buttons_list)
    # Calculate the x-coordinate for the first rectangle
    total_rect_width = num_buttons * RECT_WIDTH + \
        (num_buttons-1) * RECT_DISTANCE
    left = (s.screen_values[0] - total_rect_width) // 2
    top = (2 * s.screen_values[1]) // 3 + spacing

    buttons_dict = {}
    # Draw the four rectangles
    for button in buttons_list:
        rect = pygame.Rect((left, top), (RECT_WIDTH, RECT_HEIGHT))

        buttons_dict[button] = pygame_gui.elements.UIButton(
            relative_rect=rect,
            text=button)

        left += RECT_WIDTH + RECT_DISTANCE

    return buttons_dict


def disable_hide_buttons(buttons):
    for button in buttons.values():
        button.disable()
        button.hide()


def enable_show_buttons(buttons):
    for button in buttons.values():
        button.enable()
        button.show()
