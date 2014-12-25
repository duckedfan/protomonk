__author__ = 'jkamuda'

import pygame
import os


def scale_image(image, multiplier):
    width = image.get_rect().width
    height = image.get_rect().height
    return pygame.transform.scale(image, (int(width * multiplier), int(height * multiplier)))


def load_music_resources(directory, ext_filter):
        resources = {}
        for file in os.listdir(directory):
            name,ext = os.path.splitext(file)
            if ext.lower() in ext_filter:
                resources[name] = os.path.join(directory, file)
        return resources