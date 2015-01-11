__author__ = 'jkamuda'


class GameState():

    STATE_MENU = 'menu'
    STATE_LOAD = 'load'
    STATE_GAME = 'game'
    STATE_GAME_OVER = 'gameover'

    def __init__(self, state, next_state):
        self.current = state
        self.next = next_state
        self.switch = False

    def set_next_state(self, next_state):
        self.next = next_state

    def switch_state(self):
        return self.switch

    def process_events(self, events):
        pass

    def update(self, game_time):
        pass

    def draw(self, screen):
        pass


