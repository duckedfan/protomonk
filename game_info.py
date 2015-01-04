__author__ = 'jkamuda'


class GameInfo():

    points = 0
    coins = 0
    world = 1
    level = 1
    num_lives = 3
    game_time = None
    timer = None

    def __init__(self):
        pass

    def set_timer_in_seconds(self, time_in_seconds):
        self.timer = time_in_seconds * 1000

    def get_timer_in_seconds(self):
        return self.timer / 1000
