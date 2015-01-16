__author__ = 'jkamuda'

from box import Box
from src import coordinates as coords
from .. import constants as c
from src.spritesheet import SpriteSheet


class BrickBox(Box):
    def __init__(self, sound_manager, x, y):
        Box.__init__(self, sound_manager, x, y)

        self.box_time = -1
        self.game_time = 0

        self.init_frames()
        self.refresh_image(self.display_frame)

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")
        self.display_frame = sprite_sheet.get_image(coords.BRICK, c.IMG_MULTIPLIER, c.WHITE)

    def activate(self):
        self.in_transition = True
        self.y_offset = 10
        self.sound_manager.play_sound(c.SOUND_BUMP)
        return 0, 0

    def update(self, game_time):
        time_delta = (game_time - self.game_time)
        self.box_time += time_delta
        self.game_time = game_time

        if self.in_transition is True:
            if self.box_time > 10:
                self.y_offset -= 1
                self.box_time = 0
            if self.y_offset == 0:
                self.in_transition = False
        else:
            self.box_time = 0