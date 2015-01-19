__author__ = 'jkamuda'

from src import constants
from src.utils import *


class SpriteSheet():
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename)
        if self.sprite_sheet.get_alpha():
            self.sprite_sheet = self.sprite_sheet.convert_alpha()
        else:
            self.sprite_sheet = self.sprite_sheet.convert()

    def get_image(self, rect, scale=1, colorkey=constants.BLACK):
        image = pygame.Surface([rect[2], rect[3]]).convert()
        image.fill(colorkey)
        image.set_colorkey(colorkey)
        image.blit(self.sprite_sheet, (0, 0), rect)
        if scale != 1:
            image = scale_image(image, scale)
        return image