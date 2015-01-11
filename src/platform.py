__author__ = 'jkamuda'

import pygame
import pygame.gfxdraw

from src import constants


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        if constants.DEBUG:
            pygame.gfxdraw.box(screen, self.rect, (100, 0, 0, 127))



