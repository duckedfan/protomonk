__author__ = 'Admin'

import pygame
import constants
from platform import Platform
from tools import *


class Level():

    background = None
    player = None

    def __init__(self, player):
        # Init background
        self.background = pygame.image.load("data/levels/level_1.png").convert()
        self.background = scale_image(self.background, constants.IMG_MULTIPLIER)

        self.background.set_colorkey(constants.WHITE)

        self.player = player

        self.init_platforms()

    def init_platforms(self):

        # Ground
        # TODO absract away the level width
        ground_rect = Platform(0, constants.GROUND_HEIGHT, 2000, 60)

        self.ground_group = pygame.sprite.Group(ground_rect)

    def draw(self, screen):
        screen.fill(constants.BLUE)
        screen.blit(self.background, (0, 0))

    def update(self):
        ground_collisions = pygame.sprite.spritecollideany(self.player, self.ground_group)
        if ground_collisions:
            print "ground collision"