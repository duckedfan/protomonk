__author__ = 'jkamuda'

import pygame
from src.spritesheet import SpriteSheet
from src import coordinates as coords
from src import constants as c


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data\item_objects.png")

        self.mushroom_frame = sprite_sheet.get_image(coords.MUSHROOM_POWERUP, c.IMG_MULTIPLIER, c.BLACK)
        self.image = self.mushroom_frame
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_cap = self.rect.y - self.rect.height
        self.y_vel = 0
        self.x_vel = 2
        self.direction = c.DIR_RIGHT
        self.emerging = True

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += .45

    def shift_world(self, shift):
        self.rect.x += shift

    def update(self, game_time, platform_group, player):
        if self.emerging:
            self.rect.y -= .5
            if self.rect.y < self.y_cap:
                self.emerging = False
        else:
            self.calc_gravity()
            if self.direction == c.DIR_RIGHT:
                self.x_vel = 2
            else:
                self.x_vel = -2

            self.rect.x += self.x_vel
            self.rect.y += self.y_vel
            self.check_platform_collisions(platform_group)
            self.check_player_collisions(player)

    def check_platform_collisions(self, platform_group):
        collisions_y = pygame.sprite.spritecollideany(self, platform_group)
        if collisions_y:
            if self.y_vel < 0:
                self.rect.top = collisions_y.rect.bottom
            else:
                self.rect.bottom = collisions_y.rect.top
            self.y_vel = 0

        collisions_x = pygame.sprite.spritecollide(self, platform_group, False)
        for collision in collisions_x:
            if self.x_vel > 0:
                self.rect.right = collision.rect.left
                self.direction = c.DIR_LEFT
            elif self.x_vel < 0:
                self.rect.left = collision.rect.right
                self.direction = c.DIR_RIGHT

    def check_player_collisions(self, player):
        player_collision = pygame.sprite.collide_rect(self, player)
        if player_collision:
            player.powerup(c.POWERUP_MUSHROOM)
            self.kill()

    def draw(self, screen):
        screen.blit(self.mushroom_frame, (self.rect.x, self.rect.y))
