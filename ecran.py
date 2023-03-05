import pygame

ecran = (500, 500)
ECRAN = pygame.display.set_mode(ecran)
FPS = 60
pygame.display.set_caption("jeux geopo okonore")

BLEU = (0, 0, 255)

def afficher_ecran():
    ECRAN.fill(BLEU)
    
    pygame.display.update()