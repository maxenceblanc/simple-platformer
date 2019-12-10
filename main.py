#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.7
# Author: Maxence BLANC
# Date created : 11/19
# Titre du Fichier : Boucle de Jeu
########################

# IMPORTS
import pygame
from pygame.locals import *

# IMPORTS DE FICHIERS
from fonctions import *

# Initialise pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # Titre de la Fenetre

score = 0
chunk_num = 0

over = False

# Génère le premier chunk et retourne sa longueur en block
levelGeneration(niveau[0], 0)

while not over:

    CLOCK.tick(20) # 20 FPS

    for e in pygame.event.get():
        pygame.event.set_allowed(None)
        pygame.event.set_allowed((QUIT, MOUSEBUTTONDOWN, KEYDOWN))
        pygame.event.pump()

        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_RETURN): # condition pour quitter
            over = True

    if Perso.rect.y + Perso_HEIGHT > TAILLE_Y:
        over = True

    # Deplace la camera si besoin
    camera()

    # Bouge le Perso
    bouge()

    # Charge le chunk suivant si nécessaire
    if endOfChunk():

        # On selectionne le prochain chunk à générer dans la liste des chunks
        if chunk_num < len(niveau)-1:
            next_chunk = niveau[chunk_num]
            chunk_num += 1

            # On trouve la coordonnée x où commencer la génération
            start_x = blocks[-1].rect.x + BLOCK_WIDTH

            levelGeneration(next_chunk, start_x)

    # Affichage dans la fenetre
    display()


# Affichage du score dans la console
score()

#FIXME: save(filename, player_name, score)

pygame.quit()
quit
