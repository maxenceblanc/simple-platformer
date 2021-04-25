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

class DemoRecorder():

    def __init__(self, app):

        self.app = app

    def recordState(self, state):
        """
        """

        state = recording_system.serializeState(self.app)
        recording_system.saveDemo(state, self.app.player_name, cfg.MAP_NAME)


    def serializeState(self):
        """ Saves the current state of the game. This is to be able to replicate
        states in a replay system.
        """

        game_state_serialized = pickle.dumps(self.app)

        return game_state_serialized
    

    def saveDemo(demo, player_name, map_name):
        """ Saves all the demo data into a file of the demo folder.
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


    def loadState(self, filename):

        with open(os.path.join(config.DEMO_FOLDER, filename), "rb") as demo_file: # "b" for byte
            game = pickle.load(demo_file)

        self.app.__dict__ = game.__dict__

####################################################
##################| FUNCTIONS |#####################
####################################################

### Recording System ### --------------------



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
    