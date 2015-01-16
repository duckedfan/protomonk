__author__ = 'jkamuda'

from src.spritesheet import SpriteSheet
from src import coordinates as coords
from src import constants as c
from powerup import Powerup


class Mushroom(Powerup):
    def __init__(self, x, y):
        Powerup.__init__(self, x, y)

        sprite_sheet = SpriteSheet("data\item_objects.png")

        self.x_vel = 2

        self.display_frame = sprite_sheet.get_image(coords.MUSHROOM_POWERUP, c.IMG_MULTIPLIER, c.BLACK)
        self.refresh_image(self.display_frame)

        self.time = 0

        self.y_cap = self.rect.y - self.rect.height

    def update(self, game_time, viewport):
        if self.emerging:
            if self.time == 0:
                self.time = game_time
            elif (game_time - self.time) > 10:
                self.time = game_time
                self.rect.y -= .5

            if self.rect.y < self.y_cap:
                self.emerging = False
        else:
            self.calc_gravity()
            if self.direction == c.DIR_RIGHT:
                self.x_vel = 2
            else:
                self.x_vel = -2

            self.rect.x += self.x_vel
            self.rect.y += self.y_vel