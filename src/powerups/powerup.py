__author__ = 'jkamuda'

import pygame
import src.constants as c


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.y_vel = 0
        self.x_vel = 0
        self.frame_idx = 0
        self.power_time = 0
        self.direction = c.DIR_RIGHT
        self.image = None
        self.rect = None
        self.display_frame = None
        self.emerging = True

    def refresh_image(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def shift_world(self, shift):
        self.rect.x += shift

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x, self.rect.y))