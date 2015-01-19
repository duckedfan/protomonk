__author__ = 'jkamuda'

import pygame
from box import Box
from src import coordinates as coords
from .. import constants as c
from src.spritesheet import SpriteSheet


class BrickBox(Box):
    def __init__(self, sound_manager, x, y):
        Box.__init__(self, sound_manager, x, y)

        self.box_time = -1
        self.game_time = 0

        self.brick_piece_left_frame = None
        self.brick_piece_right_frame = None
        self.exploding = False
        self.exploding_timer = 0
        self.brick_pieces_left = []
        self.brick_pieces_right = []

        self.init_frames()
        self.refresh_image(self.display_frame)

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")
        self.display_frame = sprite_sheet.get_image(coords.BRICK, c.IMG_MULTIPLIER, c.WHITE)

        item_objects_ss = SpriteSheet("data\item_objects.png")
        self.brick_piece_left_frame = item_objects_ss.get_image(coords.BRICK_PIECE_LEFT, c.IMG_MULTIPLIER, c.WHITE)
        self.brick_piece_right_frame = item_objects_ss.get_image(coords.BRICK_PIECE_RIGHT, c.IMG_MULTIPLIER, c.WHITE)

    def activate(self):
        self.in_transition = True
        self.y_offset = 10
        self.sound_manager.play_sound(c.SOUND_BUMP)
        return 0, 0

    def explode(self):
        self.exploding = True
        self.brick_pieces_left.append((self.rect.left + 5, self.rect.top + 5))
        self.brick_pieces_left.append((self.rect.left + 5, self.rect.bottom - 20))

    def update(self, game_time):
        time_delta = (game_time - self.game_time)
        self.box_time += time_delta
        self.game_time = game_time

        if self.exploding:
            pass
        else:
            if self.in_transition is True:
                if self.box_time > 10:
                    self.y_offset -= 1
                    self.box_time = 0
                if self.y_offset == 0:
                    self.in_transition = False
            else:
                self.box_time = 0

    def draw(self, screen):
        if self.exploding:
            for piece in self.brick_pieces_left:
                screen.blit(self.brick_piece_left_frame, piece)
        else:
            super(BrickBox, self).draw(screen)