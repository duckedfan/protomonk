__author__ = 'jkamuda'


class GameInfo():
    points = 0
    coins = 0
    world = 0
    level = 0
    num_lives = 0
    game_time = None
    timer = None

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
