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
        self.phase = kwargs.get('phase', 'player')
        self.scene = {'normal': ['fight', 'act', 'items', 'block'],
                      'act': ['poison', 'fire', 'thunder'],
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
        self.waiting = kwargs.get('waiting', False)
        self.damage_phase = kwargs.get('damage_phase', False)
        self.reward = kwargs.get('reward', None)
        self.target = kwargs.get('target', None)

    def victory(self):
        if not self.enemy.is_alive():
            self.player.post_game_heal()
            if self.waiting:
                text = ["Congratulations, You've won the round!"]
                self.set_text_box(text)
            else:
                self.sm.set_state('postgame')

    def game_over(self):
        if not self.player.is_alive():
            if self.sm.cont_game == True:
                if self.waiting:
                    text = [
                        "Unlucky, You have one more chance to come back from this"]
                    self.set_text_box(text)

                self.cont_game = False
                self.reward = self.player.post_game_heal
                self.player.alive = True
                self.sm.set_state('quiz')
            else:
                if self.waiting:
                    text = ["Unfortunate. Try again"]
                    self.set_text_box(text)
                self.sm.game_over = True
                self.sm.set_state('postgame')

    def turn_combat(self):
        if self.phase == 'player':
            self.player.remove_block()

        elif self.phase == 'enemy':
            disable_hide_buttons(self.buttons_normal)
            self.enemy.hit_player(self.player)
            enable_show_buttons(self.buttons_normal)

    def apply_damage(self, screen, time_delta):
        if self.waiting:
            if self.damage_phase:
                if self.phase == 'player':
                    self.reward_check()
                    self.player.affliction()
                    self.player.draw_attack(screen, time_delta)
                    self.player.damage_application(self.enemy)
                    self.set_text_box(self.player.text_entry)
                    self.victory()
                    self.phase = 'enemy'

                else:
                    self.enemy.affliction()
                    self.enemy.hit_player(self.player)
                    self.enemy.draw_attack(screen, time_delta)
                    self.enemy.damage_application(self.player)
                    self.set_text_box(self.enemy.text_entry)
                    self.game_over()
                    self.phase = 'player'

                    self.damage_phase = False

    def draw(self, screen, time_delta):
        screen.fill('black')
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.apply_damage(screen, time_delta)

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.create_text_box()

            elif event.type == pygame.KEYDOWN:
                pass

            if self.phase == 'player':
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.buttons_normal['fight']:
                        self.player.attack(self.enemy)
                        self.waiting = True
                        self.damage_phase = True
                    elif event.ui_element == self.buttons_normal['act']:
                        if self.mana_check():
                            enable_show_buttons(self.buttons_act)
                        else:
                            self.set_text_box(
                                ["I am afraid you are out of mana.", "You can no longer use spell till after the round."])
                    elif event.ui_element == self.buttons_normal['items']:
                        enable_show_buttons(self.buttons_items)
                    elif event.ui_element == self.buttons_normal['block']:
                        self.player.set_block()
                        self.waiting = True
                        self.damage_phase = True
                    elif event.ui_element == self.buttons_act['poison']:
                        self.reward = self.enemy.poison_spell
                        self.target = self.enemy
                        disable_hide_buttons(self.buttons_act)
                        self.sm.set_state('quiz')
                    elif event.ui_element == self.buttons_act['fire']:
                        self.reward = self.player.fire_spell
                        self.target = self.enemy
                        disable_hide_buttons(self.buttons_act)
                        self.sm.set_state('quiz')
                    elif event.ui_element == self.buttons_act['thunder']:
                        self.reward = self.player.thunder_spell
                        self.target = self.enemy
                        disable_hide_buttons(self.buttons_act)
                        self.sm.set_state('quiz')

            manager.process_events(event)

    def update(self):
        if not self.waiting:
            self.turn_combat()

    def store_state(self):
        self.sm.previous_state = {
            'name': 'combat',
            'enemy': self.enemy,
            'phase': self.phase,
            'reward': self.reward,
            'target': self.target,
            'waiting': True,
            'damage_phase': True
        }

    def create_text_box(self):
        if len(self.message_queue) > 0:
            self.text_box = pygame_gui.elements.ui_text_box.UITextBox(
                html_text=self.message_queue.pop(0), relative_rect=pygame.Rect(220, 600, 540, 100))
            self.text_box.set_active_effect('TEXT_EFFECT_TYPING_APPEAR')
        else:
            self.waiting = False

    def set_text_box(self, text):
        if len(text) > 0:
            self.message_queue.extend(text)
            text.clear()
            self.waiting = True

    def message_queue_empty(self):
        return len(self.message_queue) == 0

    def mana_check(self):
        return self.player.mana > 0


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
