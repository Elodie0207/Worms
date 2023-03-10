import pygame
from Map import Map

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.life = 140
        self.vieMax = 100
        self.vitesse = 10
        self.perso = pygame.image.load("Image/Perso.png")
        self.perso = pygame.transform.flip(self.perso, True, False)
        self.rect = self.perso.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.saut = False
        self.nbJumpMax = 35
        self.nbJump = 0
        self.vitesseChute = 0
        self.block1 = Map(self.rect.x,self.rect.y,50,60)
        self.is_facing_left = False
        self.parachute = False
        self.fin=False
    def draw(self,screen):
        wallList = pygame.sprite.Group()
        wallList.add(self.block1)
        wallList.draw(screen)

    def update(self):
        self.block1.rect.x += 50
        if not pygame.sprite.spritecollide(self, self.spriteTerrain, False):
            self.rect.y += self.vitesseChute
    def bouger_droite(self):
        self.rect.x += self.vitesse
        if self.is_facing_left:
            self.perso = pygame.transform.flip(self.perso, True, False)
            self.is_facing_left = False

    def bouger_gauche(self):
        self.rect.x -= self.vitesse
        if not self.is_facing_left:
            self.perso = pygame.transform.flip(self.perso, True, False)
            self.is_facing_left = True

    def sauter(self):
        if self.saut is True:
            if self.parachute is False:
                self.rect.y -= self.nbJump # nbJump = nbJumpMax au début
                if self.nbJump > -self.nbJumpMax:
                    self.nbJump -= 2.5 # Fais varier la gravité du personnage
                else:
                    self.saut=False

            if self.parachute is True:
                self.rect.y += 0.1 # Fais varier la vitesse de chute en parachute

    def vie(self):
        self.barreVie = pygame.Surface((self.rect.width,5))



