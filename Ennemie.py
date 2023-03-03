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
        self.perso=pygame.image.load("Image/Perso.png")
        self.grenade=pygame.image.load("Image/grenade.png")
        self.getRect=self.perso.get_rect()
        self.getRect.x=700
        self.getRect.y=450
        self.saut=False
        self.nbJumpMax=20
        self.nbJump=0
        self.vitesseChute=0
        self.grenadeObj= Map(self.getRect.x,self.getRect.y,50,60)
        self.player=Personnage()
    def draw(self,screen):
        wallList=pygame.sprite.Group()
        wallList.add(self.grenadeObj)
        wallList.draw(screen)

    def update(self):

        self.grenadeObj.rect.x+=50
        self.grenadeObj.rect.y-=40
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

    def vies(self):
        if self.player.grenadeObj.rect.x== self.getRect.x:
            self.vie-=20


