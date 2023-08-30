from src.systems.questions.maths.maths_questions import choose_maths_question
import pygame
import pygame_gui
from src.systems.questions.quiz import Quiz


class MathsQuiz(Quiz):
    def __init__(self):
        super().__init__(subject='maths')
        self.quiz = choose_maths_question()
        self.text = self.quiz['text']
        self.answer = self.quiz['answer']
        self.solution = None
        self.num_box = None
        # self.start_button = None

    def draw(self, screen, time_delta):
        font = pygame.font.Font('data/fonts/league_spartan.ttf', 24)
        question = font.render(self.text, True, 'white')
        screen.blit(question, (0, 0))

        self.num_box = pygame_gui.elements.UITextEntryBox(
            relative_rect=pygame.Rect(
                (0, 0), 50,
                initial_text=''))

        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                    text='Start')

    def events(self, manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code("return"):
                    self.check_answer()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == self.num_box:
                    self.solution = self.num_box.get_text()

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    self.check_answer()

            manager.process_events(event)

    def check_answer(self):
        try:
            if int(self.solution) == self.answer:
                pass
            else:
                pass
        except ValueError as e:
            pass
