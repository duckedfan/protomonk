__author__ = 'Admin'

import pygame
import constants as c


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, name, x_trigger):
        pygame.sprite.Sprite.__init__(self)

        width = 20
        height = c.GROUND_HEIGHT
        self.name = name
        self.rect = pygame.Rect(x_trigger, 0, x_trigger + width, height)

        self.image = pygame.Surface((width, height))
        self.image.fill(c.BLACK)

    def shift_world(self, shift):
        self.rect.x += shift