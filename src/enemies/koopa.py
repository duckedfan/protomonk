__author__ = 'jkamuda'

from enemy import Enemy
from src.spritesheet import SpriteSheet
import src.constants as c
import src.coordinates as coords

class Koopa(Enemy):
    def __init__(self, x, y, direction=c.DIR_LEFT):
        Enemy.__init__(self, x, y, c.SCORE_KOOPA, direction)

        self.koopa_frames = []
        self.x_vel = 1.5

        self.init_frames()
        self.refresh_image(self.koopa_frames[0])

    def init_frames(self):
        sprite_sheet = SpriteSheet("data/characters.gif")

        self.koopa_frames.append(sprite_sheet.get_image(coords.KOOPA_GREEN_LEFT_1, c.IMG_MULTIPLIER, c.BLUE))
        self.koopa_frames.append(sprite_sheet.get_image(coords.KOOPA_GREEN_LEFT_2, c.IMG_MULTIPLIER, c.BLUE))

    def update(self, game_time, viewport):
        time_delta = game_time - self.enemy_time
        if self.state == c.ENEMY_STATE_DEAD:
            self.kill()
            # TODO replace dead koopa with shell
        elif self.state == c.ENEMY_STATE_ALIVE:
            if time_delta > 250:
                if self.frame_idx == 0:
                    self.frame_idx = 1
                else:
                    self.frame_idx = 0
                self.enemy_time = game_time
            self.image = self.koopa_frames[self.frame_idx]

            self.calc_gravity()
            if self.direction == c.DIR_RIGHT:
                x_change = self.x_vel
            else:
                x_change = self.x_vel * -1

            self.x += x_change
            self.rect.y += self.y_vel

        self.refresh_rect()
        self.rect.x = self.x + viewport