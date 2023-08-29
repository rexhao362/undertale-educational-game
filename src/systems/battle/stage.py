from src.systems.battle.enemy import create_enemy
import src.settings as s
import pygame
import pygame_gui


class Stage:
    def __init__(self, player, current_stage):
        self.player = player
        self.stage = current_stage
        self.enemy = create_enemy()
        self.turn = 'player'
        self.background = pygame.image.load(
            'assets/pictures/backgrounds/boss_battle_bg.png')
        self.buttons = {}

    def victory(self):
        if not self.enemy.is_alive():
            victory_img = 'assets/pictures/victory.png'
            # self.screen.blit(victory_img)
            self.player.user.update_user()
            self.game_won()

    def game_over(self):
        if not self.player.is_alive():
            defeat_img = 'assets/pictures/game_over.png'
            # self.screen.blit(defeat_img)

    def game_won(self):
        if self.stage == 5:
            pygame.quit()

    def turn_combat(self):
        if self.turn == 'player':
            self.player.action(self.enemy)
            self.victory()
            self.turn = 'enemy'
        else:
            self.enemy.attack(self.player)
            self.game_over()
            self.turn = 'player'

    def draw(self, screen, time_delta):
        screen.fill('black')
        screen.blit(self.background, (0, 0))
        self.enemy.draw(screen)
        if self.turn == 'player':
            self.draw_buttons()
        else:
            self.enemy.draw_attack(self.player, screen, time_delta)

    def draw_buttons(self):
        buttons_list = ['fight', 'act', 'item']

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

        # Draw the four rectangles
        for button in buttons_list:
            rect = pygame.Rect((left, top), (RECT_WIDTH, RECT_HEIGHT))
            self.buttons[button] = pygame_gui.elements.UIButton(
                relative_rect=rect,
                text=button)
            left += RECT_WIDTH + RECT_DISTANCE

    def events(self, manager):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                pass

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                pass

            manager.process_events(event)

    def update(self):
        self.turn_combat()

    def change_turn(self):
        if self.turn == 'player':
            self.turn == 'enemy'
        else:
            self.turn = 'enemy'


def combat_button(text, left):
    # Calculate the y-coordinate for the rectangles
    top = (3 * SCREEN_HEIGHT) // 4

    button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                          text=text)
    return button
