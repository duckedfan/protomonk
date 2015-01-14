__author__ = 'jkamuda'

import pygame
from enemy import Enemy
from src.spritesheet import SpriteSheet
import src.constants as c
import src.coordinates as coords


class Goomba(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self)

        self.frames = []
        self.dead_frame = None
        self.enemy_time = 0
        self.frame_idx = 0
        self.dead = False
        self.display_frame = None
        self.y_vel = 0
        self.x_vel = 2
        self.direction = c.DIR_RIGHT
        self.shift = 0

        self.init_frames()

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\characters.gif")

        self.frames.append(sprite_sheet.get_image(coords.GOOMBA_LEFT, c.IMG_MULTIPLIER, c.BLACK))
        self.frames.append(sprite_sheet.get_image(coords.GOOMBA_RIGHT, c.IMG_MULTIPLIER, c.BLACK))
        self.dead_frame = sprite_sheet.get_image(coords.GOOMBA_DEAD, c.IMG_MULTIPLIER, c.WHITE)

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def shift_world(self, shift):
        self.rect.x += shift

    def update(self, game_time, platform_group, player):
        time_delta = game_time - self.enemy_time
        if time_delta > 50:
            if self.frame_idx == 0:
                self.frame_idx = 1
            else:
                self.frame_idx = 0
            self.enemy_time = game_time
        self.display_frame = self.frames[self.frame_idx]

        self.calc_gravity()
        if self.direction == c.DIR_RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.check_platform_collisions(platform_group)
        self.check_mario_collisions(player)

    def check_platform_collisions(self, platform_group):
        collisions_y = pygame.sprite.spritecollideany(self, platform_group)
        if collisions_y:
            if self.y_vel < 0:
                self.rect.top = collisions_y.rect.bottom
            else:
                self.rect.bottom = collisions_y.rect.top
            self.y_vel = 0

        collisions_x = pygame.sprite.spritecollide(self, platform_group, False)
        for collision in collisions_x:
            if self.x_vel > 0:
                self.rect.right = collision.rect.left
                self.direction = c.DIR_LEFT
            elif self.x_vel < 0:
                self.rect.left = collision.rect.right
                self.direction = c.DIR_RIGHT

    def check_mario_collisions(self, player):
        player_collision = pygame.sprite.collide_rect(self, player)
        if player_collision:
            pass

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x + self.shift, self.rect.y))
