import pygame

from Personnage import Personnage


class Tuiles(pygame.sprite.Sprite):
    def __init__(self,taille,x,y):
        super().__init__()
        self.image=pygame.Surface((taille,taille))
        self.image.fill('grey')
        self.rect=self.image.get_rect(topleft=(x,y))
        self.perso=Personnage()

#Classe qui hérite de la classe Tuiles
class TuilesFin(Tuiles):
    def __init__(self,size,x,y,screen):
        super().__init__(size,x,y)
        self.image=screen


