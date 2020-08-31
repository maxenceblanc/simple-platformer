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
import math
import pandas as pd

# IMPORTS DE FICHIERS
import levels.levels as levels
import config as cfg
import entities.Block



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
    

### PLAYER ACTIONS ### --------------------

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

    print(player.speed_x)



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



### CSV SAVE ### --------------------------

def save(filename, player_name, score, count, secs, chunk_times, nb_chunks):
    """ Saves the player's score in a csv.

    BUG: Fix a bug where numbers in the save file for previous runs get very long.
    #BUG: attempt_n is just calculating the amount of previous attempts, not using 
    #   the last attempt number of the player, this could make duplicates

    INPUTS:
            TODO
    """

    if len(chunk_times)>nb_chunks:
        raise Exception('Number of chunks incorrect.')
    
    # Loads the data into a DataFrame or create a new DataFrame
    try:
        data = pd.read_csv(filename+'.csv')
    except:
        data = pd.DataFrame(columns=['name',
                                     'attempt_n',
                                     'score',
                                     'count',
                                     'time'
                                     ]+['chunk_'+str(i) for i in range(1,nb_chunks+1)])

    attempt_n = data[data.name==player_name].shape[0]+1 # TODO: change to find highest attempt digit?

    # creates new entry
    new_entry = {
        'name':player_name,
        'attempt_n':attempt_n,
        'score':score,
        'count': count,
        'time': format(round(secs, 3), '.3f')
    }

    new_entry.update({'chunk_'+str(i): format(round(chunk_times[i-1], 3), '.3f') for i in range(1,len(chunk_times)+1)})
    
    if len(chunk_times) < nb_chunks:
        new_entry.update({'chunk_'+str(i): None for i in range(len(chunk_times)+1, nb_chunks+1)})

    try:
        data = data.append(new_entry, ignore_index=True)
    except:
        raise Exception('New entry format invalid.')

    data.to_csv(filename+'.csv', index=False)
