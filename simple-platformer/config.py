#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 03/2020
########################

from pygame.locals import *

import levels.levels as levels

###############################
###### APP CONFIGURATION ######
###############################

# Folder for run's data files
DATA_FOLDER = "data"
DATA_FILE = "data"

RANDOM_GEN = False  # Toggles random generation
CAN_LOSE = True # Disables losing, for dev/testing purposes



################################
###### GAME CONFIGURATION ######
################################

# Coefficient of Proportions (to increase physics proportionally)
PROPORTION = 1

# Size of blocks
BLOCK_WIDTH  = 16 * PROPORTION
BLOCK_HEIGHT = 16 * PROPORTION

# For the display
VISIBILITY_X = 45 # Width of WINDOW in amount of blocks.
VISIBILITY_Y = 2 # Height of WINDOW in amount of chunk height.
SIZE_X = BLOCK_WIDTH * VISIBILITY_X # Width of WINDOW in pixels.
SIZE_Y = levels.CHUNK_HEIGHT * BLOCK_HEIGHT * VISIBILITY_Y # Height of WINDOW in pixels.

# Player size
PLAYER_WIDTH  = 1 * BLOCK_WIDTH
PLAYER_HEIGHT = 2 * BLOCK_HEIGHT

# Start
START_X = 0
START_Y = SIZE_Y - BLOCK_HEIGHT - PLAYER_HEIGHT

# Colours
WHITE   = (255, 255, 255)
GREY    = (30,30,30)
ORANGE  = (255, 125, 0)
RED     = (255, 0, 0)

# Acceleration
ACCELERATION_X = 1 * PROPORTION
ACCELERATION_Y = 1.67 * PROPORTION #1.67
COEFF_ACCELERATION_X = 1.3
SLOWDOWN__X    = COEFF_ACCELERATION_X * ACCELERATION_X
# Speed
SPEED_X = 16 * PROPORTION # speed_x max
SPEED_Y = BLOCK_HEIGHT * (14/16) # speed_y max
# Camera speed
SPEED_CAMERA_X = 80 * PROPORTION
# SPEED_CAMERA_Y = 5 * PROPORTION


# Keys
KEY_RIGHT = K_d
KEY_LEFT  = K_q
KEY_UP    = K_z

# Camera keys
CAMERA_RIGHT   = K_RIGHT
CAMERA_LEFT    = K_LEFT
