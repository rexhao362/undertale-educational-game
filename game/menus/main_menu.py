from game.menus.menu_class import Menu
from game.menus.parents_menu import parents_menu
from game.menus.game_menu import game_menu


main_menu = Menu('main menu')

main_menu.add.button('Kids', game_menu)
main_menu.add.button('Parents', parents_menu)
