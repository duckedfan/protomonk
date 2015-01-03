__author__ = 'jkamuda'

from game_state import GameState
from texthelper import TextHelper
import constants as c


class LoadScreen(GameState):

    background = None
    load_screen_time = -1
    text_helper = None

    def __init__(self, ):
        GameState.__init__(self, GameState.STATE_LOAD, GameState.STATE_MENU)

        self.text_helper = TextHelper()

    def update(self, game_time):
        if self.load_screen_time == -1:
            self.load_screen_time = game_time
        elif (game_time - self.load_screen_time) > 2000:
            self.switch = True

    def draw(self, screen):
        screen.fill(c.BLACK)

        screen.blit(self.text_helper.get_text('p'), (340, 350))
        screen.blit(self.text_helper.get_text('l'), (360, 350))
        screen.blit(self.text_helper.get_text('a'), (380, 350))
        screen.blit(self.text_helper.get_text('y'), (400, 350))
        screen.blit(self.text_helper.get_text('e'), (420, 350))
        screen.blit(self.text_helper.get_text('r'), (440, 350))