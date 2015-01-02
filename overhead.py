__author__ = 'jkamuda'

from texthelper import TextHelper
from spritesheet import SpriteSheet
import constants
import coordinates as coords


class Overhead():

    coin_frames = []
    coin_frame_idx = 0
    coin_time = 0

    points = 0
    coins = 0
    level = 1
    episode = 1
    time = None

    def __init__(self):
        self.text_helper = TextHelper()

        # tile_set.png
        item_objects_ss = SpriteSheet("data/item_objects.png")

        self.coin_frames.append(item_objects_ss.get_image_v2(coords.TITLE_COIN_1, constants.IMG_MULTIPLIER))
        self.coin_frames.append(item_objects_ss.get_image_v2(coords.TITLE_COIN_2, constants.IMG_MULTIPLIER))
        self.coin_frames.append(item_objects_ss.get_image_v2(coords.TITLE_COIN_3, constants.IMG_MULTIPLIER))

    def draw(self, screen, current_time):
        # Mario
        screen.blit(self.text_helper.get_text('m'), (50, 20))
        screen.blit(self.text_helper.get_text('a'), (70, 20))
        screen.blit(self.text_helper.get_text('r'), (90, 20))
        screen.blit(self.text_helper.get_text('i'), (110, 20))
        screen.blit(self.text_helper.get_text('o'), (130, 20))

        # Mario score
        screen.blit(self.text_helper.get_text('0'), (50, 40))
        screen.blit(self.text_helper.get_text('0'), (70, 40))
        screen.blit(self.text_helper.get_text('0'), (90, 40))
        screen.blit(self.text_helper.get_text('0'), (110, 40))
        screen.blit(self.text_helper.get_text('0'), (130, 40))
        screen.blit(self.text_helper.get_text('0'), (150, 40))

        # Coins
        coin_time_delta = current_time - self.coin_time
        if coin_time_delta > 250:
            self.coin_time = current_time
            self.coin_frame_idx += 1
            if self.coin_frame_idx >= 3:
                self.coin_frame_idx = 0
        screen.blit(self.coin_frames[self.coin_frame_idx], (268, 38))

        # TODO fix the dimensions for the non-char characters!
        screen.blit(self.text_helper.get_text('+'), (284, 44))
        screen.blit(self.text_helper.get_text('0'), (300, 40))
        screen.blit(self.text_helper.get_text('0'), (320, 40))

        # World
        screen.blit(self.text_helper.get_text('w'), (450, 20))
        screen.blit(self.text_helper.get_text('o'), (470, 20))
        screen.blit(self.text_helper.get_text('r'), (490, 20))
        screen.blit(self.text_helper.get_text('l'), (510, 20))
        screen.blit(self.text_helper.get_text('d'), (530, 20))

        # Level - Episode
        screen.blit(self.text_helper.get_text('1'), (470, 40))
        screen.blit(self.text_helper.get_text('-'), (490, 47))
        screen.blit(self.text_helper.get_text('1'), (510, 40))

        # Time
        screen.blit(self.text_helper.get_text('t'), (610, 20))
        screen.blit(self.text_helper.get_text('i'), (630, 20))
        screen.blit(self.text_helper.get_text('m'), (650, 20))
        screen.blit(self.text_helper.get_text('e'), (670, 20))

        # Time (reported)
        if self.time:
            screen.blit(self.text_helper.get_text('t'), (610, 40))

    def animation(self):
        pass