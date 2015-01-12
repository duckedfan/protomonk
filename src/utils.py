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
        name, ext = os.path.splitext(file)
        if ext.lower() in ext_filter:
            resources[name] = os.path.join(directory, file)
    return resources


def get_digits(value, num_digits=None):
    if num_digits is None:
        num_digits = len(str(value))

    digits = []
    for i in range(0, num_digits):
        digits.append(value % 10)
        value = int(value / 10)
    return digits


def get_digit_chars(value, num_digits=None):
    digits = get_digits(value, num_digits)
    digit_chars = []
    for digit in digits:
        digit_chars.append(str(digit))

    return digit_chars