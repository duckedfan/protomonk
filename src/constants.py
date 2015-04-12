__author__ = 'jkamuda'

"""
Global constants
"""

DEBUG = False

# Colors
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_WIDTH_START = 0
SCREEN_WIDTH_MID = SCREEN_WIDTH / 2
SCREEN_HEIGHT = 560
GROUND_HEIGHT = SCREEN_HEIGHT - 62

# Image multipliers
IMG_MULTIPLIER = 2.5

# Sound
SOUND_EXTENSIONS = ('.wav', '.ogg', '.mp3')
SOUND_DIR = 'data/sound'
MUSIC_DIR = 'data/music'

# Sound options
SOUND_BIG_JUMP = 'big_jump'
SOUND_BRICK_SMASH = 'brick_smash'
SOUND_BUMP = 'bump'
SOUND_COIN = 'coin'
SOUND_COUNT_DOWN = 'count_down'
SOUND_FIREBALL = 'fireball'
SOUND_KICK = 'kick'
SOUND_ONE_UP = 'one_up'
SOUND_PIPE = 'pipe'
SOUND_POWERUP = 'powerup'
SOUND_POWERUP_APPEARS = 'powerup_appears'
SOUND_SMALL_JUMP = 'small_jump'
SOUND_STOMP = 'stomp'

# Music options
MUSIC_DEATH = 'death'
MUSIC_FLAGPOLE = 'flagpole'
MUSIC_GAME_OVER = 'game_over'
MUSIC_INVINCIBLE = 'invincible'
MUSIC_MAIN_THEME = 'main_theme'
MUSIC_MAIN_THEME_SPED_UP = 'main_theme_sped_up'
MUSIC_OUT_OF_TIME = 'out_of_time'
MUSIC_STAGE_CLEAR = 'stage_clear'
MUSIC_WORLD_CLEAR = 'world_clear'

# Player states
STATE_STANDING = 'standing'
STATE_WALKING = 'walking'
STATE_JUMPING = 'jumping'
STATE_FALLING = 'falling'
STATE_CROUCHING = 'crouching'
STATE_TRANSITION = 'transition'
STATE_DEAD = 'mario_dead_sad_face'

POWER_SMALL = 'small'
POWER_LARGE = 'large'
POWER_FIREBALL = 'fireball'
POWER_INVINCIBLE = 'invincible'

TRANSITION_SMALL_TO_BIG = 'small_to_big'
TRANSITION_BIG_TO_SMALL = 'big_to_small'
TRANSITION_DEATH_SEQUENCE = 'death_sequence'

# Enemy states
ENEMY_STATE_ALIVE = "alive"
ENEMY_STATE_DEAD = "dead"

DIR_LEFT = "left"
DIR_RIGHT = "right"

# Object dimensions
PIPE_W = 80
PIPE_SMALL_H = 80
PIPE_MED_H = 120
PIPE_LARGE_H = 160

BRICK_W = 40
BRICK_H = 40

PLAYER_MID_W = 16
PLAYER_MID_H = 24
PLAYER_ADULT_W = 18
PLAYER_SMALL_W = 14
PLAYER_SMALL_JUMP_W = 16
PLAYER_ADULT_H = 32
PLAYER_SMALL_H = 17

# Scoring
SCORE_COIN = 200
SCORE_GOOMBA = 100
SCORE_KOOPA = 100
SCORE_POWERUP = 1000

# Powerups
POWERUP_MUSHROOM = 'powerup_mushroom'
POWERUP_FLOWER = 'powerup_flower'
POWERUP_STAR = 'powerup_star'