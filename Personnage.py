import pygame
from pygame.locals import*

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.vie=100
        self.vieMax=00
        self.vitesse=10
        self.perso=pygame.image.load("Image/Perso.png")
        self.getRect=self.perso.get_rect()
        self.getRect.x=200
        self.getRect.y=380

    def bouger_droite(self):
        self.getRect.x+=self.vitesse

    def bouger_gauche(self):
        self.getRect.x-=self.vitesse
