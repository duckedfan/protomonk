__author__ = 'jkamuda'

import pygame

from src import coordinates as coords
import constants as constants
from src.spritesheet import SpriteSheet


class CoinBox(pygame.sprite.Sprite):

    empty = False
    coin_box_empty_frame = None
    display_frame = None
    coin_box_frames = []
    coin_box_frame_idx = 0
    coin_box_time = -1
    game_time = 0

    in_transition = False
    transition_time = 0
    y_offset = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.init_frames()

        self.image = self.coin_box_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")

        self.coin_box_frames.append(sprite_sheet.get_image_v2(coords.COIN_BOX_1, constants.IMG_MULTIPLIER))
        self.coin_box_frames.append(sprite_sheet.get_image_v2(coords.COIN_BOX_2, constants.IMG_MULTIPLIER))
        self.coin_box_frames.append(sprite_sheet.get_image_v2(coords.COIN_BOX_3, constants.IMG_MULTIPLIER))

        self.coin_box_empty_frame = sprite_sheet.get_image_v2(coords.COIN_BOX_EMPTY, constants.IMG_MULTIPLIER)
        self.coin_box_empty_frame.set_colorkey(constants.WHITE)

        for frame in self.coin_box_frames:
            frame.set_colorkey(constants.WHITE)

    def activate(self):
        if self.empty is False:
            self.in_transition = True
            self.y_offset = 10
            return (200, 1)
        else:
            return (0, 0)

    def update(self, game_time):
        if self.game_time == 0:
            self.game_time = game_time

        time_delta = (game_time - self.game_time)
        self.coin_box_time += time_delta
        self.transition_time = self.coin_box_time
        self.game_time = game_time

        if self.empty:
            self.display_frame = self.coin_box_empty_frame
        else:
            if 0 < self.coin_box_time <= 400:
                self.coin_box_frame_idx = 0
            elif 400 < self.coin_box_time <= 600:
                self.coin_box_frame_idx = 1
            elif 600 < self.coin_box_time <= 700:
                self.coin_box_frame_idx = 2
            elif self.coin_box_time > 700:
                self.coin_box_frame_idx = 0
                self.coin_box_time = 0

            self.display_frame = self.coin_box_frames[self.coin_box_frame_idx]

        if self.in_transition is True:
            if self.transition_time > 10:
                self.y_offset -= 1
                self.transition_time = 0
            if self.y_offset == 0:
                self.in_transition = False
                self.empty = True
        else:
            self.transition_time = 0

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x, self.rect.y - self.y_offset))
