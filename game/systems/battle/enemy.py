from sprites import Sprites

class Enemy(Sprites):
    def __init__(self, name, health, attack, defence):
        super().__init__(health, attack, defence)
        self.name = name