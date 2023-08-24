from src.systems.questions.maths.maths_questions import choose_maths_question
from src.manager import manager
import pygame
import pygame_gui


class MathsQuiz:
    def __init__(self) -> None:
        self.quiz = choose_maths_question()
        self.text = self.quiz['text']
        self.answer = self.quiz['answer']

    def events(self):
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.KEYDOWN:
                pass

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start:
                    mark()
            
    def draw(self, screen):
        font = pygame.font.Font('chalkduster.ttf', 24)
        question = font.render(self.text, 'white')
        question_rect = question.get_rect()
        screen.blit(question_rect, center)#todo

        text_entry_box = pygame_gui.UITextEntryBox(
        relative_rect=pygame.Rect((0, 0), notepad_window.get_container().get_size()),
        initial_text="",
        container=notepad_window)




    def mark(self, input):
        if input == self.answer:
            pass
        else:
            pass