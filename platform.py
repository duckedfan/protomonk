__author__ = 'jkamuda'

import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


