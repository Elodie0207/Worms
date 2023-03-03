import csv

import pygame

from ImportCsv import import_csv, cartes
from Personnage import Personnage
from Tuiles import Tuiles, TuilesFin


class Terrain:
    #on attribue les images nécessaire pour construire la map en fonction du csv
    def __init__(self, data, screen):
        self.display = screen
        terrain_lay = import_csv("Image/Map.csv")
        self.sprites = self.tuiles(terrain_lay)
        self.perso=Personnage()

    def tuiles(self, terrain):
        sprite_grp = pygame.sprite.Group()

        for index, colonne in enumerate(terrain):
            for col_index, val in enumerate(colonne):
                if val != '-1':
                    x = col_index * 32  # 32 est la taille du pixel
                    y = index * 32

                    imageTerrain = cartes("Image/Map.jpg")
                    surface = imageTerrain[int(val)]
                    sprite = TuilesFin(32, x, y, surface)
                    sprite_grp.add(sprite)
        return sprite_grp

    def run(self):
        self.sprites.draw(self.display)



