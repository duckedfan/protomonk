__author__ = 'jkamuda'


class GameInfo():
    def __init__(self):
        self.reset()

    def reset(self):
        self.points = 0
        self.coins = 0
        self.world = 1
        self.level = 1
        self.num_lives = 3
        self.game_time = None
        self.timer = None

    def set_timer_in_seconds(self, time_in_seconds):
        self.timer = time_in_seconds * 1000

    def get_timer_in_seconds(self):
        return self.timer / 1000
