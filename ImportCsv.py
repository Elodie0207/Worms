from csv import reader

import pygame
import csv


#Fonction qui va lire et enregistrer la Map sous forme csv
def import_csv(file):
    mapListe=[]
    with open(file) as fichier:
        map=reader(fichier,delimiter=",")
        for colonne in map:
            mapListe.append(list(colonne))
        return mapListe



def cartes(file):
    screen=pygame.image.load((file)).convert_alpha()
    x=int(screen.get_size()[0]/32)
    y=int(screen.get_size()[1]/32)

    #differente partie de la tuile
    partie=[]
    for ligne in range(y):
        for colonne in range(x):
            posX=colonne*32
            posY=ligne*32
            surface=pygame.Surface((32,32))
            surface.blit(screen,(0,0),pygame.Rect(posX,posY,32,32))
            partie.append(surface)

    return partie
