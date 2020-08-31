#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 11/2019
########################

# IMPORTS
import pygame
import random as rd
from pygame.locals import *

# CUSTOM IMPORTS
import levels.levels as levels
import game_config as cfg
import entities.Block

import recording_system


""" TO DO LIST
"""


""" PROBLEMS
PB :
Ans :
"""

""" NOTES

coordinates:
0 - - - - -> (x)
|
|
|
v (y)
"""

####################################################
###################| CLASSES |######################
####################################################


####################################################
##################| FONCTIONS |#####################
####################################################
    

### LEVEL GENERATION ### ----------------------

def loadChunk(block_list, chunk, x_start) :
    """ Loads the chunk from the start coordinate.

    INPUTS: 
            list of the blocks from the level
            the chunk to be loaded, [str, ..]
            the start coordinate

    VARIABLES: 
                x = x coordinate of the next block to be created
                y = y coordinate of the next block to be created
    """

    # Sets the star of the player for the generation.
    x, y = x_start, (cfg.VISIBILITY_Y-1) * levels.CHUNK_HEIGHT * cfg.BLOCK_HEIGHT


    # Generation
    for column in range(len(chunk[0])):

        for row in range(len(chunk)):

            if chunk[row][column] == "W":
                block_list.append(entities.Block.Block(x,y))
            elif chunk[row][column] == "E":
                block_list.append(entities.Block.Block(x,y, type="end"))

            y += cfg.BLOCK_HEIGHT # Goes downwards of one block

        x += cfg.BLOCK_WIDTH # Goes right of block
        y = (cfg.VISIBILITY_Y-1) * levels.CHUNK_HEIGHT * cfg.BLOCK_HEIGHT # Get back up

def endOfChunk(blocks):
    """ Detects if the last block of the last chunk is on screen.

    INPUTS:
            list of the blocks from the level
    OUTPUT: 
            True if last block is on screen, False otherwise
    """

    return blocks[-1].rect.x < cfg.SIZE_X

def levelGeneration(isRandom, blocks, level, chunk_num=None):
    """ Handles the level generation, loads a chunk if needed.

    INPUTS: 
            True if the generation must choose next chunk randomly
            the list of all the blocks
            the chunk list
            amount of chunks already loaded
    OUTPUT: 
            True if a chunk has been loaded, False otherwise
    """

    # Loads the next chunk if needed
    if endOfChunk(blocks):

        # Getting the coordinate x from where to start the generation
        start_x = blocks[-1].rect.x + cfg.BLOCK_WIDTH

        # Random generation
        if isRandom: 

            # Next chunk is chosen at random
            next_chunk = level[rd.randint(0, len(level)-1)]

            loadChunk(blocks, next_chunk, start_x)
            return True

        # Sequential generation
        elif chunk_num < len(level): 

            # Selects the next chunk to be loaded in the chunk list
            next_chunk = level[chunk_num]

            loadChunk(blocks, next_chunk, start_x)
            return True
        
            
    return False
    

### ACTIONS ### --------------------

def move(player, blocks):
    """ Detects pressed keys and changes speeds accordingly. 
    Then applies slowdowns.

    INPUTS:
            Player object
            list of the blocks from the level
    """

    key = pygame.key.get_pressed()

    # Horizontal movements #

    # Left
    if key[cfg.KEY_LEFT]:
        if player.speed_x > 0:
            player.slowdown()
        else:
            player.speed_x -= cfg.ACCELERATION_X
    # Right
    elif key[cfg.KEY_RIGHT]:
        if player.speed_x < 0:
            player.slowdown()
        else:
            player.speed_x += cfg.ACCELERATION_X

    # Gentle slowdowns if L/R keys aren't in use
    else:
        if player.speed_x > 0:
            player.speed_x -= 1
        elif player.speed_x < 0:
            player.speed_x += 1

    # Vertical movements #

    # Gravity
    if not ground(player, blocks):
        player.speed_y += cfg.ACCELERATION_Y

    if key[cfg.KEY_UP] and ground(player, blocks): # Up
        player.speed_y = -cfg.SPEED_Y # - to go upwards

    # x speed limit
    if player.speed_x < -cfg.SPEED_X:
        player.speed_x = -cfg.SPEED_X
    elif player.speed_x > cfg.SPEED_X:
        player.speed_x = cfg.SPEED_X

    # Applies speeds to the Player
    player.move(blocks)

def ground(player, blocks):
    """ Detects if a block is under the Player.

    INPUTS:
            player object
            list of blocks from the level
    """
    
    for block in blocks:
        for pixel in range(-(cfg.BLOCK_WIDTH-1),cfg.BLOCK_WIDTH):
            if player.rect.bottom == block.rect.top and player.rect.left == block.rect.left + pixel:
                return True
    return False

def record(game):
    """
    """

    state = recording_system.serializeState(game)
    recording_system.saveDemo(state, game.player_name, cfg.MAP_NAME)

### WINDOW DISPLAY ### --------------------------

def camera(player, blocks):
    """ Moves the camera.

    INPUTS:
            the player object
            the list of blocks from the level
    """

    key = pygame.key.get_pressed()

    if key[cfg.CAMERA_RIGHT]:
        for block in blocks:
            block.move(-cfg.SPEED_CAMERA_X, 0)

        player.rect.x -= cfg.SPEED_CAMERA_X

    elif key[cfg.CAMERA_LEFT]:
        for block in blocks:
            block.move(cfg.SPEED_CAMERA_X, 0)

        player.rect.x += cfg.SPEED_CAMERA_X

def mouse(player):
    """ Uses mouse position to set the player's position

    INPUTS: 
            player object
    """
    
    player.rect.x, player.rect.y = pygame.mouse.get_pos()
    player.speed_x, player.speed_y = 0, 0
    
def display(window, blocks, player):
    """ Updates the display.

    INPUTS:
            the window object
            the list of blocks from the level
            the player object
    """

    # Draws the background
    window.fill(cfg.GREY) 

    # Draws each block
    for block in blocks:
        pygame.draw.rect(window, cfg.WHITE, block.rect)

    # Draws the player
    pygame.draw.rect(window, cfg.ORANGE, player.rect) 

    # Refreshes the window
    pygame.display.update()


### SCORE CALCULATIONS ### --------------------------

def score_func(time, player, blocks):
    """ Score according to speed (block/sec) and distance traveled.

    INPUTS:
            the time in seconds spent in the run
            the player object
            the list of blocks from the level
    """

    # Count the amount of chunks passed
    chunks_passed = 0
    for block in blocks:
        if block.type == "end" and block.rect.x < player.rect.x:
            chunks_passed += 1

    # Score formula
    pos_weight   = 2.5
    speed_weight = 1
    score = chunks_passed*pos_weight + ((chunks_passed*20)/time**1.5)*speed_weight

    return(round(score,1), chunks_passed, time)




