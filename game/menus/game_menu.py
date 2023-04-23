from game.menus.menu_class import Menu

def start_game():
    pass

def set_subject():
    pass

game_menu = Menu('game')

game_menu.add.selector('Subject :', [('Maths', 1), ('English', 2), ('Science', 3)], onchange=set_subject)
game_menu.add.button('Play', start_game)