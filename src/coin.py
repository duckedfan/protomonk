__author__ = 'jkamuda'

import pygame
import pygame.gfxdraw

from src import coordinates as coords
import constants as constants
from src.spritesheet import SpriteSheet


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.shift = 0

        self.x = x
        self.y = y

        self.y_offset = 0
        self.y_velocity = 0
        self.is_bouncing = False

        self.game_time = 0
        self.display_frame = None
        self.coin_frames = []
        self.coin_frame_idx = 0
        self.game_time = 0
        self.coin_time = 0

        self.init_frames()

        self.image = self.coin_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\item_objects.png")

        self.coin_frames.append(sprite_sheet.get_image(coords.COIN_SPINNING_1, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image(coords.COIN_SPINNING_2, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image(coords.COIN_SPINNING_3, constants.IMG_MULTIPLIER))
        self.coin_frames.append(sprite_sheet.get_image(coords.COIN_SPINNING_4, constants.IMG_MULTIPLIER))

        for frame in self.coin_frames:
            frame.set_colorkey(constants.BLACK)

    def start_coin_bounce(self):
        self.y_velocity = -10
        self.is_bouncing = True

    def calc_gravity(self):
        self.y_velocity += .55

    def shift_world(self, shift):
        self.shift += shift

    def update(self, game_time):
        if self.is_bouncing:
            self.calc_gravity()
            self.rect.y += self.y_velocity
            if self.rect.y > self.y:
                # self.kill()
                self.is_bouncing = False

        time_delta = game_time - self.coin_time
        if time_delta > 50:
            if self.coin_frame_idx < 3:
                self.coin_frame_idx += 1
            else:
                self.coin_frame_idx = 0

            self.coin_time = game_time

        self.display_frame = self.coin_frames[self.coin_frame_idx]
        self.refresh_rect()

    def refresh_rect(self):
        bottom = self.rect.bottom
        self.image = self.display_frame
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.bottom = bottom

    def draw(self, screen):
        x_offset = int(self.rect.width / 2)
        screen.blit(self.display_frame, (self.rect.x + self.shift - x_offset, self.rect.y - self.y_offset))

