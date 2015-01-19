__author__ = 'jkamuda'

import pygame
from src.spritesheet import SpriteSheet
import src.constants as c
import src.coordinates as coords


class BrickPiece(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.dir = direction
        self.image = None

        self.init_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_image(self):
        sprite_sheet = SpriteSheet("data\item_objects.png")

        if self.dir == c.DIR_LEFT:
            self.image = sprite_sheet.get_image(coords.BRICK_PIECE_LEFT, c.IMG_MULTIPLIER, c.WHITE)
        else:
            self.image = sprite_sheet.get_image(coords.BRICK_PIECE_RIGHT, c.IMG_MULTIPLIER, c.WHITE)

    def shift_world(self, shift):
        self.rect.x += shift