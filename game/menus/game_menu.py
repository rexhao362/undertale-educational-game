from game.menus.menu_class import Menu
from game.run_game import start_game
from game.systems.battle.topic import set_subject


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
        self.center_content()


game_menu = Game_Menu()
