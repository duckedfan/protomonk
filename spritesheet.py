__author__ = 'jkamuda'

import constants
from utils import *


class SpriteSheet():

    sprite_sheet = None

    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height, scale=1):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        if scale != 1:
            image = scale_image(image, scale)
        return image

    def get_image_v2(self, rect, scale=1):
        image = pygame.Surface([rect[2], rect[3]]).convert()
        image.blit(self.sprite_sheet, (0, 0), rect)
        image.set_colorkey(constants.BLACK)
        if scale != 1:
            image = scale_image(image, scale)
        return image