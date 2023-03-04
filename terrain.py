import csv

import pygame

from ImportCsv import import_csv, cartes
from Personnage import Personnage


class Tuiles(pygame.sprite.Sprite):
    def __init__(self,taille,x,y,screen):
        super().__init__()
        self.image=screen
        self.rect=self.image.get_rect(topleft=(x,y))

class TuilesFin(Tuiles):
    def __init__(self,size,x,y,screen):
        super().__init__(size,x,y,screen)
        self.image=screen

class Terrain:
    #on attribue les images nécessaire pour construire la map en fonction du csv
    def __init__(self, screen):
        self.display = screen
        self.terrain_lay = import_csv("Image/Map.csv")
        self.sprites = self.tuiles()


    def tuiles(self):
        sprite_grp = pygame.sprite.Group()
        for index, colonne in enumerate(self.terrain_lay):
            for col_index, val in enumerate(colonne):
                if val != '-1':
                    x = col_index * 32  # 32 est la taille du pixel
                    y = index * 32
                    self.imageTerrain = cartes("Image/Map.jpg")
                    surface = self.imageTerrain[int(val)]
                    sprite = TuilesFin(32, x, y, surface)
                    sprite_grp.add(sprite)
        return sprite_grp

    def run(self):
        self.sprites.draw(self.display)



