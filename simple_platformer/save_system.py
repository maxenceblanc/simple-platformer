#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6
# Author : Maxence Blanc - https://github.com/maxenceblanc
########################

# IMPORTS
import sys

import pandas as pd

# FILE IMPORTS

# Sub-modules


#######################################
############| SAVE SYSTEM |############
#######################################

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
    