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
import config as cfg

# Sub-modules


##################################
############| BLOCKS |############
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

class Block():
    """ block entity.

        INPUTS: 
                x coordinate
                y coordinate
                type of the block (str)
        """

    def __init__(self, block_x, block_y, type='default'):
        
        # Applies coordinates and sizes.
        self.rect = pygame.Rect(block_x, block_y, cfg.BLOCK_WIDTH, cfg.BLOCK_HEIGHT)

        # Sets block attributes
        self.type = type

    def move(self, distance_x, distance_y):
        """ Moves the blocks relatively.

        INPUTS: 
                distance in x
                distance in y
        """
        self.rect.x += distance_x
        self.rect.y += distance_y

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
    