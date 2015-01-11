__author__ = 'jkamuda'

import pygame

from src import coordinates as coords, constants
from src.spritesheet import SpriteSheet
from texthelper import TextHelper
from game_state import GameState


class Menu(GameState):
    PLAYER_1_SELECTED_RECT = (250, 348)
    PLAYER_2_SELECTED_RECT = (250, 389)

    def __init__(self):
        GameState.__init__(self, GameState.STATE_MENU, GameState.STATE_LOAD)

        self.player_num = 1
        self.background = None
        self.title = None
        self.title_rect = None

        self.init_background()
        self.text_helper = TextHelper()

        item_objects_ss = SpriteSheet("data/item_objects.png")
        self.selector_frame = item_objects_ss.get_image(coords.TITLE_SELECTOR, constants.IMG_MULTIPLIER)

    def init_background(self):
        # Background
        background_ss = SpriteSheet("data/levels/level_1.png")
        self.background = background_ss.get_image(coords.LEVEL_1, constants.IMG_MULTIPLIER, constants.WHITE)

        # Title image
        title_screen_ss = SpriteSheet("data/title_screen.png")
        self.title = title_screen_ss.get_image(coords.MAIN_TITLE, constants.IMG_MULTIPLIER, constants.WHITE)

        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = constants.SCREEN_WIDTH_MID
        self.title_rect.centery = 200

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_UP:
                    self.player_num = 1
                if key == pygame.K_DOWN:
                    self.player_num = 2
                if key == pygame.K_RETURN:
                    self.switch = True

    def draw(self, screen):
        screen.fill(constants.WHITE)
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, self.title_rect)

        # 1 Player Game
        screen.blit(self.text_helper.get_text('1'), (300, 350))

        screen.blit(self.text_helper.get_text('p'), (340, 350))
        screen.blit(self.text_helper.get_text('l'), (360, 350))
        screen.blit(self.text_helper.get_text('a'), (380, 350))
        screen.blit(self.text_helper.get_text('y'), (400, 350))
        screen.blit(self.text_helper.get_text('e'), (420, 350))
        screen.blit(self.text_helper.get_text('r'), (440, 350))

        screen.blit(self.text_helper.get_text('g'), (480, 350))
        screen.blit(self.text_helper.get_text('a'), (500, 350))
        screen.blit(self.text_helper.get_text('m'), (520, 350))
        screen.blit(self.text_helper.get_text('e'), (540, 350))

        # 2 Player Game
        screen.blit(self.text_helper.get_text('2'), (300, 390))

        screen.blit(self.text_helper.get_text('p'), (340, 390))
        screen.blit(self.text_helper.get_text('l'), (360, 390))
        screen.blit(self.text_helper.get_text('a'), (380, 390))
        screen.blit(self.text_helper.get_text('y'), (400, 390))
        screen.blit(self.text_helper.get_text('e'), (420, 390))
        screen.blit(self.text_helper.get_text('r'), (440, 390))

        screen.blit(self.text_helper.get_text('g'), (480, 390))
        screen.blit(self.text_helper.get_text('a'), (500, 390))
        screen.blit(self.text_helper.get_text('m'), (520, 390))
        screen.blit(self.text_helper.get_text('e'), (540, 390))

        # Selector
        if self.player_num == 1:
            screen.blit(self.selector_frame, self.PLAYER_1_SELECTED_RECT)
        else:
            screen.blit(self.selector_frame, self.PLAYER_2_SELECTED_RECT)

