#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 11/2019
########################

# IMPORTS
import os
import sys
import pygame
from pygame.locals import *

# CUSTOM IMPORTS
import game_config as cfg
import config
import levels.levels as levels

import functions
import entities.Player

import save_system
import recording_system


""" TODO
Score refactoring
Add date to run data
TAS system (log + custom start)
Replay system
Scoreboard system (best time, bt per chunck)
training mode with options (like no death, mouse etc.)
"""


class Game():

    def __init__(self, random_gen, can_lose, player_name):


        self.random_gen = random_gen
        self.can_lose   = can_lose

        self.player_name = player_name
        
        # List of all the Blocks
        self.blocks = []

        # Init the player
        self.player = entities.Player.Player()

        
        # Inits TODO: explain variables
        self.chunk_num = 1 # 1 because of the init chunk
        self.prev_chunks_passed = 0

        self.chunk_times = []
        self.last_time = 0

    
    def __repr__(self):
        pass


    def idleLoop(self, WINDOW):
        """ Used this to wait for the user input to start time but still picture the level.
        That allows for time to start when the user presses a key rather than when 
        program starts.
        """

        ready = False # True when all chunks that should be visible are loaded
        start = False

        while not start:

            for e in pygame.event.get():
                pygame.event.set_allowed(None)
                pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
                pygame.event.pump()

            key = pygame.key.get_pressed()

            if key[cfg.KEY_LEFT] or key[cfg.KEY_RIGHT] or key[cfg.KEY_UP]:
                if pygame.time.get_ticks() / 1000 > 0.5: # Arbitrary, used to wait for the game to be fully loaded
                    start = True

            # Loads the next chunk if needed
            chunkWasLoaded = functions.levelGeneration(self.random_gen, self.blocks, levels.level, self.chunk_num)

            if chunkWasLoaded:
                self.chunk_num += 1
            elif not ready:
                print("ready")
                ready = True

            functions.display(WINDOW, self.blocks, self.player) # Window dispay


    def main(self, WINDOWn, CLOCK):
        """ Main function. Contains the main loop of the game.

        """

        # Loads the first chunk of the map
        functions.loadChunk(self.blocks, levels.level[0], 0)

        # Idle screen
        # Using this to wait for the user input to start time but still picture the level
        self.idleLoop(WINDOW)

        self.start_time = pygame.time.get_ticks() / 1000


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
                
                if e.type == KEYDOWN and e.key == cfg.KEY_RECORD:
                    functions.record(self)

                if e.type == KEYDOWN and e.key == cfg.KEY_LOAD:
                    self = recording_system.loadState("demo_2020-08-31_17-23-33_GMT_test_First-Land.txt")

            if self.player.rect.y + cfg.PLAYER_HEIGHT > cfg.SIZE_Y and self.can_lose:
                over = True

            # Moves the camera if needed
            functions.camera(self.player, self.blocks)

            # Moves the player when m1 is on click
            if pygame.mouse.get_pressed()[0]:
                functions.mouse(self.player)

            # Moves the player
            functions.move(self.player, self.blocks)

            # Not very viable but works for that list length
            chunks_passed = 0
            for block in self.blocks:
                if block.type == "end" and block.rect.x < self.player.rect.x:
                    chunks_passed+=1
            
            if chunks_passed == self.prev_chunks_passed + 1:
                self.current_time = pygame.time.get_ticks() / 1000 - self.start_time
                print("chunk n°", chunks_passed, ": ", self.current_time)

                self.chunk_times.append(round(self.current_time-self.last_time, 3))
                self.last_time = self.current_time
                self.prev_chunks_passed+=1


            # Loads the next chunk if needed
            chunkWasLoaded = functions.levelGeneration(self.random_gen, self.blocks, levels.level, self.chunk_num)

            if chunkWasLoaded:
                self.chunk_num += 1

            functions.display(WINDOW, self.blocks, self.player) # Window dispay


        # Displays the score in console
        score, chunks_passed, end_time = functions.score_func(self.current_time, self.player, self.blocks)
        print('Chunk nb:', chunks_passed, 'Time:', end_time)
        print('Score:', score)

        # Saving
        filename = os.path.join(config.DATA_FOLDER, config.DATA_FILE)
        save_system.save(filename, self.player_name, score, chunks_passed, end_time, self.chunk_times, levels.NB_CHUNK)




if __name__ == "__main__":

    # Solving launch args
    arguments = sys.argv
    player_name = ""

    if len(arguments) != 2:
        print("ERROR: Wrong args. Should be like : \n\npython3 main.py name_of_player")
        exit()
    else:
        player_name = arguments[1]

    # Additional options
    random_gen = cfg.RANDOM_GEN
    can_lose = cfg.CAN_LOSE


    # Initializes pygame
    pygame.init()

    # Time
    CLOCK = pygame.time.Clock()

    # Display Setup
    pygame.display.set_caption("simple platformer") # sets the window's title
    WINDOW = pygame.display.set_mode((cfg.SIZE_X, # Dimensions of WINDOW
                                      cfg.SIZE_Y))

    game = Game(random_gen, can_lose, player_name)
    game.main(WINDOW, CLOCK)

    pygame.quit()
    quit()
