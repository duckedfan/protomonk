__author__ = 'jkamuda'

import pygame
from src.spritesheet import SpriteSheet
import src.constants as c
import src.coordinates as coords


class BrickPiece(pygame.sprite.Sprite):
    def __init__(self, x, y, x_vel, y_vel):
        pygame.sprite.Sprite.__init__(self)

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.image = None

        self.init_image()
        self.piece_time = -1

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_image(self):
        sprite_sheet = SpriteSheet("data\item_objects.png")

        if self.x_vel < 0:
            self.image = sprite_sheet.get_image(coords.BRICK_PIECE_LEFT, c.IMG_MULTIPLIER, c.WHITE)
        else:
            self.image = sprite_sheet.get_image(coords.BRICK_PIECE_RIGHT, c.IMG_MULTIPLIER, c.WHITE)

    def shift_world(self, shift):
        self.rect.x += shift

    def update(self, game_time):
        if self.piece_time == -1:
            self.piece_time = game_time

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += .50

        if (game_time - self.piece_time) > 1500:
            self.kill()
