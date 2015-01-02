__author__ = 'jkamuda'

import os
import pygame
import constants
from player import Player
from sound import SoundManager
from menu import Menu
from overhead import Overhead


class Game():

    screen = None
    caption = 'NES Mario'
    sound_manager = None

    def __init__(self):
        # Center window on screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        self.sound_manager = SoundManager()

    def run(self):
        pygame.display.set_caption(self.caption)

        running = True
        clock = pygame.time.Clock()

        active_sprite_list = pygame.sprite.Group()
        player = Player(self.sound_manager)
        player.rect.x = 100
        player.rect.bottom = constants.GROUND_HEIGHT

        active_sprite_list.add(player)

        self.sound_manager.play_music(constants.MUSIC_MAIN_THEME)

        overhead_info = Overhead()
        menu = Menu()

        while running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_ESCAPE or key == pygame.K_q:
                        running = False

            menu.draw(self.screen)
            overhead_info.draw(self.screen, current_time)

            # limit to 60 frames per second
            clock.tick(60)

            # update screen
            pygame.display.flip()

        pygame.quit()


