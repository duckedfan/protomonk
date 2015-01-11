__author__ = 'jkamuda'

from src.game_state import GameState
from src.texthelper import TextHelper
from src.spritesheet import SpriteSheet
import src.constants as c
from src import coordinates as coords


class LoadScreen(GameState):
    def __init__(self, game_info):
        GameState.__init__(self, GameState.STATE_LOAD, GameState.STATE_GAME)

        self.game_info = game_info
        self.text_helper = TextHelper()

        self.load_screen_time = 0
        # Mario frame
        sprite_sheet = SpriteSheet("data\characters.gif")
        self.mario_frame = sprite_sheet.get_image(coords.MARIO_SMALL_STANDING_RIGHT, c.IMG_MULTIPLIER)

    def update(self, game_time):
        if (game_time - self.load_screen_time) > 2000:
            self.switch = True

    def draw(self, screen):
        screen.fill(c.BLACK)

        screen.blit(self.text_helper.get_text('w'), (280, 200))
        screen.blit(self.text_helper.get_text('o'), (300, 200))
        screen.blit(self.text_helper.get_text('r'), (320, 200))
        screen.blit(self.text_helper.get_text('l'), (340, 200))
        screen.blit(self.text_helper.get_text('d'), (360, 200))

        screen.blit(self.text_helper.get_text(str(self.game_info.world)), (420, 200))
        screen.blit(self.text_helper.get_text('-'), (440, 205))
        screen.blit(self.text_helper.get_text(str(self.game_info.level)), (460, 200))

        screen.blit(self.text_helper.get_text('+'), (390, 270))

        screen.blit(self.mario_frame, (320, 250))
        screen.blit(self.text_helper.get_text(str(self.game_info.num_lives)), (430, 265))
