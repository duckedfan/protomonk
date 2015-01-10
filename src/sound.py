__author__ = 'jkamuda'

import pygame

from src import constants, utils


class SoundManager():

    def __init__(self):
        self.sounds = utils.load_music_resources(constants.SOUND_DIR, constants.SOUND_EXTENSIONS)
        self.music = utils.load_music_resources(constants.MUSIC_DIR, constants.SOUND_EXTENSIONS)

    def play_sound(self, sound_name):
        if sound_name not in self.sounds:
            raise Exception("Sound name not found")

        pygame.mixer.Sound(self.sounds[sound_name]).play()

    def play_music(self, music_name):
        if music_name not in self.music:
            raise Exception("Music name not found")

        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.music[music_name])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()