import pygame

from Personnage import Personnage


class Jeu:
    def __init__(self):
        self.personnage=Personnage()
        self.touche= {
        }


    def bouger(self):
        if self.touche.get(pygame.K_d):
            self.personnage.bouger_droite()
        elif self.touche.get(pygame.K_q):
            self.personnage.bouger_gauche()

        elif self.touche.get(pygame.K_SPACE) and self.personnage.saut is False:
            self.personnage.saut=True
            self.personnage.nbJump=self.personnage.nbJumpMax

        if self.personnage.saut is True:
            self.personnage.sauter()
