from src.systems.questions.maths.maths_questions import choose_maths_question
import pygame
import pygame_gui
from src.systems.questions.quiz import Quiz


class MathsQuiz(Quiz):
    def __init__(self, state_manager):
        super().__init__(state_manager, 'maths')
        self.quiz = choose_maths_question()
        self.text = self.quiz['text']
        self.answer = self.quiz['answer']
        self.solution = None
        self.num_box = create_num_box()
        self.start_button = create_start_box()

    def draw(self, screen, time_delta):
        font = pygame.font.Font('data/fonts/league_spartan.ttf', 36)
        question = font.render(self.text, True, 'white')
        screen.blit(question, (0, 0))
        self.draw_crosses(screen)

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.check_answer()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == self.num_box:
                    self.solution = event.text

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                self.check_answer()

            manager.process_events(event)

    def check_answer(self):
        try:
            if int(self.solution) == self.answer:
                self.correct_answer()
            else:
                self.wrong_answer()
        except ValueError as e:
            pass


def create_num_box():
    num_box = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect(
            (500, 300), (100, 50)))
    num_box.set_allowed_characters('numbers')
    return num_box


def create_start_box():
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-100, -200), (100, 50)),
                                        text='Start')
