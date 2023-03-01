import pygame
from pygame.locals import*

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.vie=100
        self.vieMax=100
        self.vitesse=10
        self.perso=pygame.image.load("Image/Perso.png")
        self.getRect=self.perso.get_rect()
        self.getRect.x=200
        self.getRect.y=500
        self.saut=False
        self.nbJumpMax=20
        self.nbJump=0
        self.vitesseChute=0

    def bouger_droite(self):
        self.getRect.x+=self.vitesse

    def bouger_gauche(self):
        self.getRect.x-=self.vitesse

    def sauter(self):
        if self.saut is True:
            self.getRect.y -= self.nbJump
            if self.nbJump > -self.nbJumpMax:
                self.nbJump -=1
            else:
                self.saut=False

    def vie(self,screen):
        self.barreVie=pygame.Surface((self.getRect.width,5))
        self.barreCouleur.fill((255,0,0))


