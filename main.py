__author__ = 'jkamuda'

import pygame
import constants
from level import Level
from player import Player


def main():

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("NES Mario")

    running = True
    clock = pygame.time.Clock()

    active_sprite_list = pygame.sprite.Group()
    player = Player()
    player.rect.x = 100
    player.rect.bottom = constants.GROUND_HEIGHT

    active_sprite_list.add(player)

    level = Level(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.x_vel < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.x_vel > 0:
                    player.stop()

        active_sprite_list.update()
        level.update()

        level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.draw.rect(screen, constants.BLACK, (0, constants.GROUND_HEIGHT, 2000, 60))

        # limit to 60 frames per second
        clock.tick(60)

        # update screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()