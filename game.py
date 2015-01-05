__author__ = 'jkamuda'

import os
import pygame
import constants
from player import Player
from sound import SoundManager
from menu import Menu
from overhead import Overhead
from game_state import GameState
from load_screen import LoadScreen
from game_info import GameInfo
from mario_game import MarioGame
from game_over_screen import GameOverScreen


class Game():
    screen = None
    caption = 'NES Mario'
    sound_manager = None
    game_info = None

    def __init__(self):
        # Center window on screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        self.game_info = GameInfo()
        self.sound_manager = SoundManager()

    def get_game_state(self, game_state):
        if game_state == GameState.STATE_MENU:
            # TODO kind of an ugly place to put this reset...
            self.game_info.reset()
            return Menu()
        elif game_state == GameState.STATE_LOAD:
            return LoadScreen(self.game_info)
        elif game_state == GameState.STATE_GAME:
            return MarioGame(self.game_info, self.sound_manager)
        elif game_state == GameState.STATE_GAME_OVER:
            return GameOverScreen(self.game_info, self.sound_manager)

    def run(self):
        pygame.display.set_caption(self.caption)

        running = True
        clock = pygame.time.Clock()

        active_sprite_list = pygame.sprite.Group()
        player = Player(self.sound_manager)
        player.rect.x = 100
        player.rect.bottom = constants.GROUND_HEIGHT

        active_sprite_list.add(player)

        overhead_info = Overhead(self.game_info)
        game_state = self.get_game_state(GameState.STATE_MENU)

        while running:
            game_time = pygame.time.get_ticks()

            if game_state.switch_state():
                game_state = self.get_game_state(game_state.next)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_ESCAPE or key == pygame.K_q:
                        running = False

            game_state.process_events(events)

            overhead_info.update(game_time)
            game_state.update(game_time)

            game_state.draw(self.screen)
            overhead_info.draw(self.screen)

            # Limit to 60 frames per second
            clock.tick(60)

            # Update screen
            pygame.display.flip()

        pygame.quit()
