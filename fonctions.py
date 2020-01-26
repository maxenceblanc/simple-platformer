#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 11/2019
########################

# IMPORTS
import pygame
from random import *
from pygame.locals import *
import math
import pandas as pd

# IMPORTS DE FICHIERS
from levels import *

##############################
######>> CHANGE HERE <<#######
##############################
invertCommand = "" # "reverse" or ""
##############################
##############################


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
        blocks.append(self) # Add it to the block list #TODO: remove the inside append
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


    def move(self):

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

        self.collisions(self.vitesse_x, 0)

        self.rect.y += self.vitesse_y
        self.collisions(0, self.vitesse_y)


    def collisions(self, vitesse_x, vitesse_y):

        for Block in blocks:
            if self.rect.colliderect(Block.rect):

                if vitesse_x > 0:
                    self.rect.right = Block.rect.left
                    freinage()
                elif vitesse_x < 0:
                    self.rect.left = Block.rect.right
                    freinage()

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

def levelGeneration(chunk, x_start) :
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
                Block(x,y)
            elif chunk[ligne][colonne] == "E":
                Block(x,y, type="end")

            y += BLOCK_HEIGHT # Goes downwards of one block

        x += BLOCK_WIDTH # Goes right of block
        y = (VISIBILITE_Y-1) * HAUTEUR_CHUNK * BLOCK_HEIGHT # Get back up

def endOfChunk():
    """ Detects if the last block from the last chunk is on screen.

    OUTPUT: 
            True if last block is on screen
            False otherwise
    """

    if blocks[-1].rect.x < TAILLE_X:
        return(True)
    return(False)

### INTERACTIONS PERSONNAGE ### --------------------

def bouge():
    """ Detects pressed keys and changes speeds accordingly. 
    Then applies slowdowns.
    """

    k = pygame.key.get_pressed()

    # Horizontal movements #

    # Left
    if k[TOUCHE_GAUCHE]:
        if Perso.vitesse_x > 0:
            freinage()
        else:
            Perso.vitesse_x -= ACCELERATION_X
    # Right
    elif k[TOUCHE_DROITE]:
        if Perso.vitesse_x < 0:
            freinage()
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
    if not sol():
        Perso.vitesse_y += ACCELERATION_Y

    if k[TOUCHE_HAUT] and sol(): # Up
        Perso.vitesse_y = -VITESSE_Y # - to go upwards

    # x speed limit
    if Perso.vitesse_x < -VITESSE_X:
        Perso.vitesse_x = -VITESSE_X
    elif Perso.vitesse_x > VITESSE_X:
        Perso.vitesse_x = VITESSE_X

    # Applies speeds to the Player
    Perso.move()

def freinage():
    """
    """

    if 1 > Perso.vitesse_x / FREINAGE_X > -1 : Perso.vitesse_x = 0
    elif Perso.vitesse_x < 0 : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)
    else : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)

def sol():
    """ Detects if a Block is under the Player
    """
    
    for Block in blocks:
        for pixel in range(-(BLOCK_WIDTH-1),BLOCK_WIDTH):
            if Perso.rect.bottom == Block.rect.top and Perso.rect.left == Block.rect.left + pixel:
                return True
    return False



### WINDOW DISPLAY ### --------------------------

def camera():
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

def display():
    """ Updates the display
    """

    FENETRE.fill(GRIS) # background of FENETRE

    # Draws each Block
    for Block in blocks:
        pygame.draw.rect(FENETRE, BLANC, Block.rect)

    pygame.draw.rect(FENETRE, ORANGE, Perso.rect) # draws the player

    ### Free space for object display ###

    pygame.display.update() # refreshes FENETRE

def score(secs):
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

def save(filename, player_name, reversed_screen, score, count, secs, chunk_times, nb_chunks):
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
            'reversed_screen',
            'inverted_keys',
            'score',
            'count',
            'time'
        ]+['chunk_'+str(i) for i in range(1,nb_chunks+1)])

    attempt_n = data[data.name==player_name].shape[0]+1
    # creates new entry
    new_entry = {
        'name':player_name,
        'attempt_n':attempt_n,
        'reversed_screen': reversed_screen,
        'inverted_keys': True if invertCommand=='reverse' else False,
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

# List of all the Blocks
blocks = []

chunk_lenght = 0 # unused at the moment



###################################################
##################| CONSTANTS |####################
###################################################

# Coefficient of Proportions (to increase physics proportionally)
PROPORTION = 1

# Size of blocks
BLOCK_WIDTH  = 16 * PROPORTION
BLOCK_HEIGHT = 16 * PROPORTION

# For the display
VISIBILITE_X = 45 # Width of FENETRE in amount of blocks.
VISIBILITE_Y = 2 # Height of FENETRE in amount of chunk height.
TAILLE_X = BLOCK_WIDTH * VISIBILITE_X # Width of FENETRE in pixels.
TAILLE_Y = HAUTEUR_CHUNK * BLOCK_HEIGHT * VISIBILITE_Y # Height of FENETRE in pixels.

# Player size
Perso_WIDTH  = 1 * BLOCK_WIDTH
Perso_HEIGHT = 2 * BLOCK_HEIGHT

# Start
START_X = 0
START_Y = TAILLE_Y - BLOCK_HEIGHT - Perso_HEIGHT

# Colours
BLANC = (255, 255, 255)
GRIS = (30,30,30)
ORANGE = (255, 125, 0)
ROUGE = (255, 0, 0)

# Acceleration
ACCELERATION_X = 1 * PROPORTION
ACCELERATION_Y = 1.67 * PROPORTION
COEFF_ACCELERATION_X = 1.3
FREINAGE_X = COEFF_ACCELERATION_X * ACCELERATION_X
# Speed
VITESSE_X = 16 * PROPORTION # vitesse_x max
VITESSE_Y = BLOCK_HEIGHT * (14/16) # vitesse_y max
# Camera speed
VITESSE_CAMERA_X = 80 * PROPORTION
VITESSE_CAMERA_Y = 5 * PROPORTION

# Init the Player
Perso = Player()

# Display Setup
FENETRE = pygame.display.set_mode((TAILLE_X, # Dimensions of FENETRE
                                   TAILLE_Y))

# Time
CLOCK = pygame.time.Clock()

# Keys
TOUCHE_DROITE = K_d
TOUCHE_GAUCHE = K_q
TOUCHE_HAUT   = K_z

if invertCommand == "rot":
    TOUCHE_DROITE = K_z
    TOUCHE_GAUCHE = K_d
    TOUCHE_HAUT   = K_q

elif invertCommand == "reverse":
    TOUCHE_DROITE = K_q
    TOUCHE_GAUCHE = K_d
    TOUCHE_HAUT   = K_z

# Camera keys
CAMERA_DROITE    = K_RIGHT
CAMERA_GAUCHE    = K_LEFT
