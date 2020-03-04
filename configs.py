#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.6.9
# Author : Maxence Blanc - https://github.com/maxenceblanc
# Creation Date : 03/2020
########################

from pygame.locals import *

from levels import *


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
ACCELERATION_Y = 1.67 * PROPORTION #1.67
COEFF_ACCELERATION_X = 1.3
FREINAGE_X = COEFF_ACCELERATION_X * ACCELERATION_X
# Speed
VITESSE_X = 16 * PROPORTION # vitesse_x max
VITESSE_Y = BLOCK_HEIGHT * (14/16) # vitesse_y max
# Camera speed
VITESSE_CAMERA_X = 80 * PROPORTION
VITESSE_CAMERA_Y = 5 * PROPORTION


# Keys
TOUCHE_DROITE = K_d
TOUCHE_GAUCHE = K_q
TOUCHE_HAUT   = K_z

# Camera keys
CAMERA_DROITE    = K_RIGHT
CAMERA_GAUCHE    = K_LEFT
