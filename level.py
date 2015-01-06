__author__ = 'Admin'

import constants
from platform import Platform
from utils import *
from coin_box import CoinBox
from coin import Coin
from brick_box import BrickBox


class Level():

    world_shift = 0
    background = None
    player = None

    ground_group = None

    def __init__(self, player):
        # Init background
        self.background = pygame.image.load("data/levels/level_1.png").convert()
        self.background = scale_image(self.background, constants.IMG_MULTIPLIER)

        self.background.set_colorkey(constants.WHITE)

        self.player = player

        self.init_platforms()
        self.init_boxes()

    def init_boxes(self):
        # TODO is temp
        # Coins
        self.coin_test = Coin(100, 100)

        # Coin boxes
        self.coin_box_group = pygame.sprite.Group()
        self.coin_box_group.add(CoinBox(640, 330))
        self.coin_box_group.add(CoinBox(880, 330))
        self.coin_box_group.add(CoinBox(960, 330))
        self.coin_box_group.add(CoinBox(920, 200))

        # Brick boxes
        self.brick_box_group = pygame.sprite.Group()
        self.brick_box_group.add(BrickBox(840, 330))
        self.brick_box_group.add(BrickBox(920, 330))
        self.brick_box_group.add(BrickBox(1000, 330))

    def init_platforms(self):

        # Ground
        # TODO absract away the level width
        ground_rect1 = Platform(0, constants.GROUND_HEIGHT, 2760, 62)
        ground_rect2 = Platform(2840, constants.GROUND_HEIGHT, 600, 62)
        ground_rect3 = Platform(3560, constants.GROUND_HEIGHT, 2560, 62)
        ground_rect4 = Platform(6200, constants.GROUND_HEIGHT, 2280, 62)

        self.ground_group = pygame.sprite.Group(ground_rect1, ground_rect2, ground_rect3, ground_rect4)

        # Pipes
        pipe1 = Platform(1120, constants.GROUND_HEIGHT - constants.PIPE_SMALL_H, constants.PIPE_W, constants.PIPE_SMALL_H)
        pipe2 = Platform(1520, constants.GROUND_HEIGHT - constants.PIPE_MED_H, constants.PIPE_W, constants.PIPE_MED_H)
        pipe3 = Platform(1840, constants.GROUND_HEIGHT - constants.PIPE_LARGE_H, constants.PIPE_W, constants.PIPE_LARGE_H)
        pipe4 = Platform(2280, constants.GROUND_HEIGHT - constants.PIPE_LARGE_H, constants.PIPE_W, constants.PIPE_LARGE_H)
        pipe5 = Platform(6520, constants.GROUND_HEIGHT - constants.PIPE_SMALL_H, constants.PIPE_W, constants.PIPE_SMALL_H)
        pipe6 = Platform(7160, constants.GROUND_HEIGHT - constants.PIPE_SMALL_H, constants.PIPE_W, constants.PIPE_SMALL_H)

        pipe_group = pygame.sprite.Group(pipe1, pipe2, pipe3, pipe4, pipe5, pipe6)

        # Bricks
        brick_set1_1 = Platform(5360, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W * 4, constants.BRICK_H)
        brick_set1_2 = Platform(5400, constants.GROUND_HEIGHT - (constants.BRICK_H * 2), constants.BRICK_W * 3, constants.BRICK_H)
        brick_set1_3 = Platform(5440, constants.GROUND_HEIGHT - (constants.BRICK_H * 3), constants.BRICK_W * 2, constants.BRICK_H)
        brick_set1_4 = Platform(5480, constants.GROUND_HEIGHT - (constants.BRICK_H * 4), constants.BRICK_W, constants.BRICK_H)

        brick_set1_group = pygame.sprite.Group(brick_set1_1, brick_set1_2, brick_set1_3, brick_set1_4)

        brick_set2_1 = Platform(5600, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W * 4, constants.BRICK_H)
        brick_set2_2 = Platform(5600, constants.GROUND_HEIGHT - (constants.BRICK_H * 2), constants.BRICK_W * 3, constants.BRICK_H)
        brick_set2_3 = Platform(5600, constants.GROUND_HEIGHT - (constants.BRICK_H * 3), constants.BRICK_W * 2, constants.BRICK_H)
        brick_set2_4 = Platform(5600, constants.GROUND_HEIGHT - (constants.BRICK_H * 4), constants.BRICK_W, constants.BRICK_H)

        brick_set2_group = pygame.sprite.Group(brick_set2_1, brick_set2_2, brick_set2_3, brick_set2_4)

        brick_set3_1 = Platform(5920, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W * 5, constants.BRICK_H)
        brick_set3_2 = Platform(5960, constants.GROUND_HEIGHT - (constants.BRICK_H * 2), constants.BRICK_W * 4, constants.BRICK_H)
        brick_set3_3 = Platform(6000, constants.GROUND_HEIGHT - (constants.BRICK_H * 3), constants.BRICK_W * 3, constants.BRICK_H)
        brick_set3_4 = Platform(6040, constants.GROUND_HEIGHT - (constants.BRICK_H * 4), constants.BRICK_W * 2, constants.BRICK_H)

        brick_set3_group = pygame.sprite.Group(brick_set3_1, brick_set3_2, brick_set3_3, brick_set3_4)

        brick_set4_1 = Platform(6200, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W * 4, constants.BRICK_H)
        brick_set4_2 = Platform(6200, constants.GROUND_HEIGHT - (constants.BRICK_H * 2), constants.BRICK_W * 3, constants.BRICK_H)
        brick_set4_3 = Platform(6200, constants.GROUND_HEIGHT - (constants.BRICK_H * 3), constants.BRICK_W * 2, constants.BRICK_H)
        brick_set4_4 = Platform(6200, constants.GROUND_HEIGHT - (constants.BRICK_H * 4), constants.BRICK_W, constants.BRICK_H)

        brick_set4_group = pygame.sprite.Group(brick_set4_1, brick_set4_2, brick_set4_3, brick_set4_4)

        brick_set5_1 = Platform(7240, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W * 9, constants.BRICK_H)
        brick_set5_2 = Platform(7280, constants.GROUND_HEIGHT - (constants.BRICK_H * 2), constants.BRICK_W * 8, constants.BRICK_H)
        brick_set5_3 = Platform(7320, constants.GROUND_HEIGHT - (constants.BRICK_H * 3), constants.BRICK_W * 7, constants.BRICK_H)
        brick_set5_4 = Platform(7360, constants.GROUND_HEIGHT - (constants.BRICK_H * 4), constants.BRICK_W * 6, constants.BRICK_H)
        brick_set5_5 = Platform(7400, constants.GROUND_HEIGHT - (constants.BRICK_H * 5), constants.BRICK_W * 5, constants.BRICK_H)
        brick_set5_6 = Platform(7440, constants.GROUND_HEIGHT - (constants.BRICK_H * 6), constants.BRICK_W * 4, constants.BRICK_H)
        brick_set5_7 = Platform(7480, constants.GROUND_HEIGHT - (constants.BRICK_H * 7), constants.BRICK_W * 3, constants.BRICK_H)
        brick_set5_8 = Platform(7520, constants.GROUND_HEIGHT - (constants.BRICK_H * 8), constants.BRICK_W * 2, constants.BRICK_H)

        brick_set5_group = pygame.sprite.Group(brick_set5_1, brick_set5_2, brick_set5_3, brick_set5_4, brick_set5_5, brick_set5_6, brick_set5_7, brick_set5_8)

        brick_set6_1 = Platform(7920, constants.GROUND_HEIGHT - constants.BRICK_H, constants.BRICK_W, constants.BRICK_H)

        brick_set6_group = pygame.sprite.Group(brick_set6_1)

        # Put it all together naw
        self.ground_group.add(pipe_group)
        self.ground_group.add(brick_set1_group)
        self.ground_group.add(brick_set2_group)
        self.ground_group.add(brick_set3_group)
        self.ground_group.add(brick_set4_group)
        self.ground_group.add(brick_set5_group)
        self.ground_group.add(brick_set6_group)

    def update(self, game_time):
        for coin_box in self.coin_box_group:
            coin_box.update(game_time)

        for brick_box in self.brick_box_group:
            brick_box.update(game_time)

        self.coin_test.update(game_time)

    def draw(self, screen):
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift, 0))

        # TODO yuck i dont like this...
        for block in self.ground_group:
            block.draw(screen)

        for coin_box in self.coin_box_group:
            coin_box.draw(screen)

        for brick_box in self.brick_box_group:
            brick_box.draw(screen)

        self.coin_test.draw(screen)

    def shift_world(self, shift):
        self.world_shift += shift
        for rect in self.ground_group:
            rect.rect.x += shift

        for coin_box in self.coin_box_group:
            coin_box.rect.x += shift

        for brick_box in self.brick_box_group:
            brick_box.rect.x += shift

        self.coin_test.rect.x += shift