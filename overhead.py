__author__ = 'jkamuda'

from texthelper import TextHelper
from spritesheet import SpriteSheet
import constants
import coordinates as coords


class Overhead():

    coin_frames = []

    points = 0
    coins = 0
    level = 1
    episode = 1
    time = None

    def __init__(self):
        self.text_helper = TextHelper()

        # tile_set.png
        tileset_ss = SpriteSheet("data/tile_set.png")
        tileset = tileset_ss.get_image_v2((0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), constants.IMG_MULTIPLIER)
        tileset.set_colorkey(constants.WHITE)

        coin_frame_1 = tileset_ss.get_image_v2(coords.COIN_1)
        coin_frame_1.set_colorkey(constants.WHITE)
        self.coin_frames.append(coin_frame_1)
        self.coin_frames.append(tileset_ss.get_image_v2(coords.COIN_2))
        self.coin_frames.append(tileset_ss.get_image_v2(coords.COIN_3))


    def draw(self, screen):
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
        screen.blit(self.coin_frames[0], (260, 40))

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