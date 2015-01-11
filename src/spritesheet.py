__author__ = 'jkamuda'

from src import constants
from src.utils import *


class SpriteSheet():
    sprite_sheet = None

    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename)

    def get_image(self, rect, scale=1, colorkey=constants.BLACK):
        image = pygame.Surface([rect[2], rect[3]])
        image.blit(self.sprite_sheet, (0, 0), rect)
        image.set_colorkey(colorkey)
        if scale != 1:
            image = scale_image(image, scale)
        return image