__author__ = 'jkamuda'

import pygame


def scale_image(image, multiplier):
    width = image.get_rect().width
    height = image.get_rect().height

    return pygame.transform.scale(image, (int(width * multiplier), int(height * multiplier)))

