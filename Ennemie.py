import pygame

class Ennemie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie=100
        self.vieMax=100
        self.vitesse=10
        self.perso=pygame.image.load("Image/Perso.png")
        self.getRect=self.perso.get_rect()
        self.getRect.x=500
        self.getRect.y=500
        self.saut=False
        self.nbJumpMax=20
        self.nbJump=0
        self.vitesseChute=0

