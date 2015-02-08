__author__ = 'jkamuda'

from texthelper import TextHelper
from src import utils


class DebugOverlay():
    def __init__(self, game_info, player):
        self.game_info = game_info
        self.player = player

        self.text_helper = TextHelper()

    def draw(self, screen):
        # x coordinate
        screen.blit(self.text_helper.get_text('x'), (50, 80))
        player_x = self.player.rect.x + self.player.world_shift
        x_digits = utils.get_digit_chars(player_x, 5)

        if player_x >= 10000:
            screen.blit(self.text_helper.get_text(x_digits[4]), (90, 80))
        if player_x >= 1000:
            screen.blit(self.text_helper.get_text(x_digits[3]), (110, 80))
        screen.blit(self.text_helper.get_text(x_digits[2]), (130, 80))
        screen.blit(self.text_helper.get_text(x_digits[1]), (150, 80))
        screen.blit(self.text_helper.get_text(x_digits[0]), (170, 80))

        # y coordinate
        screen.blit(self.text_helper.get_text('y'), (50, 100))
        player_y = self.player.rect.y
        y_digits = utils.get_digit_chars(player_y, 4)
        if player_y >= 1000:
            screen.blit(self.text_helper.get_text(y_digits[3]), (110, 100))
        screen.blit(self.text_helper.get_text(y_digits[2]), (130, 100))
        screen.blit(self.text_helper.get_text(y_digits[1]), (150, 100))
        screen.blit(self.text_helper.get_text(y_digits[0]), (170, 100))

