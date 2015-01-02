__author__ = 'jkamuda'

import os
import pygame
import constants
from level import Level
from player import Player
from sound import SoundManager
from game import Game

def main():

    # Center window on screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    caption = 'NES Mario'
    pygame.display.set_caption(caption)

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
    world_shift = 0

    while running:
        current_time = pygame.time.get_ticks()

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
                if key == pygame.K_DOWN:
                    player.crouch()
                if key == pygame.K_a:
                    player.transition(constants.POWER_LARGE)
                if key == pygame.K_s:
                    player.transition(constants.POWER_SMALL)
                if key == pygame.K_ESCAPE or key == pygame.K_q:
                    running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_vel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_vel > 0:
                    player.stop()
                if event.key == pygame.K_DOWN:
                    player.stop()

        if player.rect.right >= constants.SCREEN_WIDTH_MID:
            diff = player.rect.right - constants.SCREEN_WIDTH_MID
            level.shift_world(-diff)
            player.shift(diff)
            world_shift += diff
            player.rect.right = constants.SCREEN_WIDTH_MID

        #if player.rect.left <= constants.SCREEN_WIDTH_START:
        #    player.rect.left = constants.SCREEN_WIDTH_START
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            world_shift -= diff
            level.shift_world(diff)

        active_sprite_list.update(level, current_time)

        level.draw(screen)
        active_sprite_list.draw(screen)

        # debug stuff
        if constants.DEBUG:
            print '(%d, %d)' % (player.rect.x + player.world_shift, player.rect.y)

            fps = clock.get_fps()
            caption_fps = "{} - {:.2f} FPS".format(caption, fps)
            pygame.display.set_caption(caption_fps)

        # limit to 60 frames per second
        clock.tick(60)

        # update screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    #main()
    game = Game()
    game.run()