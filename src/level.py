__author__ = 'Admin'

from src import constants as c
from src.platform import Platform
from src.utils import *
from src.boxes.coin_box import CoinBox
from src.boxes.brick_box import BrickBox
from src.boxes.powerup_box import PowerupBox
from src.enemies.goomba import Goomba
from checkpoint import Checkpoint
from score import Score


class Level():
    def __init__(self, game_info, player, sound_manager):
        self.game_info = game_info
        self.player = player
        self.sound_manager = sound_manager
        self.background = None
        self.world_shift = 0
        self.viewport = 0

        self.ground_group = None
        self.coin_box_group = None
        self.brick_box_group = None
        self.powerup_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.brick_piece_group = pygame.sprite.Group()
        self.checkpoint_group = pygame.sprite.Group()

        self.init_background()
        self.init_platforms()
        self.init_boxes()
        self.init_checkpoints()

    def init_background(self):
        self.background = pygame.image.load("data/levels/level_1.png").convert()
        self.background = scale_image(self.background, c.IMG_MULTIPLIER)

    def init_boxes(self):
        # TODO test enemies
        self.enemy_group.add(Goomba(700, 330))

        # Coin boxes
        self.coin_box_group = pygame.sprite.Group()
        self.coin_box_group.add(CoinBox(self.sound_manager, 640, 330))
        self.coin_box_group.add(PowerupBox(self.sound_manager, self.powerup_group, 880, 330))
        self.coin_box_group.add(CoinBox(self.sound_manager, 960, 330))
        self.coin_box_group.add(CoinBox(self.sound_manager, 920, 200))

        # Brick boxes
        self.brick_box_group = pygame.sprite.Group()
        self.brick_box_group.add(BrickBox(self.sound_manager, 840, 330))
        self.brick_box_group.add(BrickBox(self.sound_manager, 920, 330))
        self.brick_box_group.add(BrickBox(self.sound_manager, 1000, 330))

        self.platform_group.add(self.coin_box_group)
        self.platform_group.add(self.brick_box_group)

    def init_platforms(self):
        # Ground
        # TODO abstract away the level width
        ground_rect1 = Platform(0, c.GROUND_HEIGHT, 2760, 62)
        ground_rect2 = Platform(2840, c.GROUND_HEIGHT, 600, 62)
        ground_rect3 = Platform(3560, c.GROUND_HEIGHT, 2560, 62)
        ground_rect4 = Platform(6200, c.GROUND_HEIGHT, 2280, 62)

        self.ground_group = pygame.sprite.Group(ground_rect1, ground_rect2, ground_rect3, ground_rect4)

        # Pipes
        pipe1 = Platform(1120, c.GROUND_HEIGHT - c.PIPE_SMALL_H, c.PIPE_W, c.PIPE_SMALL_H)
        pipe2 = Platform(1520, c.GROUND_HEIGHT - c.PIPE_MED_H, c.PIPE_W, c.PIPE_MED_H)
        pipe3 = Platform(1840, c.GROUND_HEIGHT - c.PIPE_LARGE_H, c.PIPE_W, c.PIPE_LARGE_H)
        pipe4 = Platform(2280, c.GROUND_HEIGHT - c.PIPE_LARGE_H, c.PIPE_W, c.PIPE_LARGE_H)
        pipe5 = Platform(6520, c.GROUND_HEIGHT - c.PIPE_SMALL_H, c.PIPE_W, c.PIPE_SMALL_H)
        pipe6 = Platform(7160, c.GROUND_HEIGHT - c.PIPE_SMALL_H, c.PIPE_W, c.PIPE_SMALL_H)

        pipe_group = pygame.sprite.Group(pipe1, pipe2, pipe3, pipe4, pipe5, pipe6)

        # Bricks
        brick_set1_1 = Platform(5360, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W * 4, c.BRICK_H)
        brick_set1_2 = Platform(5400, c.GROUND_HEIGHT - (c.BRICK_H * 2), c.BRICK_W * 3, c.BRICK_H)
        brick_set1_3 = Platform(5440, c.GROUND_HEIGHT - (c.BRICK_H * 3), c.BRICK_W * 2, c.BRICK_H)
        brick_set1_4 = Platform(5480, c.GROUND_HEIGHT - (c.BRICK_H * 4), c.BRICK_W, c.BRICK_H)

        brick_set1_group = pygame.sprite.Group(brick_set1_1, brick_set1_2, brick_set1_3, brick_set1_4)

        brick_set2_1 = Platform(5600, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W * 4, c.BRICK_H)
        brick_set2_2 = Platform(5600, c.GROUND_HEIGHT - (c.BRICK_H * 2), c.BRICK_W * 3, c.BRICK_H)
        brick_set2_3 = Platform(5600, c.GROUND_HEIGHT - (c.BRICK_H * 3), c.BRICK_W * 2, c.BRICK_H)
        brick_set2_4 = Platform(5600, c.GROUND_HEIGHT - (c.BRICK_H * 4), c.BRICK_W, c.BRICK_H)

        brick_set2_group = pygame.sprite.Group(brick_set2_1, brick_set2_2, brick_set2_3, brick_set2_4)

        brick_set3_1 = Platform(5920, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W * 5, c.BRICK_H)
        brick_set3_3 = Platform(6000, c.GROUND_HEIGHT - (c.BRICK_H * 3), c.BRICK_W * 3, c.BRICK_H)
        brick_set3_2 = Platform(5960, c.GROUND_HEIGHT - (c.BRICK_H * 2), c.BRICK_W * 4, c.BRICK_H)
        brick_set3_4 = Platform(6040, c.GROUND_HEIGHT - (c.BRICK_H * 4), c.BRICK_W * 2, c.BRICK_H)

        brick_set3_group = pygame.sprite.Group(brick_set3_1, brick_set3_2, brick_set3_3, brick_set3_4)

        brick_set4_1 = Platform(6200, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W * 4, c.BRICK_H)
        brick_set4_2 = Platform(6200, c.GROUND_HEIGHT - (c.BRICK_H * 2), c.BRICK_W * 3, c.BRICK_H)
        brick_set4_3 = Platform(6200, c.GROUND_HEIGHT - (c.BRICK_H * 3), c.BRICK_W * 2, c.BRICK_H)
        brick_set4_4 = Platform(6200, c.GROUND_HEIGHT - (c.BRICK_H * 4), c.BRICK_W, c.BRICK_H)

        brick_set4_group = pygame.sprite.Group(brick_set4_1, brick_set4_2, brick_set4_3, brick_set4_4)

        brick_set5_1 = Platform(7240, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W * 9, c.BRICK_H)
        brick_set5_2 = Platform(7280, c.GROUND_HEIGHT - (c.BRICK_H * 2), c.BRICK_W * 8, c.BRICK_H)
        brick_set5_3 = Platform(7320, c.GROUND_HEIGHT - (c.BRICK_H * 3), c.BRICK_W * 7, c.BRICK_H)
        brick_set5_4 = Platform(7360, c.GROUND_HEIGHT - (c.BRICK_H * 4), c.BRICK_W * 6, c.BRICK_H)
        brick_set5_5 = Platform(7400, c.GROUND_HEIGHT - (c.BRICK_H * 5), c.BRICK_W * 5, c.BRICK_H)
        brick_set5_6 = Platform(7440, c.GROUND_HEIGHT - (c.BRICK_H * 6), c.BRICK_W * 4, c.BRICK_H)
        brick_set5_7 = Platform(7480, c.GROUND_HEIGHT - (c.BRICK_H * 7), c.BRICK_W * 3, c.BRICK_H)
        brick_set5_8 = Platform(7520, c.GROUND_HEIGHT - (c.BRICK_H * 8), c.BRICK_W * 2, c.BRICK_H)

        brick_set5_group = pygame.sprite.Group(brick_set5_1, brick_set5_2, brick_set5_3, brick_set5_4, \
                                               brick_set5_5, brick_set5_6, brick_set5_7, brick_set5_8)

        brick_set6_1 = Platform(7920, c.GROUND_HEIGHT - c.BRICK_H, c.BRICK_W, c.BRICK_H)

        brick_set6_group = pygame.sprite.Group(brick_set6_1)

        # Put it all together naw
        self.ground_group.add(pipe_group)
        self.ground_group.add(brick_set1_group)
        self.ground_group.add(brick_set2_group)
        self.ground_group.add(brick_set3_group)
        self.ground_group.add(brick_set4_group)
        self.ground_group.add(brick_set5_group)
        self.ground_group.add(brick_set6_group)

        self.platform_group.add(self.ground_group)

    def init_checkpoints(self):
        self.checkpoint_group.add(Checkpoint("goomba_set_1", 1200))

    def update(self, game_time):
        if self.player.rect.right >= c.SCREEN_WIDTH_MID:
            diff = self.player.rect.right - c.SCREEN_WIDTH_MID
            self.shift_world(-diff)
            self.player.shift(diff)
            self.world_shift += diff
            self.viewport -= diff
            self.player.rect.right = c.SCREEN_WIDTH_MID

        if self.player.rect.left <= c.SCREEN_WIDTH_START:
            self.player.rect.left = c.SCREEN_WIDTH_START

        self.player.update(self, game_time)
        self.coin_box_group.update(game_time)
        self.brick_box_group.update(game_time)
        self.brick_piece_group.update(game_time)
        self.powerup_group.update(game_time, self.viewport)
        self.enemy_group.update(game_time, self.viewport)

        for score in self.score_group:
            score.update(game_time)

        # Powerup collisions
        for powerup in self.powerup_group:
            if not powerup.emerging:
                self.check_platform_collisions(powerup)
            self.check_player_powerup_collisions(powerup)

        # Platform collisions
        for enemy in self.enemy_group:
            self.check_platform_collisions(enemy)

        # Player collisions
        self.check_player_enemy_collisions()

        self.check_player_checkpoint_collisions()

    def check_player_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
        for enemy in enemy_collisions:
            if enemy.state is c.ENEMY_STATE_ALIVE:
                if self.player.y_vel > 0:
                    self.player.y_vel = -10
                    self.player.rect.bottom = enemy.rect.top
                    self.sound_manager.play_sound(c.SOUND_STOMP)
                    self.game_info.points += enemy.kill_enemy(self.score_group)
                else:
                    if self.player.power == c.POWER_SMALL:
                        self.player.start_death_sequence()
                    else:
                        self.player.transition(c.POWER_SMALL)


    def check_player_powerup_collisions(self, powerup):
        player_collision = pygame.sprite.collide_rect(powerup, self.player)
        if player_collision:
            self.player.powerup(c.POWERUP_MUSHROOM)
            self.game_info.points += c.SCORE_POWERUP
            score = Score(powerup.rect.x + 5, powerup.rect.y - 25, c.SCORE_POWERUP)
            self.score_group.add(score)
            powerup.kill()

    def check_player_checkpoint_collisions(self):
        checkpoint_collisions = pygame.sprite.spritecollide(self.player, self.checkpoint_group, True)
        for checkpoint in checkpoint_collisions:
            if checkpoint.name == "goomba_set_1":
                self.enemy_group.add(Goomba(1700, 330))
                self.enemy_group.add(Goomba(2050, 330))
                self.enemy_group.add(Goomba(2100, 330))


    def check_platform_collisions(self, sprite):
        collisions_y = pygame.sprite.spritecollideany(sprite, self.platform_group)
        if collisions_y:
            if sprite.y_vel < 0:
                sprite.rect.top = collisions_y.rect.bottom
            else:
                sprite.rect.bottom = collisions_y.rect.top
            sprite.y_vel = 0

        collisions_x = pygame.sprite.spritecollide(sprite, self.platform_group, False)
        for collision in collisions_x:
            if sprite.x_vel > 0:
                sprite.rect.right = collision.rect.left
                sprite.direction = c.DIR_LEFT
            elif sprite.x_vel < 0:
                sprite.rect.left = collision.rect.right
                sprite.direction = c.DIR_RIGHT

    def draw(self, screen):
        screen.fill(c.WHITE)
        screen.blit(self.background, (self.viewport, 0))

        # TODO yuck i dont like this...
        for block in self.ground_group:
            block.draw(screen)

        for powerup in self.powerup_group:
            powerup.draw(screen)

        for coin_box in self.coin_box_group:
            coin_box.draw(screen)

        for brick_box in self.brick_box_group:
            brick_box.draw(screen)

        self.enemy_group.draw(screen)
        self.brick_piece_group.draw(screen)

        if c.DEBUG:
            self.checkpoint_group.draw(screen)

        for score in self.score_group:
            score.draw(screen)

    def shift_world(self, shift):
        self.world_shift += shift

        for powerup in self.powerup_group:
            powerup.shift_world(shift)

        for rect in self.ground_group:
            rect.rect.x += shift

        for coin_box in self.coin_box_group:
            coin_box.shift_world(shift)

        for brick_box in self.brick_box_group:
            brick_box.shift_world(shift)

        for brick_piece in self.brick_piece_group:
            brick_piece.shift_world(shift)

        for score in self.score_group:
            score.shift_world(shift)

        for checkpoint in self.checkpoint_group:
            checkpoint.shift_world(shift)
