import pygame
import math

#trajectoire de la balle
class trajectoire:
    def __init__(self,point,color,radius):
        self.color=color
        self.radius=radius
        self.color=(255,0,0)
        self.radius=3
        self.point=point
    def draw(self,screen):
        for points in self.point:
            pygame.draw.circle(screen,self.color,self.point,self.radius)


