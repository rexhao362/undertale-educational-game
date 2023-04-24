from menus.menu_class import Menu
from run_game import start_game
from game.systems.battle.topic import set_subject

def start_game():
    pass



class Game_Menu(Menu):
    def __init__(self):
        super().__init__('Game')
        self.add.selector(
            'Subject :', [
                ('Maths', 1), ('English', 2), ('Science', 3)
            ],
            onchange=set_subject
        )
        self.add.button('Play', start_game)


game_menu = Game_Menu('game')
