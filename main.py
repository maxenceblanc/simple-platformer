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

arguments = sys.argv
player_name = ""

if len(arguments) != 3:
    print("ERROR: Wrong args. Should be like : \n\npython3 main.py name_of_player normal\n\nor\n\npython3 main.py name_of_player reverse\n\n")
    exit()

else:
    player_name = arguments[1]
    if arguments[2]=='normal':
        reversed_screen = False
    elif arguments[2]=='reverse':
        reversed_screen = True
    else:
        raise Exception('Invalid second argument. Should be: \n\nnormal or reverse\n\n')


# EXTRA FILES
from fonctions import *

# Initializes pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # sets the window's title

# Variables
chunk_num = 1
prev_count = 0

chunk_times = []
last_time = 0

# Loads the first chunk
levelGeneration(level[0], 0)

over = False
while not over:

    CLOCK.tick(20) # 20 FPS

    for e in pygame.event.get():
        pygame.event.set_allowed(None)
        pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
        pygame.event.pump()

        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_RETURN): # quit condition
            over = True

    if Perso.rect.y + Perso_HEIGHT > TAILLE_Y:
        over = True

    # Moves the camera if needed
    camera()

    # Moves the Player
    bouge()

    # Not very viable but works for that list length
    count = 0
    for block in blocks:
        if block.type == "end" and block.rect.x < Perso.rect.x:
            count+=1
    
    if count == prev_count + 1:
        current_time = pygame.time.get_ticks() / 1000
        print("chunck n°", count, ": ", current_time)

        chunk_times.append(round(current_time-last_time, 3))
        last_time = current_time
        prev_count+=1


    # Loads the next chunk if needed
    if endOfChunk():

        # Selects the next chunk to be loaded in the chunk list
        if chunk_num < len(level):
            next_chunk = level[chunk_num]
            chunk_num += 1

            # Getting the coordinate x from where to start the generation
            start_x = blocks[-1].rect.x + BLOCK_WIDTH

            levelGeneration(next_chunk, start_x)

    # Window dispay
    display()


# Displays the score in console
score, count, secs = score(current_time)
print('Score:', score)
filename = "data"
save(filename, player_name, reversed_screen, score, count, secs, chunk_times, NBR_CHUNK)

pygame.quit()
quit