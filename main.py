#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 11/2019
########################

# IMPORTS
import sys
import pygame
from pygame.locals import *

# EXTRA FILES
from functions import *
from configs import *

""" TODO
Code cleaning (french to english)
Score refactoring
TAS system (log + custom start)
Replay system
Scoreboard system (best time, bt per chunck)
training mode with options (like no death, mouse etc.)
"""



# Initializes pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # sets the window's title


### SETUP ### ---------------------- 

def idleLoop(random_gen, blocks, chunk_num, WINDOW, player):
    """ Used this to wait for the user input to start time but still picture the level.
    That allows for time to start when the user presses a key rather than when 
    program starts.

    INPUTS: 
            if True, toggles random generation (bool)
            the list of all the blocks
            amount of chunks already loaded
            Window object
            player object

    OUTPUT:
            amount of chunks already loaded
    """
    ready = False # True when all chunks that should be visible are loaded
    start = False
    while not start:

        for e in pygame.event.get():
            pygame.event.set_allowed(None)
            pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
            pygame.event.pump()

        key = pygame.key.get_pressed()

        if key[KEY_LEFT] or key[KEY_RIGHT] or key[KEY_UP]:
            if pygame.time.get_ticks() / 1000 > 0.5: # Arbitrary, used to wait for the game to be fully loaded
                start = True

        # Loads the next chunk if needed
        chunkWasLoaded = levelGeneration(random_gen, blocks, level, chunk_num)

        if chunkWasLoaded:
            chunk_num += 1
        elif not ready:
            print("ready")
            ready = True

        display(WINDOW, blocks, player) # Window dispay

    return chunk_num


### MAIN ----------------------

def main(random_gen, canLose, player_name):
    """ Main function. Contains the main loop of the game.

    INPUTS: 
            if True, toggles random generation (bool)
            name of the player (str)
    """

    # List of all the Blocks
    blocks = []

    # Init the player
    player = Player()

    # Display Setup
    WINDOW = pygame.display.set_mode((SIZE_X, # Dimensions of WINDOW
                                      SIZE_Y))

    # Time
    CLOCK = pygame.time.Clock()

    # Inits TODO: explain variables
    chunk_num = 1 # 1 because of the init chunk
    prev_chunks_passed = 0

    chunk_times = []
    last_time = 0

    # Loads the first chunk of the map
    loadChunk(blocks, level[0], 0)

    # Idle screen
    # Using this to wait for the user input to start time but still picture the level
    chunk_num = idleLoop(random_gen, blocks, chunk_num, WINDOW, player)

    start_time = pygame.time.get_ticks() / 1000


    # Main loop
    over = False
    while not over:

        CLOCK.tick(20) # 20 FPS

        for e in pygame.event.get():
            pygame.event.set_allowed(None)
            pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
            pygame.event.pump()

            if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_RETURN): # quit condition
                over = True

        if player.rect.y + PLAYER_HEIGHT > SIZE_Y and canLose:
            over = True

        # Moves the camera if needed
        camera(player, blocks)

        # Moves the player when m1 is on click
        if pygame.mouse.get_pressed()[0]:
            mouse(player)

        # Moves the player
        move(player, blocks)

        # Not very viable but works for that list length
        chunks_passed = 0
        for block in blocks:
            if block.type == "end" and block.rect.x < player.rect.x:
                chunks_passed+=1
        
        if chunks_passed == prev_chunks_passed + 1:
            current_time = pygame.time.get_ticks() / 1000 - start_time
            print("chunk n°", chunks_passed, ": ", current_time)

            chunk_times.append(round(current_time-last_time, 3))
            last_time = current_time
            prev_chunks_passed+=1


        # Loads the next chunk if needed
        chunkWasLoaded = levelGeneration(random_gen, blocks, level, chunk_num)

        if chunkWasLoaded:
            chunk_num += 1

        display(WINDOW, blocks, player) # Window dispay


    # Displays the score in console
    score, chunks_passed, end_time = score_func(current_time, player, blocks)
    print('Chunk nb:', chunks_passed, 'Time:', end_time)
    print('Score:', score)

    # Saving
    filename = "data"
    save(filename, player_name, score, chunks_passed, end_time, chunk_times, NB_CHUNK)
    



if __name__ == "__main__":

    arguments = sys.argv
    player_name = ""

    if len(arguments) != 2:
        print("ERROR: Wrong args. Should be like : \n\npython3 main.py name_of_player")
        exit()

    else:
        player_name = arguments[1]

    random_gen = False  # Toggles random generation
    canLose = True


    main(random_gen, canLose, player_name)

    pygame.quit()
    quit()
