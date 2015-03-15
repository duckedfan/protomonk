__author__ = 'jkamuda'

import pygame
from src.spritesheet import SpriteSheet
from src import utils
from src import coordinates as coords
from src import constants as c


class Score(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        pygame.sprite.Sprite.__init__(self)

        self.score = score
        self.score_dict = {}
        self.digit_images = []
        self.digit_positions = []
        self.x = x
        self.y = y
        self.shift = 0
        self.score_time = -1
        self.y_offset = 0

        self.init_score_dictionary()
        self.build_digit_images()

    def init_score_dictionary(self):
        tile_set = SpriteSheet("data/item_objects.png")

        self.score_dict[0] = tile_set.get_image(coords.SCORE_WHITE_0, c.IMG_MULTIPLIER)
        self.score_dict[1] = tile_set.get_image(coords.SCORE_WHITE_1, c.IMG_MULTIPLIER)
        self.score_dict[2] = tile_set.get_image(coords.SCORE_WHITE_2, c.IMG_MULTIPLIER)
        self.score_dict[4] = tile_set.get_image(coords.SCORE_WHITE_4, c.IMG_MULTIPLIER)
        self.score_dict[5] = tile_set.get_image(coords.SCORE_WHITE_5, c.IMG_MULTIPLIER)
        self.score_dict[8] = tile_set.get_image(coords.SCORE_WHITE_8, c.IMG_MULTIPLIER)

    def get_digit_image(self, digit):
        if digit not in self.score_dict:
            raise(digit + " not supported for scores")
        else:
            return self.score_dict[digit]

    def build_digit_images(self):
        digits = utils.get_digits(self.score)
        for i in range(len(digits) - 1, -1, -1):
            image = self.get_digit_image(digits[i])
            position = (self.x, self.y)

            self.x += image.get_rect().width + 2

            self.digit_positions.append(position)
            self.digit_images.append(image)

    def shift_world(self, shift):
        self.shift += shift

    def update(self, game_time):
        if self.score_time == -1:
            self.score_time = game_time
        else:
            time_delta = game_time - self.score_time
            if time_delta > 500:
                self.kill()

        self.y_offset += 1

    def draw(self, screen):
        for i in range(0, len(self.digit_images)):
            position = (self.digit_positions[i][0] + self.shift, self.digit_positions[i][1] - self.y_offset)
            screen.blit(self.digit_images[i], position)