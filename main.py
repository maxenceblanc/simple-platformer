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

if len(arguments) != 3:
    print("ERROR: Wrong args. Should be like : \n\npython3 main.py name_of_player normal\n\n")
    exit()

else:
    player_name = arguments[1]
    if arguments[2]=='normal':
        reversed_screen = False
    elif arguments[2]=='reverse':
        reversed_screen = True
    else:
        raise Exception('Invalide second argument. Should be: \n\nnormal or reverse\n\n')


# IMPORTS DE FICHIERS
from fonctions import *

# Initialise pygame
pygame.init()

# Display Setup
pygame.display.set_caption("simple platformer") # Titre de la Fenetre


chunk_num = 1

prev_count = 0

chunk_times = []

last_time = 0

# Génère le premier chunk et retourne sa longueur en block
levelGeneration(niveau[0], 0)

over = False
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

    # Not very viable but works for that list length
    count = 0
    for block in blocks:
        if block.type == "end" and block.rect.x < Perso.rect.x:
            count+=1
    
    if count == prev_count + 1:
        current_time = pygame.time.get_ticks() / 1000
        print("chunck n°", count, ": ", current_time)

        chunk_times.append(round(current_time-last_time, 3))
        last_time = current_time
        prev_count+=1


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
score, count, secs = score(current_time)
print('Score:', score)
filename = "data"
save(filename, player_name, reversed_screen, score, count, secs, chunk_times, NBR_CHUNK)

pygame.quit()
quit
