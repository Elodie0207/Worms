import pygame
import math

class Armes(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.vitesse=5
        self.image= pygame.image.load("Image/grenade.png")
        self.color=(255,255,255)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),5)


    def update(self):
        self.y -=self.vitesse
