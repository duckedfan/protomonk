__author__ = 'jkamuda'

import os
import pygame
import constants
from level import Level
from player import Player
from sound import SoundManager


def main():

    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("NES Mario")

    sound_manager = SoundManager()

    running = True
    clock = pygame.time.Clock()

    active_sprite_list = pygame.sprite.Group()
    player = Player(sound_manager)
    player.rect.x = 100
    player.rect.bottom = constants.GROUND_HEIGHT

    active_sprite_list.add(player)

    level = Level(player)

    sound_manager.play_music(constants.MUSIC_MAIN_THEME)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_LEFT:
                    player.go_left()
                if key == pygame.K_RIGHT:
                    player.go_right()
                if key == pygame.K_UP:
                    player.jump()
                if key == pygame.K_ESCAPE or key == pygame.K_q:
                    running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_vel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_vel > 0:
                    player.stop()

        if player.rect.right >= constants.SCREEN_WIDTH_MID:
            diff = player.rect.right - constants.SCREEN_WIDTH_MID
            level.shift_world(-diff)
            player.rect.right = constants.SCREEN_WIDTH_MID

        if player.rect.left <= constants.SCREEN_WIDTH_START:
            player.rect.left = constants.SCREEN_WIDTH_START

        active_sprite_list.update()
        level.update()

        level.draw(screen)
        active_sprite_list.draw(screen)

        # limit to 60 frames per second
        clock.tick(60)

        # update screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()