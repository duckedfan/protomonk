__author__ = 'jkamuda'

from src.game_state import GameState
from src.texthelper import TextHelper
from src import constants as c


class GameOverScreen(GameState):
    def __init__(self, game_info, sound_manager):
        GameState.__init__(self, GameState.STATE_GAME_OVER, GameState.STATE_MENU)

        self.game_info = game_info
        self.sound_manager = sound_manager

        self.load_screen_time = -1

        self.sound_manager.play_music(c.MUSIC_GAME_OVER)

        self.text_helper = TextHelper()

    def update(self, game_time):
        if (game_time - self.load_screen_time) > 5000:
            self.switch = True

    def draw(self, screen):
        screen.fill(c.BLACK)

        screen.blit(self.text_helper.get_text('g'), (280, 200))
        screen.blit(self.text_helper.get_text('a'), (300, 200))
        screen.blit(self.text_helper.get_text('m'), (320, 200))
        screen.blit(self.text_helper.get_text('e'), (340, 200))

        screen.blit(self.text_helper.get_text('o'), (380, 200))
        screen.blit(self.text_helper.get_text('v'), (400, 200))
        screen.blit(self.text_helper.get_text('e'), (420, 200))
        screen.blit(self.text_helper.get_text('r'), (440, 200))
