from menus import Menu

users_menu = Menu('')
for user in users:
    users_menu.add.button(user.name)