#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.5.2
# Author: Maxence BLANC
# Last modified : 10/17
# Titre du Fichier : Fonctions et Classes
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
######## CHANGE HERE #########
##############################
invertCommand = "" # "reverse" or ""
##############################
##############################


""" TO DO LIST
? fix minor impacts ajustments
ADD Explosion effect
"""


""" PROBLEMS
PB :
Ans :
"""

""" NOTES




les coordonnées fonctionnent ainsi:
0 - - - - -> (x)
|
|
|
v (y)
"""


""" Commentaires
A quoi sert la fonction. Comment elle marche
Entrée :
Variables :
Sortie :
"""


####################################################
###################| CLASSES |######################
####################################################

class Block(object):

    def __init__(self, block_x, block_y, type='default'):
        """ Genere un Block.
        Entrée : coordonnée en x
                 coordonnée en y
        """
        # Pour chaque block, on lui applique ses coordonnées et ses dimensions.
        self.rect = pygame.Rect(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(self) # On l'ajoute à la liste des Block
        self.type = type

    def move(self, distance_x, distance_y):
        """ Déplace relativement les blocks.
        Entrée : la distance à parcourir en x
                 la distance à parcourir en y
        """
        self.rect.x += distance_x
        self.rect.y += distance_y # inutilisé ici

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(START_X, START_Y, Perso_WIDTH, Perso_HEIGHT)
        self.vitesse_x = 0
        self.vitesse_y = 0


    def move(self):

        self.rect.x += self.vitesse_x

        # Ajustement pour ne pas dépasser le milieu
        if self.rect.x > TAILLE_X/2:
            self.rect.x = TAILLE_X/2

        # et le coté gauche de la FENETRE
        if self.rect.x < 0:
            self.rect.x = 0
            self.vitesse_x = 0

        # Pour faire avancer la map quand Perso est au milieu
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

### GENERATION DU TERRAIN ### ----------------------

def levelGeneration(chunk, x_start) :
    """ Génère le chunk à partir de la coordonnée de départ.
    Entrée : Le chunk à générer (liste de str)
             La coordonnée x de départ
    Variables : x = coordonnées x du prochain block à générer
                y = coordonnées y du prochain block à générer
    """

    # On place le point de départ pour la génération.
    x, y = x_start, (VISIBILITE_Y-1) * HAUTEUR_CHUNK * BLOCK_HEIGHT


    # Génération
    for colonne in range(len(chunk[0])):

        for ligne in range(len(chunk)):

            if chunk[ligne][colonne] == "W":
                Block(x,y)
            elif chunk[ligne][colonne] == "E":
                Block(x,y, type="end")

            y += BLOCK_HEIGHT # On avance vers le bas d'un block.

        x += BLOCK_WIDTH # On avance vers la droite d'un block.
        y = (VISIBILITE_Y-1) * HAUTEUR_CHUNK * BLOCK_HEIGHT # On remonte

def endOfChunk():
    """ Detecte si le dernier block du dernier chunk est affiché.
    Sortie : True si le dernier block est affiché
             False sinon
    """
    if blocks[-1].rect.x < TAILLE_X:
        return(True)
    return(False)

### INTERACTIONS PERSONNAGE ### --------------------

def bouge():
    """ Detecte les touches appuyés et modifie les vitesses
    en conséquence. Applique ensuite le freinage
    """

    k = pygame.key.get_pressed()

    # Déplacements horizontaux #

    # Gauche
    if k[TOUCHE_GAUCHE]:
        if Perso.vitesse_x > 0:
            freinage()
        else:
            Perso.vitesse_x -= ACCELERATION_X
    # Droite
    elif k[TOUCHE_DROITE]:
        if Perso.vitesse_x < 0:
            freinage()
        else:
            Perso.vitesse_x += ACCELERATION_X

    # Ralentissement doux si les touches D/G ne sont pas utilisées
    else:
        if Perso.vitesse_x > 0:
            Perso.vitesse_x -= 1
        elif Perso.vitesse_x < 0:
            Perso.vitesse_x += 1

    # Déplacements verticaux #

    # Gravité
    if not sol():
        Perso.vitesse_y += ACCELERATION_Y

    if k[TOUCHE_HAUT] and sol(): # Haut
        Perso.vitesse_y = -VITESSE_Y # - pour aller vers le haut

    # Limitation de vitesse_x
    if Perso.vitesse_x < -VITESSE_X:
        Perso.vitesse_x = -VITESSE_X
    elif Perso.vitesse_x > VITESSE_X:
        Perso.vitesse_x = VITESSE_X

    # Applique les vitesses au Perso
    Perso.move()

def freinage():
    """
    """
    if 1 > Perso.vitesse_x / FREINAGE_X > -1 : Perso.vitesse_x = 0
    elif Perso.vitesse_x < 0 : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)
    else : Perso.vitesse_x = int(Perso.vitesse_x / FREINAGE_X)

