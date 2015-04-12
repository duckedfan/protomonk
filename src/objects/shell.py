__author__ = 'jkamuda'

import pygame
import src.constants as c
from src.spritesheet import SpriteSheet
import src.coordinates as coords


class Shell(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.type = type
        self.direction = c.DIR_NONE

        self.shell_frame = None
        self.x_vel = 2
        self.y_vel = 0
        self.state = c.ENEMY_STATE_ALIVE
        self.enemy_time = 0

        self.init_frames()
        self.refresh_image(self.shell_frame)

    def refresh_image(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def refresh_rect(self):
        bottom = self.rect.bottom
        left = self.rect.left
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left

    def init_frames(self):
        sprite_sheet = SpriteSheet("data/characters.gif")

        self.shell_frame = sprite_sheet.get_image(coords.SHELL_GREEN, c.IMG_MULTIPLIER, c.BLUE)

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def kill_shell(self):
        self.state = c.ENEMY_STATE_DEAD

    def update(self, game_time, viewport):
        time_delta = game_time - self.enemy_time
        if self.state == c.ENEMY_STATE_DEAD:
            self.kill()
        elif self.state == c.ENEMY_STATE_ALIVE:
            if time_delta > 250:
                self.enemy_time = game_time

            self.calc_gravity()
            if self.direction == c.DIR_NONE:
                x_change = 0
            elif self.direction == c.DIR_RIGHT:
                x_change = self.x_vel
            else:
                x_change = self.x_vel * -1

            self.x += x_change
            self.rect.y += self.y_vel

        self.refresh_rect()
        self.rect.x = self.x + viewport