__author__ = 'jkamuda'

import pygame

from src import coordinates as coords
from .. import constants as c
from src.spritesheet import SpriteSheet
from src.coin import Coin
from src.score import Score


class CoinBox(pygame.sprite.Sprite):
    def __init__(self, sound_manager, x, y, num_coins=1):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager
        self.num_coins = num_coins
        self.empty = False
        self.empty_frame = None
        self.display_frame = None
        self.coin_box_frames = []
        self.frame_idx = 0
        self.coin_box_time = 0
        self.game_time = 0
        self.in_transition = False
        self.transition_time = 0
        self.y_offset = 0

        self.coin_animating = False
        self.coin = None

        self.score_group = pygame.sprite.Group()

        self.init_frames()

        self.image = self.coin_box_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")

        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_1, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_2, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_3, c.IMG_MULTIPLIER, c.WHITE))

        self.empty_frame = sprite_sheet.get_image(coords.COIN_BOX_EMPTY, c.IMG_MULTIPLIER, c.WHITE)

    def shift_world(self, shift):
        self.rect.x += shift
        if self.coin_animating:
            self.coin.shift_world(shift)

        for score in self.score_group:
            score.shift_world(shift)

    def activate(self):
        if self.empty is False:
            self.in_transition = True
            self.y_offset = 10
            self.sound_manager.play_sound(c.SOUND_COIN)
            self.start_coin_animation()
            return 200, 1
        else:
            self.sound_manager.play_sound(c.SOUND_BUMP)
            return 0, 0

    def update(self, game_time):
        time_delta = (game_time - self.game_time)
        self.coin_box_time += time_delta
        self.transition_time = self.coin_box_time
        self.game_time = game_time

        if self.empty:
            self.display_frame = self.empty_frame
        else:
            if 0 < self.coin_box_time <= 400:
                self.frame_idx = 0
            elif 400 < self.coin_box_time <= 600:
                self.frame_idx = 1
            elif 600 < self.coin_box_time <= 700:
                self.frame_idx = 2
            elif self.coin_box_time > 700:
                self.frame_idx = 0
                self.coin_box_time = 0

            self.display_frame = self.coin_box_frames[self.frame_idx]

        if self.in_transition is True:
            if self.transition_time > 10:
                self.y_offset -= 1
                self.transition_time = 0
            if self.y_offset == 0:
                self.in_transition = False
                self.empty = True
        else:
            self.transition_time = 0

        if self.coin_animating:
            self.coin.update(game_time)
            if not self.coin.is_bouncing:
                self.coin_animating = False
                score = Score(self.rect.x + 5, self.rect.y - 25, 200)
                self.score_group.add(score)

        for group in self.score_group:
            group.update(game_time)

    def start_coin_animation(self):
        self.coin_animating = True
        self.coin = Coin(self.rect.x + (self.rect.width / 2), self.rect.y - self.y_offset - 40)
        self.coin.start_coin_bounce()

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x, self.rect.y - self.y_offset))
        if self.coin_animating:
            self.coin.draw(screen)

        for score in self.score_group:
            score.draw(screen)
