__author__ = 'jkamuda'

import src.constants as c
from src.spritesheet import SpriteSheet
from src.utils import *
from src import coordinates as coords


class Player(pygame.sprite.Sprite):
    def __init__(self, sound_manager, game_info):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager
        self.game_info = game_info

        self.state = c.STATE_STANDING
        self.power = c.POWER_SMALL
        self.direction = c.DIR_RIGHT
        self.world_shift = 0

        self.transition_state = None
        self.transition_timer = 0

        self.player_small_frames = {}
        self.player_frames = {}
        self.transition_frames = {}
        self.death_frame = None

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
        self.transition_frames = dict((key, []) for key in dir_keys)

        # Standing frames
        small_standing_left = self.sprite_sheet.get_image(coords.MARIO_SMALL_STANDING_LEFT, c.IMG_MULTIPLIER)
        small_standing_right = self.sprite_sheet.get_image(coords.MARIO_SMALL_STANDING_RIGHT, c.IMG_MULTIPLIER)
        self.player_small_frames[c.STATE_STANDING][c.DIR_LEFT].append(small_standing_left)
        self.player_small_frames[c.STATE_STANDING][c.DIR_RIGHT].append(small_standing_right)

        # Jumping frames
        small_jumping_left = self.sprite_sheet.get_image(coords.MARIO_SMALL_JUMPING_LEFT, c.IMG_MULTIPLIER)
        small_jumping_right = self.sprite_sheet.get_image(coords.MARIO_SMALL_JUMPING_RIGHT, c.IMG_MULTIPLIER)
        self.player_small_frames[c.STATE_JUMPING][c.DIR_LEFT].append(small_jumping_left)
        self.player_small_frames[c.STATE_JUMPING][c.DIR_RIGHT].append(small_jumping_right)

        # Transition frames
        self.transition_frames[c.DIR_LEFT] = self.sprite_sheet.get_image(coords.MARIO_TRANSITION_MID_LEFT, c.IMG_MULTIPLIER)
        self.transition_frames[c.DIR_RIGHT] = self.sprite_sheet.get_image(coords.MARIO_TRANSITION_MID_RIGHT, c.IMG_MULTIPLIER)

        # Death frame
        self.death_frame = self.sprite_sheet.get_image(coords.MARIO_DEAD, c.IMG_MULTIPLIER)

        # Walking frames
        right_1 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_RIGHT_1, c.IMG_MULTIPLIER)
        right_2 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_RIGHT_2, c.IMG_MULTIPLIER)
        right_3 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_RIGHT_3, c.IMG_MULTIPLIER)

        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_1)
        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_2)
        self.player_small_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_3)

        left_1 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_LEFT_1, c.IMG_MULTIPLIER)
        left_2 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_LEFT_2, c.IMG_MULTIPLIER)
        left_3 = self.sprite_sheet.get_image(coords.MARIO_SMALL_WALKING_LEFT_3, c.IMG_MULTIPLIER)

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
        big_standing_left = self.sprite_sheet.get_image(coords.MARIO_BIG_STANDING_LEFT, c.IMG_MULTIPLIER)
        big_standing_right = self.sprite_sheet.get_image(coords.MARIO_BIG_STANDING_RIGHT, c.IMG_MULTIPLIER)
        self.player_frames[c.STATE_STANDING][c.DIR_LEFT].append(big_standing_left)
        self.player_frames[c.STATE_STANDING][c.DIR_RIGHT].append(big_standing_right)

        # Jumping frames
        big_jumping_left = self.sprite_sheet.get_image(coords.MARIO_BIG_JUMPING_LEFT, c.IMG_MULTIPLIER)
        big_jumping_right = self.sprite_sheet.get_image(coords.MARIO_BIG_JUMPING_RIGHT, c.IMG_MULTIPLIER)
        self.player_frames[c.STATE_JUMPING][c.DIR_LEFT].append(big_jumping_left)
        self.player_frames[c.STATE_JUMPING][c.DIR_RIGHT].append(big_jumping_right)

        # Crouching frames
        big_crouching_left = self.sprite_sheet.get_image(coords.MARIO_BIG_CROUCHING_LEFT, c.IMG_MULTIPLIER)
        big_crouching_right = self.sprite_sheet.get_image(coords.MARIO_BIG_CROUCHING_RIGHT, c.IMG_MULTIPLIER)
        self.player_frames[c.STATE_CROUCHING][c.DIR_LEFT].append(big_crouching_left)
        self.player_frames[c.STATE_CROUCHING][c.DIR_RIGHT].append(big_crouching_right)

        # Walking frames
        right_1 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_RIGHT_1, c.IMG_MULTIPLIER)
        right_2 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_RIGHT_2, c.IMG_MULTIPLIER)
        right_3 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_RIGHT_3, c.IMG_MULTIPLIER)

        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_1)
        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_2)
        self.player_frames[c.STATE_WALKING][c.DIR_RIGHT].append(right_3)

        left_1 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_LEFT_1, c.IMG_MULTIPLIER)
        left_2 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_LEFT_2, c.IMG_MULTIPLIER)
        left_3 = self.sprite_sheet.get_image(coords.MARIO_BIG_WALKING_LEFT_3, c.IMG_MULTIPLIER)

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

        # TODO group all these collision groups together

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
            else:
                self.rect.bottom = coin_box_collisions_y.rect.top

            self.y_vel = 0

        brick_box_collisions_y = pygame.sprite.spritecollideany(self, level.brick_box_group)
        if brick_box_collisions_y:
            if self.y_vel < 0:
                self.rect.top = brick_box_collisions_y.rect.bottom
                brick_box_collisions_y.activate()
                brick_box_collisions_y.update(current_time)
            else:
                self.rect.bottom = brick_box_collisions_y.rect.top
            self.y_vel = 0

        if self.state == c.STATE_CROUCHING:
            self.image = self.get_player_frame(self.state, self.direction)
            self.refresh_rect()
        elif self.y_vel != 0:
            self.image = self.get_player_frame(c.STATE_JUMPING, self.direction)
        elif self.x_vel == 0:
            self.image = self.get_player_frame(c.STATE_STANDING, self.direction)
            self.refresh_rect()
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
