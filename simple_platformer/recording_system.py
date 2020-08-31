#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6
# Author : Maxence Blanc - https://github.com/maxenceblanc
########################

# IMPORTS
import sys
import os
import time

import pickle


# CUSTOM IMPORTS
import config



############################################
############| RECORDING SYSTEM |############
############################################

""" TO DO LIST ✔✘
"""

""" PROBLEMS
"""

""" NOTES
"""

####################################################
###################| CLASSES |######################
####################################################


####################################################
##################| FUNCTIONS |#####################
####################################################

### Recording System ### --------------------

def serializeState(game):
    """ Saves the current state of the game. This is to be able to replicate
    states in a replay system.

    TODO
    """

    game_state_serialized = pickle.dumps(game)

    return game_state_serialized
    

def saveDemo(demo, player_name, map_name):
    """ Saves all the demo data into a file of the demo folder.
    
    TODO
    """

    t = time.gmtime()
    current_time = time.strftime('%Y-%m-%d_%H-%M-%S_%Z', t)

    name_list = [config.DEMO_PREFIX, current_time, player_name, map_name]
    name_list = [elt.replace(" ", "-") for elt in name_list]
    
    filename = "_".join(name_list) + ".txt"
    file_path = os.path.join(config.DEMO_FOLDER, filename)

    print(f"saved demo to {file_path}")

    with open(file_path, "wb") as demo_file:
        demo_file.write(demo)



def loadState(filename):

    with open(os.path.join(config.DEMO_FOLDER, filename), "rb") as demo_file: # "b" for byte
        game = pickle.load(demo_file)

    return game

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
    saveDemo("", "max", "First Land")
    