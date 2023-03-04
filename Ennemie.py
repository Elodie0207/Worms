import pygame
from pygame.locals import*
from Armes import  Armes
from Map import Map
from Personnage import Personnage


class Ennemie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie=100
        self.vieMax=100
        self.vitesse=10
        self.image=pygame.image.load("Image/Perso.png")
        self.grenade=pygame.image.load("Image/grenade.png")
        self.rect=self.image.get_rect()
        self.rect.x=700
        self.rect.y=500
        self.saut=False
        self.nbJumpMax=20
        self.nbJump=0
        self.vitesseChute=0
        self.grenadeObj= Map(self.rect.x, self.rect.y, 50, 60)
        self.player=Personnage()

    def draw(self,screen):
        wallList=pygame.sprite.Group()
        wallList.add(self.grenadeObj)
        wallList.draw(screen)

    def update(self):

        self.grenadeObj.rect.x+=50
        self.grenadeObj.rect.y-=40
    def bouger_droite(self):
        self.rect.x+=self.vitesse

    def bouger_gauche(self):
        self.rect.x-=self.vitesse

    def sauter(self):
        if self.saut is True:
            self.rect.y -= self.nbJump
            if self.nbJump > -self.nbJumpMax:
                self.nbJump -=1
            else:
                self.saut=False

    def vies(self):
        if self.player.grenadeObj.rect.x== self.rect.x:
            self.vie-=20


