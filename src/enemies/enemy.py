__author__ = 'jkamuda'

import pygame
import src.constants as c
from src.score import Score


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, kill_score):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.kill_score = kill_score
        self.y_vel = 0
        self.x_vel = 0
        self.frame_idx = 0
        self.enemy_time = 0
        self.dead = False
        self.direction = c.DIR_RIGHT
        self.image = None
        self.rect = None
        self.state = c.ENEMY_STATE_ALIVE

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

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def kill_enemy(self, score_group):
        self.state = c.ENEMY_STATE_DEAD
        score = Score(self.rect.x + 5, self.rect.y - 25, self.kill_score)
        score_group.add(score)
        return self.kill_score