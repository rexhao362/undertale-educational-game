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

    def game_over(self, screen):
        if not self.player.is_alive():
            screen.fill('black')
            defeat_img = 'assets/pictures/game_over.png'
            screen.blit(defeat_img, (0, 0))

    def game_won(self):
        if self.stage == 5:
            pygame.quit()

    def turn_combat(self):
        if self.turn == 'player':
            self.victory()
        else:
            self.enemy.attack(self.player)
            self.game_over()
            self.turn = 'player'
            self.player.acting = True

    def draw(self, screen, time_delta):
        screen.fill('black')
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
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

    def draw_items(self):
        for item in self.player.get_items():
            pass

    def events(self, manager):
        for event in pygame.events.get():
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
                    pass
                elif event.ui_element == self.buttons['items']:
                    pass
                self.turn = 'enemy'

            manager.process_events(event)

    def update(self):
        self.turn_combat()

    def change_turn(self):
        if self.turn == 'player':
            self.turn == 'enemy'
        else:
            self.turn = 'enemy'
