from menus.menu_class import Menu

class User_Menu(Menu):
    def __init__(self):
        super().__init__('Users')
        # for name in get_user_names:
        #     self.add.button(name)
        #  self.add.button('Create New User', create_user)