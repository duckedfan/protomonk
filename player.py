__author__ = 'jkamuda'

import constants as c
from spritesheet import SpriteSheet
from utils import *
import coordinates


class Player(pygame.sprite.Sprite):

    state = c.STATE_STANDING
    power = c.POWER_SMALL

    transition_state = None
    transition_timer = 0

    player_small_frames = {}
    player_frames = {}
    transition_frames = {}
    death_frame = None

    direction = c.DIR_RIGHT

    world_shift = 0

    def __init__(self, sound_manager, game_info):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager
        self.game_info = game_info

        self.sprite_sheet = SpriteSheet("data\characters.gif")

        self.load_player_small_frames()
        self.load_player_adult_frames()

        self.image = self.get_player_frame(self.state, self.direction)
        self.rect = self.image.get_rect()

        self.rect.left = 100

        self.x_vel = 0
        self.y_vel = 0

    def load_player_small_frames(self):
        dir_keys = [c.DIR_LEFT, c.DIR_RIGHT]
        self.player_small_frames[c.STATE_STANDING] = dict((key, []) for key in dir_keys)
        self.player_small_frames[c.STATE_WALKING] = dict((key, []) for key in dir_keys)
        self.player_small_frames[c.STATE_JUMPING] = dict((key, []) for key in dir_keys)

        # Standing frames
        self.player_small_frames[c.STATE_STANDING][c.DIR_LEFT].append(self.sprite_sheet.get_image(223, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER))
        self.player_small_frames[c.STATE_STANDING][c.DIR_RIGHT].append(self.sprite_sheet.get_image(276, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER))

        # Jumping frames
        self.player_small_frames[c.STATE_JUMPING][c.DIR_LEFT].append(self.sprite_sheet.get_image(142, 43, c.PLAYER_SMALL_JUMP_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER))
        self.player_small_frames[c.STATE_JUMPING][c.DIR_RIGHT].append(self.sprite_sheet.get_image(355, 43, c.PLAYER_SMALL_JUMP_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER))

        # Transition frames
        self.transition_frames = dict((key, []) for key in dir_keys)
        self.transition_frames[c.DIR_LEFT] = self.sprite_sheet.get_image(239, 36, c.PLAYER_MID_W, c.PLAYER_MID_H, c.IMG_MULTIPLIER)
        self.transition_frames[c.DIR_RIGHT] = self.sprite_sheet.get_image(258, 36, c.PLAYER_MID_W, c.PLAYER_MID_H, c.IMG_MULTIPLIER)

        # Death frame
        self.death_frame = self.sprite_sheet.get_image_v2(coordinates.MARIO_DEAD, c.IMG_MULTIPLIER)

        # Walking frames
        right_1 = self.sprite_sheet.get_image(291, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)
        right_2 = self.sprite_sheet.get_image(305, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)
        right_3 = self.sprite_sheet.get_image(321, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)

        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_1)
        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_2)
        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_3)

        left_1 = self.sprite_sheet.get_image(208, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)
        left_2 = self.sprite_sheet.get_image(194, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)
        left_3 = self.sprite_sheet.get_image(178, 43, c.PLAYER_SMALL_W, c.PLAYER_SMALL_H, c.IMG_MULTIPLIER)

        self.player_small_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_1)
        self.player_small_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_2)
        self.player_small_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_3)

    def load_player_adult_frames(self):
        dir_keys = [c.DIR_LEFT, c.DIR_RIGHT]
        self.player_frames[c.STATE_STANDING] = dict((key, []) for key in dir_keys)
        self.player_frames[c.STATE_WALKING] = dict((key, []) for key in dir_keys)
        self.player_frames[c.STATE_JUMPING] = dict((key, []) for key in dir_keys)
        self.player_frames[c.STATE_CROUCHING] = dict((key, []) for key in dir_keys)

        # Standing frames
        self.player_frames[c.STATE_STANDING][c.DIR_LEFT].append(self.sprite_sheet.get_image(238, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))
        self.player_frames[c.STATE_STANDING][c.DIR_RIGHT].append(self.sprite_sheet.get_image(257, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))

        # Jumping frames
        self.player_frames[c.STATE_JUMPING][c.DIR_LEFT].append(self.sprite_sheet.get_image(127, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))
        self.player_frames[c.STATE_JUMPING][c.DIR_RIGHT].append(self.sprite_sheet.get_image(368, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))

        # Crouching frames
        self.player_frames[c.STATE_CROUCHING][c.DIR_LEFT].append(self.sprite_sheet.get_image(221, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))
        self.player_frames[c.STATE_CROUCHING][c.DIR_RIGHT].append(self.sprite_sheet.get_image(276, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER))

        # Walking frames
        right_1 = self.sprite_sheet.get_image(295, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)
        right_2 = self.sprite_sheet.get_image(313, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)
        right_3 = self.sprite_sheet.get_image(330, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)

        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_1)
        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_2)
        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_3)

        left_1 = self.sprite_sheet.get_image(200, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)
        left_2 = self.sprite_sheet.get_image(165, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)
        left_3 = self.sprite_sheet.get_image(182, 1, c.PLAYER_ADULT_W, c.PLAYER_ADULT_H, c.IMG_MULTIPLIER)

        self.player_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_1)
        self.player_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_2)
        self.player_frames[c.STATE_WALKING][c.DIR_LEFT].append(left_3)

    def get_player_frame(self, state, direction, position=0):
        if self.power == c.POWER_SMALL:
            frame_idx = position % len(self.player_small_frames[state][direction])
            return self.player_small_frames[state][direction][frame_idx]
        else:
            frame_idx = position % len(self.player_frames[state][direction])
            return self.player_frames[state][direction][frame_idx]

    def shift(self, shift):
        self.world_shift += shift

    def refresh_rect(self):
        bottom = self.rect.bottom
        left = self.rect.left
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left

    def update(self, level, current_time):
        if self.transition_state:
            if self.transition_state == c.TRANSITION_SMALL_TO_BIG:
                self.small_to_big(current_time)
            elif self.transition_state == c.TRANSITION_BIG_TO_SMALL:
                self.big_to_small(current_time)
            elif self.transition_state == c.TRANSITION_DEATH_SEQUENCE:
                self.death_sequence(current_time)
                self.calc_gravity()
                self.rect.y += self.y_vel

            self.refresh_rect()
            return

        self.calc_gravity()

        self.rect.x += self.x_vel

        ground_collisions_x = pygame.sprite.spritecollide(self, level.ground_group, False)
        for platform in ground_collisions_x:
            if self.x_vel > 0:
                self.rect.right = platform.rect.left
            elif self.x_vel < 0:
                self.rect.left = platform.rect.right

        coin_box_collisions_x = pygame.sprite.spritecollide(self, level.coin_box_group, False)
        for coin_box in coin_box_collisions_x:
            if self.x_vel > 0:
                self.rect.right = coin_box.rect.left
            elif self.x_vel < 0:
                self.rect.left = coin_box.rect.right

        brick_box_collisions_x = pygame.sprite.spritecollide(self, level.brick_box_group, False)
        for brick_box in brick_box_collisions_x:
            if self.x_vel > 0:
                self.rect.right = brick_box.rect.left
            elif self.x_vel < 0:
                self.rect.left = brick_box.rect.right

        self.rect.y += self.y_vel
        ground_collisions_y = pygame.sprite.spritecollideany(self, level.ground_group)
        if ground_collisions_y:
            self.rect.bottom = ground_collisions_y.rect.top
            self.y_vel = 0

        coin_box_collisions_y = pygame.sprite.spritecollideany(self, level.coin_box_group)
        if coin_box_collisions_y:
            if self.y_vel < 0:
                self.rect.top = coin_box_collisions_y.rect.bottom
                points, coins = coin_box_collisions_y.activate()
                self.game_info.points += points
                self.game_info.coins += coins
                self.sound_manager.play_sound(c.SOUND_COIN)
            else:
                self.rect.bottom = coin_box_collisions_y.rect.top

            self.y_vel = 0

        brick_box_collisions_y = pygame.sprite.spritecollideany(self, level.brick_box_group)
        if brick_box_collisions_y:
            if self.y_vel < 0:
                self.rect.top = brick_box_collisions_y.rect.bottom
                brick_box_collisions_y.activate()
            else:
                self.rect.bottom = brick_box_collisions_y.rect.top
            self.y_vel = 0

        if self.state == c.STATE_CROUCHING:
            self.image = self.get_player_frame(self.state, self.direction)
        elif self.y_vel != 0:
            self.image = self.get_player_frame(c.STATE_JUMPING, self.direction)
        elif self.x_vel == 0:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        else:
            self.image = self.get_player_frame(c.STATE_WALKING, self.direction, (self.rect.x + self.world_shift) // 30)

    def start_death_sequence(self):
        self.sound_manager.play_music(c.MUSIC_DEATH)
        self.state = c.STATE_TRANSITION
        self.transition_state = c.TRANSITION_DEATH_SEQUENCE
        self.y_vel = -15

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def death_sequence(self, current_time):
        time_delta = current_time - self.transition_timer

        self.image = self.death_frame

        if self.transition_timer == 0:
            self.transition_timer = current_time
        elif time_delta > 3000:
            self.state = c.STATE_DEAD
        else:
            self.transition_timer += 1

    def small_to_big(self, current_time):
        time_delta = current_time - self.transition_timer

        if self.transition_timer == 0:
            self.transition_timer = current_time
            self.image = self.transition_frames[self.direction]
        elif 100 <= time_delta < 200:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 200 <= time_delta < 300:
            self.image = self.transition_frames[self.direction]
        elif 300 <= time_delta < 400:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 400 <= time_delta < 500:
            self.image = self.transition_frames[self.direction]
        elif 500 <= time_delta < 600:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 600 <= time_delta:
            self.power = c.POWER_LARGE
            self.state = c.STATE_STANDING
            self.transition_state = None
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)

        self.transition_timer += 1

    def big_to_small(self, current_time):
        time_delta = current_time - self.transition_timer

        if self.transition_timer == 0:
            self.transition_timer = current_time
            self.image = self.transition_frames[self.direction]
        elif 100 <= time_delta < 200:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 200 <= time_delta < 300:
            self.image = self.transition_frames[self.direction]
        elif 300 <= time_delta < 400:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 400 <= time_delta < 500:
            self.image = self.transition_frames[self.direction]
        elif 500 <= time_delta < 600:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
        elif 600 <= time_delta:
            self.power = c.POWER_SMALL
            self.state = c.STATE_STANDING
            self.transition_state = None
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)

        self.transition_timer += 1

    def transition(self, target_power):
        if self.state == c.STATE_TRANSITION:
            return

        self.state = c.STATE_TRANSITION
        self.transition_state = None

        if self.power == c.POWER_SMALL and target_power == c.POWER_LARGE:
            self.transition_state = c.TRANSITION_SMALL_TO_BIG
        elif self.power == c.POWER_LARGE and target_power == c.POWER_SMALL:
            self.transition_state = c.TRANSITION_BIG_TO_SMALL

        self.transition_timer = 0

    def go_right(self):
        self.x_vel = 5
        self.direction = c.DIR_RIGHT
        self.state = c.STATE_WALKING

    def go_left(self):
        self.x_vel = -5
        self.direction = c.DIR_LEFT
        self.state = c.STATE_WALKING

    def jump(self):
        if self.y_vel == 0:
            self.y_vel += -13
            self.sound_manager.play_sound(c.SOUND_SMALL_JUMP)
            self.state = c.STATE_JUMPING

    def crouch(self):
        if self.power != c.POWER_SMALL and self.y_vel == 0 and self.x_vel == 0:
            self.state = c.STATE_CROUCHING

    def stop(self):
        self.x_vel = 0
        self.state = c.STATE_STANDING
