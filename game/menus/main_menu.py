from menus.menu_class import Menu
from menus.parents_menu import parents_menu
from menus.game_menu import game_menu


class Main_Menu(Menu):
    def __init__(self):
        super().__init__('Main Menu')

        self.add.button('Kids', game_menu)
        self.add.button('Parents', parents_menu)

main_menu = Main_Menu()