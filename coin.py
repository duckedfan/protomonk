__author__ = 'jkamuda'

import pygame
import pygame.gfxdraw
import coordinates as coords
import constants as constants
from spritesheet import SpriteSheet


class Coin(pygame.sprite.Sprite):
    display_frame = None
    coin_frames = []
    game_time = 0
    coin_time = 0

    y_offset = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.init_frames()

        self.image = self.coin_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\item_objects.png")

        self.coin_frames.append(sprite_sheet.get_image_v2(coords.COIN_SPINNING_1, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image_v2(coords.COIN_SPINNING_2, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image_v2(coords.COIN_SPINNING_3, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image_v2(coords.COIN_SPINNING_4, constants.IMG_MULTIPLIER))

        for frame in self.coin_frames:
            frame.set_colorkey(constants.BLACK)

    def update(self, game_time):
        if self.game_time == 0:
            self.game_time = game_time

        time_delta = (game_time - self.game_time)
        self.coin_time += time_delta
        self.game_time = game_time

        coin_frame_idx = 0
        if 0 < self.coin_time <= 100:
            coin_frame_idx = 0
        elif 100 < self.coin_time <= 200:
            coin_frame_idx = 1
        elif 200 < self.coin_time <= 300:
            coin_frame_idx = 2
        elif 300 < self.coin_time <= 400:
            coin_frame_idx = 2
        elif self.coin_time > 400:
            coin_frame_idx = 0
            self.coin_time = 0

        self.display_frame = self.coin_frames[coin_frame_idx]

        self.image = self.display_frame
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        width = self.rect.width
        x_offset = int(width / 2)

        screen.blit(self.display_frame, (self.rect.x - x_offset, self.rect.y - self.y_offset))

