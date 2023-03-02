import pygame

from Personnage import Personnage
from Ennemie import Ennemie
from Armes import Armes

class Jeu:
    def __init__(self):
        self.personnage = Personnage()
        self.armes=Armes()
        self.touche = {}
        self.temps=60

    def bouger(self):
        if self.touche.get(pygame.K_d) and self.personnage.getRect.x + self.personnage.getRect.width < 1080:
            self.personnage.bouger_droite()
        elif self.touche.get(pygame.K_q) and self.personnage.getRect.x > 0:
            self.personnage.bouger_gauche()

        elif self.touche.get(pygame.K_SPACE) and self.personnage.saut is False:
            self.personnage.saut = True
            self.personnage.nbJump = self.personnage.nbJumpMax

        if self.personnage.saut is True:
            self.personnage.sauter()


    def tirer(self):
          if self.touche.get(pygame.K_g):
            self.personnage.shoot()

    def ennemie(self):
        ennemie = Ennemie()

