__author__ = 'jkamuda'

import pygame

from game_state import GameState
import constants
from src.level import Level
from src.player import Player


class MarioGame(GameState):
    def __init__(self, game_info, sound_manager):
        GameState.__init__(self, GameState.STATE_GAME, GameState.STATE_LOAD)

        self.game_info = game_info
        self.sound_manager = sound_manager

        self.game_info.set_timer_in_seconds(300)

        self.mario_game_time = -1
        self.world_shift = 0

        self.player = Player(self.sound_manager, game_info)

        self.active_sprite_list = pygame.sprite.Group()
        self.active_sprite_list.add(self.player)

        self.level = Level(self.player)
        
        #self.sound_manager.play_music(constants.MUSIC_MAIN_THEME)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_LEFT:
                    self.player.go_left()
                if key == pygame.K_RIGHT:
                    self.player.go_right()
                if key == pygame.K_UP:
                    self.player.jump()
                if key == pygame.K_DOWN:
                    self.player.crouch()
                if key == pygame.K_a:
                    self.player.transition(constants.POWER_LARGE)
                if key == pygame.K_s:
                    self.player.transition(constants.POWER_SMALL)
                if key == pygame.K_t:
                    self.player.start_death_sequence()
                if key == pygame.K_ESCAPE or key == pygame.K_q:
                    # TODO should be pause
                    pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.x_vel < 0:
                    self.player.stop()
                if event.key == pygame.K_RIGHT and self.player.x_vel > 0:
                    self.player.stop()
                if event.key == pygame.K_DOWN:
                    self.player.stop()

    def update(self, game_time):
        if self.mario_game_time == -1:
            self.mario_game_time = game_time
        else:
            self.game_info.timer -= (game_time - self.mario_game_time)
            self.mario_game_time = game_time

        if self.player.rect.right >= constants.SCREEN_WIDTH_MID:
            diff = self.player.rect.right - constants.SCREEN_WIDTH_MID
            self.level.shift_world(-diff)
            self.player.shift(diff)
            self.world_shift += diff
            self.player.rect.right = constants.SCREEN_WIDTH_MID

        #if self.player.rect.left <= constants.SCREEN_WIDTH_START:
        #    self.player.rect.left = constants.SCREEN_WIDTH_START
        if self.player.rect.left <= 120:
            diff = 120 - self.player.rect.left
            self.player.rect.left = 120
            self.world_shift -= diff
            self.level.shift_world(diff)

        if self.player.rect.bottom > constants.SCREEN_HEIGHT and self.player.transition_state is not constants.TRANSITION_DEATH_SEQUENCE:
            self.player.start_death_sequence()

        if self.player.state == constants.STATE_DEAD:
            self.switch = True
            self.game_info.num_lives -= 1
            if self.game_info.num_lives < 0:
                self.set_next_state(GameState.STATE_GAME_OVER)

        self.level.update(game_time)
        self.active_sprite_list.update(self.level, game_time)

    def draw(self, screen):
        self.level.draw(screen)
        self.active_sprite_list.draw(screen)
