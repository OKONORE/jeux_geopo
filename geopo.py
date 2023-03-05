from random import randrange
import pygame
import os

import classes
import ecran

###########################

def sauvegarder(sauvegarde, data):
    with open(sauvegarde + ".pickles", "rw+b") as fichier:
        file.write(data)
    f.close()
    return

def charger(sauvegarde):
    with open(sauvegarde + ".pickles", "r") as fichier:
        data = file.read()
    f.close()
    return data

####### Surface

def main():
    en_fonction = True
    clock = pygame.time.Clock()

    while en_fonction:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_fonction = False


if __name__ == "__main__":
    main()
