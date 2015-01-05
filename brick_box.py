__author__ = 'jkamuda'

import pygame
import pygame.gfxdraw
import coordinates as coords
import constants as constants
from spritesheet import SpriteSheet


class BrickBox(pygame.sprite.Sprite):
    brick_frame = None
    box_time = -1
    game_time = 0
    in_transition = False
    y_offset = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.init_frames()

        self.image = self.brick_frame
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")

        self.brick_frame = sprite_sheet.get_image_v2(coords.BRICK, constants.IMG_MULTIPLIER)
        self.brick_frame.set_colorkey(constants.WHITE)

    def activate(self):
        self.in_transition = True
        self.y_offset = 10
        return (0, 0)

    def update(self, game_time):
        if self.game_time == 0:
            self.game_time = game_time

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

    def draw(self, screen):
        screen.blit(self.brick_frame, (self.rect.x, self.rect.y - self.y_offset))