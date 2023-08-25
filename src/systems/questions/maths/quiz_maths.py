from src.systems.questions.maths.maths_questions import choose_maths_question
from src.manager import manager
import pygame
import pygame_gui
from src.systems.questions.topic import Quiz


class MathsQuiz(Quiz):
    def __init__(self):
        super().__init__(subject='maths')
        self.quiz = choose_maths_question()
        self.text = self.quiz['text']
        self.answer = self.quiz['answer']
        self.guess = None

    def draw(self, screen):
        font = pygame.font.Font('chalkduster.ttf', 24)
        question = font.render(self.text, True, 'white')
        screen.blit(question, (0, 0))

        num_box = pygame_gui.UITextEntryBox(
            relative_rect=pygame.Rect(
                (0, 0), 50,
                initial_text=""))

        start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                    text='Start',
                                                    manager=manager)

    def events(self):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code("return"):
                    self.check_answer()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == num_box:
                    self.guess = event.text

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    self.check_answer()

            manager.process_events(event)

    def check_answer(self):
        try:
            if int(self.guess) == self.answer:
                pass
            else:
                pass
        except ValueError as e:
            pass
