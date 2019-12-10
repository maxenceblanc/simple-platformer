#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.7
# Author: Maxence BLANC
# Date created : 11/19
# Titre du Fichier : Boucle de Jeu
########################

# IMPORTS
import sys
import pygame
from pygame.locals import *

arguments = sys.argv
player_name = ""

if len(arguments) != 2:
    print("ERROR: Wrong args. Should be like : \n\npython3 main.py reverse\n\nor\n\npython3 main.py")
    exit()

else:
    player_name = arguments[1]


# IMPORTS DE FICHIERS
from fonctions import *

# Initialise pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # Titre de la Fenetre


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

    print(chunk_num, len(niveau))

    # Charge le chunk suivant si nécessaire
    if endOfChunk():

        # On selectionne le prochain chunk à générer dans la liste des chunks
        if chunk_num < len(niveau):
            next_chunk = niveau[chunk_num]
            chunk_num += 1

            # On trouve la coordonnée x où commencer la génération
            start_x = blocks[-1].rect.x + BLOCK_WIDTH

            levelGeneration(next_chunk, start_x)

    # Affichage dans la fenetre
    display()


# Affichage du score dans la console
score, count, secs = score()
print('Score:', score)
filename = "data"
save(filename, player_name, score, count, secs)

pygame.quit()
quit
