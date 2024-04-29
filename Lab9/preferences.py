"""
Author: Prof. Alyssa
Stores values for constant variables.
This is good practice to avoid "magic numbers"

Assignment adapted from HMC CS60

TODO Update this program header
"""

import pygame

class Preferences:
    pygame.init()

    ##########
    # Timing #
    ##########

    # How frequently to move the snake
    REFRESH_RATE = 1
    # How frequently to add food to the board
    FOOD_ADD_RATE = 30
    # How long to sleep between updates
    SLEEP_TIME = 30

    ##########
    # Sizing #
    ##########

    # Dimensions of the board
    NUM_CELLS_WIDE = 50
    NUM_CELLS_TALL = 30 

    # Size of each cell in pixels
    CELL_SIZE = 15

    # Dimensions of the board in pixels
    GAME_BOARD_WIDTH = NUM_CELLS_WIDE * CELL_SIZE
    GAME_BOARD_HEIGHT = NUM_CELLS_TALL * CELL_SIZE

    ##########
    # Colors #
    ##########

    COLOR_BACKGROUND = pygame.Color('lavender')
    COLOR_WALL = pygame.Color('gray40')
    COLOR_FOOD = pygame.Color('firebrick')
    COLOR_EMPTY = pygame.Color('lavender')
    COLOR_HEAD = pygame.Color('darkorchid4')
    COLOR_BODY = pygame.Color('darkgreen')

    ##########################
    # Game over text display #
    ##########################
    
    GAME_OVER_X = GAME_BOARD_HEIGHT / 2
    GAME_OVER_Y = GAME_BOARD_WIDTH / 2
    GAME_OVER_COLOR = pygame.Color('navy')
    GAME_OVER_FONT = pygame.font.SysFont("arial", 80)
    GAME_OVER_TEXT = "Game Over"

    ##########################
    # Live score text display #
    ##########################

    LIVE_SCORE_X = GAME_BOARD_HEIGHT / 2 + 400
    LIVE_SCORE_Y = GAME_BOARD_WIDTH / 2 + 50
    LIVE_SCORE_COLOR = pygame.Color('black')
    LIVE_SCORE_FONT = pygame.font.SysFont("arial", 25)

    ######################
    # Graphics and Audio #
    ######################

    # Image to display as the head
    HEAD_IMAGE = "trainer.png"
    # Sound to play when eating
    EAT_SOUND = "meow.wav"