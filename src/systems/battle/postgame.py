import src.systems.state as state
import pygame
import pygame_gui
from src.systems.music import play_music


class PostGame(state.State):
    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.sm.user.update_user()
        self.font = pygame.font.Font('data/fonts/league_spartan.ttf', 30)
        self.correct_maths = self.sm.user.overall['maths']['correct']
        self.wrong_maths = self.sm.user.overall['maths']['wrong']
        self.correct_spelling = self.sm.user.overall['spelling']['correct']
        self.wrong_spelling = self.sm.user.overall['spelling']['wrong']

    def draw(self, screen, time_delta):
        if not self.sm.game_over:
            if self.sm.stage == 5:
                image = pygame.image.load(
                    'assets/pictures/backgrounds/victory.png').convert_alpha()
                screen.blit(image, (0, 0))
                text = f"""Congratulations on wining the game.
                You got {self.correct_maths} maths and {self.correct_spelling}
                spelling questions correct, respectively.
                You got {self.wrong_maths} maths and {self.wrong_spelling}
                spelling questions wrong."""
                create_text_box(text)
                play_music('Various Themes/Victorious')
            else:
                image = pygame.image.load(
                    'assets/pictures/backgrounds/round_won.png'
                    ).convert_alpha()
                screen.blit(image, (0, 0))
                text = f"""So far you have gotten {self.correct_maths} maths
                and {self.correct_spelling} spelling questions right,
                respectively.
                You have gotten {self.wrong_maths} maths and
                {self.wrong_spelling} spelling questions wrong."""
                play_music('Various Themes/A Little R & R')
                create_text_box(text)
        else:
            image = 'assets/pictures/game_over.png'
            game_over = pygame.image.load(image).convert_alpha()
            screen.blit('black')
            screen.blit(game_over, (200, 300))
            text = f"""Unlucky. You managed to get {self.correct_maths} maths
            and {self.correct_spelling} spelling questions right, respectively.
            You got {self.wrong_maths} maths and {self.wrong_spelling} spelling
            questions wrong."""
            create_text_box(text)
            play_music('Various Themes/To Suffer a Loss (Game Over)')

    def update(self):
        pass

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.sm.stage == 5:
                    exit()
                else:
                    self.sm.set_state('tilemap')

            elif event.type == pygame.KEYDOWN:
                if self.sm.stage == 5:
                    exit()
                else:
                    self.sm.set_state('tilemap')


def create_text_box(text):
    text_box = pygame_gui.elements.ui_text_box.UITextBox(
        html_text=text,
        relative_rect=pygame.Rect(400, 350, 250, 300))
    return text_box
