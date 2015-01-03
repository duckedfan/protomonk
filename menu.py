__author__ = 'jkamuda'

from spritesheet import SpriteSheet
import constants
from texthelper import TextHelper
import coordinates as coords
import pygame

class Menu():

    player_num = 1

    PLAYER_1_SELECTED_RECT = (250, 348)
    PLAYER_2_SELECTED_RECT = (250, 390)

    selector_frame = None

    background = None
    title = None
    title_rect = None
    text_helper = None

    def __init__(self):
        self.init_background()
        self.text_helper = TextHelper()

        item_objects_ss = SpriteSheet("data/item_objects.png")
        self.selector_frame = item_objects_ss.get_image_v2(coords.TITLE_SELECTOR, constants.IMG_MULTIPLIER)

    def init_background(self):
        # Background
        background_ss = SpriteSheet("data/levels/level_1.png")
        self.background = background_ss.get_image_v2((0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), constants.IMG_MULTIPLIER)
        self.background.set_colorkey(constants.WHITE)

        # Title image
        title_screen_ss = SpriteSheet("data/title_screen.png")
        self.title = title_screen_ss.get_image_v2((1, 60, 176, 88), constants.IMG_MULTIPLIER)
        self.title.set_colorkey(constants.WHITE)

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

