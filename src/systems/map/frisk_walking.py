from systems.sprite_sheet import SpriteSheet
import src.settings as s

class FriskWalk(SpriteSheet):
    def __init__(self, direction, width, num_sprites, position):
        sheet = f'assets/pictures/spritesheets/frisk_{direction}.png'
        super().__init__(sheet, width, 29, 5, num_sprites)
        self.move_x = 0
        self.move_y = 0
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move(self, x, y):
        self.move_x += x
        self.move_y += y
        if x == 0 and y == 0:
            self.move_x = 0 
            self.move_y = 0


    def update_position(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > s.settings.screen_width - self.rect.width:
            self.rect.x = s.settings.screen_width - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > s.settings.screen_height - self.rect.height:
            self.rect.y = s.settings.screen_height - self.rect.height