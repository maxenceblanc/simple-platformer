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
TAS system (log + custom start)
Replay system
Code cleaning (english to french)
Time stamp system cleaning (start on key press) 
Score refactoring
Scoreboard system (best time, bt per chunck)
"""



# Initializes pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # sets the window's title




def main(random_gen, player_name):
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
    chunk_num = 1
    prev_count = 0

    chunk_times = []
    last_time = 0

    # Loads the first chunk of the map
    levelGeneration(blocks, level[0], 0)

    over = False
    while not over:

        CLOCK.tick(20) # 20 FPS

        for e in pygame.event.get():
            pygame.event.set_allowed(None)
            pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
            pygame.event.pump()

            if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_RETURN): # quit condition
                over = True

        if player.rect.y + PLAYER_HEIGHT > SIZE_Y:
            over = True

        # Moves the camera if needed
        camera(player, blocks)

        # Moves the player when m1 is on click
        if pygame.mouse.get_pressed()[0]:
            mouse(player)

        # Moves the player
        move(player, blocks)

        # Not very viable but works for that list length
        count = 0
        for block in blocks:
            if block.type == "end" and block.rect.x < player.rect.x:
                count+=1
        
        if count == prev_count + 1:
            current_time = pygame.time.get_ticks() / 1000
            print("chunk n°", count, ": ", current_time)

            chunk_times.append(round(current_time-last_time, 3))
            last_time = current_time
            prev_count+=1


        # Loads the next chunk if needed
        if endOfChunk(blocks):

            if random_gen:
                # Next chunk is chosen at random
                next_chunk = level[rd.randint(0, len(level)-1)]
                chunk_num += 1

                # Getting the coordinate x from where to start the generation
                start_x = blocks[-1].rect.x + BLOCK_WIDTH

                levelGeneration(blocks, next_chunk, start_x)

            else:
                # Selects the next chunk to be loaded in the chunk list
                if chunk_num < len(level):
                    next_chunk = level[chunk_num]
                    chunk_num += 1

                    # Getting the coordinate x from where to start the generation
                    start_x = blocks[-1].rect.x + BLOCK_WIDTH

                    levelGeneration(blocks, next_chunk, start_x)

        display(WINDOW, blocks, player) # Window dispay


    # Displays the score in console
    score, count, secs = score_func(current_time, player, blocks)
    print('Score:', score)
    filename = "data"
    save(filename, player_name, score, count, secs, chunk_times, NB_CHUNK)
    



if __name__ == "__main__":

    arguments = sys.argv
    player_name = ""

    if len(arguments) != 2:
        print("ERROR: Wrong args. Should be like : \n\npython3 main.py name_of_player")
        exit()

    else:
        player_name = arguments[1]

    random_gen = False  # Toggles random generation


    main(random_gen, player_name)

    pygame.quit()
    quit()