def sol():
    """ Detecte si un Block se trouve sous le Perso
    """
    for Block in blocks:
        for pixel in range(-(BLOCK_WIDTH-1),BLOCK_WIDTH):
            if Perso.rect.bottom == Block.rect.top and Perso.rect.left == Block.rect.left + pixel:
                return True
    return False



### AFFICHAGE FENETRE ### --------------------------

def camera():
    """ Deplace la camera
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
    """ Met à jour l'affichage
    """
    FENETRE.fill(GRIS) # Fond de FENETRE

    # Dessine chaque Block
    for Block in blocks:
        pygame.draw.rect(FENETRE, BLANC, Block.rect)

    pygame.draw.rect(FENETRE, ORANGE, Perso.rect) # Dessine le Perso

    ### Espace dispo pour affichage des objets ###

    pygame.display.update() # raffraichit la FENETRE

def score():
    """ Score en fonction de la vitesse (Block/sec) et de la distance parcourue
    """
    count = 0

    for block in blocks:
        if block.type == "end" and block.rect.x < Perso.rect.x:
            count+=1

    # speed = -blocks[0].rect.x / BLOCK_WIDTH * 1000 / pygame.time.get_ticks() # blocks par seconde
    # score = -blocks[0].rect.x / BLOCK_WIDTH / 10 * speed # blocks au carré par seconde

    # print(str(int(speed)) + " speed et " + str(int(score)) + "pts")
    secs = pygame.time.get_ticks() / 1000
    pos_weight = 5
    spe_weight = 1
    score = count*pos_weight + ((count*20)/secs)*spe_weight
    print('Chunk nb:', count, 'Time:', secs)
    return(round(score,1))

### ENREGISTREMENT CSV ### --------------------------

def save(filename, player_name, score):
    """ Enregistre le score du joueur dans un csv
    """
    data = pd.read_csv(filename+'.csv')
    attempt_n = data[data.name==player_name].shape[0]+1
    data.append({'name':player_name, 'attempt_n':attempt_n, 'score':score})
    data.to_csv(filename+'.csv', index=False)


####################################################
##################| VARIABLES |#####################
####################################################

# Liste de tout les block "Block"
blocks = []

chunk_lenght = 0 # inutilisé pour le moment



####################################################
##################| CONSTANTES |####################
####################################################

# Coefficient de Proportions (pour augmenter les physiques proportionnellement)
PROPORTION = 1

# Taille des blocks
BLOCK_WIDTH  = 16 * PROPORTION
BLOCK_HEIGHT = 16 * PROPORTION

# Pour l'affichage
VISIBILITE_X = 45 # Largeur de la FENETRE en nombre de block.
VISIBILITE_Y = 2 # Hauteur de la FENETRE en nombre de hauteur de chunk.
TAILLE_X = BLOCK_WIDTH * VISIBILITE_X # Largeur de la FENETRE en pixels.
TAILLE_Y = HAUTEUR_CHUNK * BLOCK_HEIGHT * VISIBILITE_Y # Hauteur de la FENETRE en pixels.

# Taille du Perso
Perso_WIDTH  = 1 * BLOCK_WIDTH
Perso_HEIGHT = 2 * BLOCK_HEIGHT

# Taille des Rocket
Rocket_WIDTH = BLOCK_WIDTH/2
Rocket_HEIGHT = BLOCK_HEIGHT/2

# Depart
START_X = 0
START_Y = TAILLE_Y - BLOCK_HEIGHT - Perso_HEIGHT

# Couleurs
BLANC = (255, 255, 255)
GRIS = (30,30,30)
ORANGE = (255, 125, 0)
ROUGE = (255, 0, 0)

# Acceleration
ACCELERATION_X = 1 * PROPORTION
ACCELERATION_Y = 1.67 * PROPORTION
COEFF_ACCELERATION_X = 1.3
FREINAGE_X = COEFF_ACCELERATION_X * ACCELERATION_X
# Vitesse
VITESSE_X = 16 * PROPORTION # vitesse_x max
VITESSE_Y = BLOCK_HEIGHT * (14/16) # vitesse_y max
# Vitesse camera
VITESSE_CAMERA_X = 80 * PROPORTION
VITESSE_CAMERA_Y = 5 * PROPORTION
# Vitesse Rocket
VITESSE_Rocket = VITESSE_X

# Propriétés des Explosion
Explosion_LIFETIME = 3
Explosion_RADIUS = 1.5 * BLOCK_WIDTH# en pixels

# Distance à laquelle les projectiles disparraissent
DISTANCE_LIMITE = TAILLE_X

# Init le Joueur
Perso = Player()

# Display Setup
FENETRE = pygame.display.set_mode((TAILLE_X, # Dimension de la FENETRE
                                   TAILLE_Y))

# Time
CLOCK = pygame.time.Clock()

# Commandes

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

# Commandes camera
CAMERA_DROITE    = K_RIGHT
CAMERA_GAUCHE    = K_LEFT
