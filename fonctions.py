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
from levels import *
from configs import *


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

class Block(object):

    def __init__(self, block_x, block_y, type='default'):
        """ Creates a Block.

        INPUTS: 
                x coordinate
                y coordinate
        """
        # Applies coordinates and sizes.
        self.rect = pygame.Rect(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT)
        # blocks.append(self) # Add it to the block list #TODO: remove the inside append
        self.type = type

    def move(self, distance_x, distance_y):
        """ Moves the blocks relatively.

        INPUTS: 
                distance in x
                distance in y
        """
        self.rect.x += distance_x
        self.rect.y += distance_y # unused here

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(START_X, START_Y, Perso_WIDTH, Perso_HEIGHT)
        self.vitesse_x = 0
        self.vitesse_y = 0


    def move(self, blocks):

        self.rect.x += self.vitesse_x

        # Ajusting not to get past the middle of the screen
        if self.rect.x > TAILLE_X/2:
            self.rect.x = TAILLE_X/2

        # Ajusting not to get past the left side of the screen
        if self.rect.x < 0:
            self.rect.x = 0
            self.vitesse_x = 0

        # Moves the level when the Player reaches the middle of the screen
        if self.rect.x == TAILLE_X/2 and self.vitesse_x > 0:
            for Block in blocks:
                Block.move (-self.vitesse_x, 0)

        self.collisions(self.vitesse_x, 0, blocks)

        self.rect.y += self.vitesse_y
        self.collisions(0, self.vitesse_y, blocks)


    def collisions(self, vitesse_x, vitesse_y, blocks):

        for Block in blocks:
            if self.rect.colliderect(Block.rect):

                if vitesse_x > 0:
                    self.rect.right = Block.rect.left
                    freinage(self, blocks)
                elif vitesse_x < 0:
                    self.rect.left = Block.rect.right
                    freinage(self, blocks)

                if vitesse_y > 0:
                    self.rect.bottom = Block.rect.top
                    self.vitesse_y = 0
                elif vitesse_y < 0:
                    self.rect.top = Block.rect.bottom
                    self.vitesse_y = 0

####################################################
##################| FONCTIONS |#####################
####################################################

### LEVEL GENERATION ### ----------------------

def levelGeneration(block_list, chunk, x_start) :
    """ Loads the chunk from the start coordinate.

    INPUTS: 
            the chunk to be loaded, [str, ..]
            the start coordinate

    VARIABLES: 
                x = x coordinate of the next block to be created
                y = y coordinate of the next block to be created
    """

    # Sets the stardu joueur dans unt for the generation.
    x, y = x_start, (VISIBILITE_Y-1) * HAUTEUR_CHUNK * BLOCK_HEIGHT


    # Generation
    for colonne in range(len(chunk[0])):

        for ligne in range(len(chunk)):

            if chunk[ligne][colonne] == "W":
                block_list.append(Block(x,y))
            elif chunk[ligne][colonne] == "E":
                block_list.append(Block(x,y, type="end"))

            y += BLOCK_HEIGHT # Goes downwards of one block

        x += BLOCK_WIDTH # Goes right of block
        y = (VISIBILITE_Y-1) * HAUTEUR_CHUNK * BLOCK_HEIGHT # Get back up

def endOfChunk(blocks):
    """ Detects if the last block from the last chunk is on screen.

    OUTPUT: 
            True if last block is on screen
            False otherwise
    """

    if blocks[-1].rect.x < TAILLE_X:
        return(True)
    return(False)

### INTERACTIONS PERSONNAGE ### --------------------

