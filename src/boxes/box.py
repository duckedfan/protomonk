__author__ = 'jkamuda'

import pygame


class Box(pygame.sprite.Sprite):
    def __init__(self, sound_manager, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager
        self.x = x
        self.y = y
        self.y_offset = 0
        self.image = None
        self.rect = None
        self.shift = 0
        self.display_frame = None
        self.in_transition = False

    def refresh_image(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def shift_world(self, shift):
        self.rect.x += shift

    def init_frames(self):
        pass

    def activate(self):
        pass

    def update(self, game_time):
        pass

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x, self.rect.y - self.y_offset))