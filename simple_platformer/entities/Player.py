#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6
# Author : Maxence Blanc - https://github.com/maxenceblanc
########################

# IMPORTS
import sys
import pygame

# FILE IMPORTS
import game_config as cfg

# Sub-modules

##################################
############| PLAYER |############
##################################

""" TO DO LIST ✔✘
"""

""" PROBLEMS
"""

""" NOTES
"""

####################################################
###################| CLASSES |######################
####################################################

class Player():
    """ Player entity.
    """

    def __init__(self):
        self.rect = pygame.Rect(cfg.START_X, cfg.START_Y, cfg.PLAYER_WIDTH, cfg.PLAYER_HEIGHT)
        self.speed_x = 0
        self.speed_y = 0


    def move(self, blocks):
        """ Moves the player.
        
        INPUTS: 
                list of blocks from the level.
        """

        self.rect.x += self.speed_x

        # Correcting not to get past the middle of the screen
        if self.rect.x > cfg.SIZE_X/2:
            self.rect.x = cfg.SIZE_X/2

        # Correcting not to get past the left side of the screen
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed_x = 0

        # Moves the level when the Player reaches the middle of the screen
        if self.rect.x == cfg.SIZE_X/2 and self.speed_x > 0:
            for block in blocks:
                block.move (-self.speed_x, 0)

        self.collisions(self.speed_x, 0, blocks)

        self.rect.y += self.speed_y
        self.collisions(0, self.speed_y, blocks)


    def collisions(self, speed_x, speed_y, blocks):
        """ Handling of collisions when moving the player.
        
        INPUTS: 
                speed in x
                speed in y
                list of blocks from the level
        """

        for block in blocks:
            if self.rect.colliderect(block.rect):

                if speed_x > 0:
                    self.rect.right = block.rect.left
                    self.slowdown()
                elif speed_x < 0:
                    self.rect.left = block.rect.right
                    self.slowdown()

                if speed_y > 0:
                    self.rect.bottom = block.rect.top
                    self.speed_y = 0
                elif speed_y < 0:
                    self.rect.top = block.rect.bottom
                    self.speed_y = 0


    def slowdown(self):
        """ Slows the player down.

        INPUTS:
                player object
        """

        if 1 > self.speed_x / cfg.SLOWDOWN__X > -1 :
            self.speed_x = 0

        else: 
            self.speed_x = int(self.speed_x / cfg.SLOWDOWN__X)

####################################################
##################| FUNCTIONS |#####################
####################################################


####################################################
##################| VARIABLES |#####################
####################################################


####################################################
###################| CONSTANTS |####################
####################################################


####################################################
####################| PROGRAM |#####################
####################################################

if __name__ == "__main__" :
    pass
    