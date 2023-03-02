import pygame
import math

class Armes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vitesse=5
        self.image= pygame.image.load("Image/grenade.png")
        self.rect=self.image.get_rect()

