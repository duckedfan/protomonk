__author__ = 'jkamuda'

import constants
from spritesheet import SpriteSheet
from utils import *


class Player(pygame.sprite.Sprite):

    state = constants.STATE_STANDING

    jumping_frame_l = None
    jumping_frame_r = None

    standing_frame_l = None
    standing_frame_r = None

    walking_frames_l = []
    walking_frames_r = []

    direction = "R"

    world_shift = 0

    def __init__(self, sound_manager):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager

        self.sprite_sheet = SpriteSheet("data\characters.gif")
        image = self.sprite_sheet.get_image(238, 1, 18, 32)
        image = scale_image(image, constants.IMG_MULTIPLIER)

        self.image = image
        self.rect = self.image.get_rect()

        self.load_adult_frames()

        self.x_vel = 0
        self.y_vel = 0

    def load_adult_frames(self):
        # Adult frame dimensions
        width = 18
        height = 32

        # Standing frames
        self.standing_frame_l = self.sprite_sheet.get_image(238, 1, width, height)
        self.standing_frame_l = scale_image(self.standing_frame_l, constants.IMG_MULTIPLIER)

        self.standing_frame_r = self.sprite_sheet.get_image(257, 1, width, height)
        self.standing_frame_r = scale_image(self.standing_frame_r, constants.IMG_MULTIPLIER)

        # Jumping frames
        self.jumping_frame_l = self.sprite_sheet.get_image(127, 1, width, height)
        self.jumping_frame_l = scale_image(self.jumping_frame_l, constants.IMG_MULTIPLIER)

        self.jumping_frame_r = self.sprite_sheet.get_image(368, 1, width, height)
        self.jumping_frame_r = scale_image(self.jumping_frame_r, constants.IMG_MULTIPLIER)

        # Walking frames
        right_1 = self.sprite_sheet.get_image(295, 1, width, height)
        right_2 = self.sprite_sheet.get_image(313, 1, width, height)
        right_3 = self.sprite_sheet.get_image(330, 1, width, height)

        right_1 = scale_image(right_1, constants.IMG_MULTIPLIER)
        right_2 = scale_image(right_2, constants.IMG_MULTIPLIER)
        right_3 = scale_image(right_3, constants.IMG_MULTIPLIER)

        self.walking_frames_r.append(right_1)
        self.walking_frames_r.append(right_2)
        self.walking_frames_r.append(right_3)

        left_1 = self.sprite_sheet.get_image(200, 1, width, height)
        left_3 = self.sprite_sheet.get_image(182, 1, width, height)
        left_2 = self.sprite_sheet.get_image(165, 1, width, height)

        left_1 = scale_image(left_1, constants.IMG_MULTIPLIER)
        left_2 = scale_image(left_2, constants.IMG_MULTIPLIER)
        left_3 = scale_image(left_3, constants.IMG_MULTIPLIER)

        self.walking_frames_l.append(left_1)
        self.walking_frames_l.append(left_2)
        self.walking_frames_l.append(left_3)

    def shift(self, shift):
        self.world_shift += shift

    def update(self, level):
        self.calc_gravity()

        self.rect.x += self.x_vel

        ground_collisions_x = pygame.sprite.spritecollide(self, level.ground_group, False)
        for platform in ground_collisions_x:
            if self.x_vel > 0:
                self.rect.right = platform.rect.left
            elif self.x_vel < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.y_vel
        ground_collisions_y = pygame.sprite.spritecollideany(self, level.ground_group)
        if ground_collisions_y:
            self.rect.bottom = ground_collisions_y.rect.top
            self.y_vel = 0

        if self.y_vel != 0:
            if self.direction == "R":
                self.image = self.jumping_frame_r
            else:
                self.image = self.jumping_frame_l
        elif self.x_vel == 0:
            if self.direction == "R":
                self.image = self.standing_frame_r
            else:
                self.image = self.standing_frame_l
        elif self.direction == "R":
            frame = ((self.rect.x + self.world_shift) // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = ((self.rect.x + self.world_shift) // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def go_right(self):
        self.x_vel = 30
        self.direction = "R"

    def go_left(self):
        self.x_vel = -20
        self.direction = "L"

    def jump(self):
        if self.y_vel == 0:
            self.y_vel += -15
            self.sound_manager.play_sound(constants.SOUND_SMALL_JUMP)

    def stop(self):
        self.x_vel = 0