def bouge(Perso, blocks):
    """ Detects pressed keys and changes speeds accordingly. 
    Then applies slowdowns.
    """

    k = pygame.key.get_pressed()

    # Horizontal movements #

    # Left
    if k[TOUCHE_GAUCHE]:
        if Perso.vitesse_x > 0:
            freinage(Perso, blocks)
        else:
            Perso.vitesse_x -= ACCELERATION_X
    # Right
    elif k[TOUCHE_DROITE]:
        if Perso.vitesse_x < 0:
            freinage(Perso, blocks)
        else:
            Perso.vitesse_x += ACCELERATION_X

    # Gentle slowdowns if L/R keys aren't in use
    else:
        if Perso.vitesse_x > 0:
            Perso.vitesse_x -= 1
        elif Perso.vitesse_x < 0:
            Perso.vitesse_x += 1

    # Vertical movements #

    # Gravity
    if not sol(Perso, blocks):
        Perso.vitesse_y += ACCELERATION_Y

    if k[TOUCHE_HAUT] and sol(Perso, blocks): # Up
        Perso.vitesse_y = -VITESSE_Y # - to go upwards

    # x speed limit
    if Perso.vitesse_x < -VITESSE_X:
        Perso.vitesse_x = -VITESSE_X
    elif Perso.vitesse_x > VITESSE_X:
        Perso.vitesse_x = VITESSE_X

    # Applies speeds to the Player
    Perso.move(blocks)

def freinage(Perso, blocks):
    """
    """

    if 1 > Perso.vitesse_x / FREINAGE_X > -1 : Perso.vitesse_x = 0
    elif Perso.vitesse_x < 0 : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)
    else : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)

def sol(Perso, blocks):
    """ Detects if a Block is under the Player
    """
    
    for Block in blocks:
        for pixel in range(-(BLOCK_WIDTH-1),BLOCK_WIDTH):
            if Perso.rect.bottom == Block.rect.top and Perso.rect.left == Block.rect.left + pixel:
                return True
    return False



### WINDOW DISPLAY ### --------------------------

def camera(Perso, blocks):
    """ Moves the camera.
    """

    k = pygame.key.get_pressed()

    if k[CAMERA_DROITE]:
        for Block in blocks:
            Block.move(-VITESSE_CAMERA_X, 0)

        Perso.rect.x -= VITESSE_CAMERA_X

    elif k[CAMERA_GAUCHE]:
        for Block in blocks:
            Block.move(VITESSE_CAMERA_X, 0)

        Perso.rect.x += VITESSE_CAMERA_X

def display(fenetre, blocks, Perso):
    """ Updates the display
    """

    fenetre.fill(GRIS) # background of FENETRE

    # Draws each Block
    for Block in blocks:
        pygame.draw.rect(fenetre, BLANC, Block.rect)

    pygame.draw.rect(fenetre, ORANGE, Perso.rect) # draws the player

    ### Free space for object display ###

    pygame.display.update() # refreshes FENETRE

def score_func(secs, Perso, blocks):
    """ Score according to speed (Block/sec) and distance traveled
    """

    count = 0

    for block in blocks:
        if block.type == "end" and block.rect.x < Perso.rect.x:
            count+=1

    final = pygame.time.get_ticks() / 1000
    pos_weight = 2.5
    spe_weight = 1
    score = count*pos_weight + ((count*20)/secs**1.5)*spe_weight
    print('Chunk nb:', count, 'Time:', final)
    return(round(score,1), count, final)

### CSV SAVE ### --------------------------

def save(filename, player_name, score, count, secs, chunk_times, nb_chunks):
    """ Saves the player's score in a csv.
    """

    if len(chunk_times)>nb_chunks:
        raise Exception('Number of chunks incorrect.')
    
    # Loads the data into a DataFrame or create a new DataFrame
    try:
        data = pd.read_csv(filename+'.csv')
    except:
        data = pd.DataFrame(columns=[
            'name',
            'attempt_n',
            'score',
            'count',
            'time'
        ]+['chunk_'+str(i) for i in range(1,nb_chunks+1)])

    attempt_n = data[data.name==player_name].shape[0]+1
    # creates new entry
    new_entry = {
        'name':player_name,
        'attempt_n':attempt_n,
        'score':score,
        'count': count,
        'time': secs
    }
    new_entry.update({'chunk_'+str(i): chunk_times[i-1] for i in range(1,len(chunk_times)+1)})
    
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


