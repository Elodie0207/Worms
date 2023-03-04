import pygame

from Personnage import Personnage
from Ennemie import Ennemie
from Armes import Armes

from terrain import Terrain


class Jeu:
    def __init__(self,screen):
        self.personnage = Personnage()
        self.armes=Armes(1080,700)
        self.touche = {}
        self.temps=60
        self.viser=True
        self.tirer=False
        self.ennemie= Ennemie()
        terrain=Terrain(screen)
        self.spriteTerrain=terrain.tuiles()
    #Creation de sprites
        self.all_sprites=pygame.sprite.Group()
        self.all_sprites.add(self.personnage)
        self.all_sprites.add(self.ennemie)
        self.all_sprites.add(self.spriteTerrain)
        self.collisions=False

#Collisions entre les personnages et la map
    def collide(self):
        if pygame.sprite.spritecollide(self.personnage, self.spriteTerrain, False):
            print("collide")
            for objet in pygame.sprite.spritecollide(self.personnage, self.spriteTerrain, False):
                if self.personnage.rect.bottom > objet.rect.top or self.personnage.rect.top > objet.rect.bottom :
                        self.personnage.rect.bottom = objet.rect.top+1 #ajout de +1 pour effacer le vide entre le personnage et la plateforme

                else:
                    self.collisions = False
        else:
            self.collisions = False
            self.personnage.rect.y+=5



        if pygame.sprite.spritecollide(self.ennemie, self.spriteTerrain, False):
            for objet in pygame.sprite.spritecollide(self.ennemie, self.spriteTerrain, False):
                if self.ennemie.rect.bottom > objet.rect.top:
                    self.ennemie.rect.bottom = objet.rect.top+1
                else:
                    self.collisions = False
        else:
            self.collisions = False
            self.ennemie.rect.y+=5

        if pygame.sprite.collide_rect(self.personnage, self.ennemie):
            if self.personnage.rect.right > self.ennemie.rect.left and self.personnage.deplacement == "droite":
                self.personnage.rect.right = self.ennemie.rect.left
            elif self.personnage.rect.left < self.ennemie.rect.right and self.personnage.deplacement == "gauche":
                self.personnage.rect.left = self.ennemie.rect.right
            if self.personnage.rect.bottom > self.ennemie.rect.top and self.personnage.deplacement == "bas":
                self.personnage.rect.bottom = self.ennemie.rect.top
            elif self.personnage.rect.top < self.ennemie.rect.bottom and self.personnage.deplacement == "haut":
                self.personnage.rect.top = self.ennemie.rect.bottom
            else:
                self.collisions = False
        else:
            self.collisions = False


#Fonction qui permet de bouger le personnage de Gauche
    def bougerPlayer(self,screen):
        self.collide()
        if self.touche.get(pygame.K_d) and self.personnage.rect.x + self.personnage.rect.width < 1080  and self.collisions==False:
            self.personnage.bouger_droite()

        elif self.touche.get(pygame.K_q) and self.personnage.rect.x > 0  and  self.collisions==False:
            self.personnage.bouger_gauche()

        elif self.touche.get(pygame.K_SPACE) and self.personnage.saut is False and  self.collisions==False:
            self.personnage.saut = True
            self.personnage.nbJump = self.personnage.nbJumpMax

        if self.personnage.saut is True and  self.collisions==False:
            self.personnage.sauter()

        if self.touche.get(pygame.K_g):
                self.personnage.draw(screen)
                if self.touche.get(pygame.K_RETURN):
                    self.personnage.update()

         #gérer la collisions



#Fonction qui permet de bouger le personnage de Droite
    def bougerPlayerBis(self,screen):
        self.collide()
        if self.touche.get(pygame.K_d) and self.ennemie.rect.x + self.ennemie.rect.width < 1080  and self.collisions==False:
            self.ennemie.bouger_droite()

        elif self.touche.get(pygame.K_q) and self.ennemie.rect.x > 0  and  self.collisions==False:
            self.ennemie.bouger_gauche()

        elif self.touche.get(pygame.K_SPACE) and self.ennemie.saut is False and  self.collisions==False:
            self.ennemie.saut = True
            self.ennemie.nbJump = self.ennemie.nbJumpMax

        if self.ennemie.saut is True and  self.collisions==False:
            self.ennemie.sauter()

        if self.touche.get(pygame.K_g):
                self.ennemie.draw(screen)
                if self.touche.get(pygame.K_RETURN):
                    self.ennemie.update()

         #gérer la collisions


    def vie(self):
        self.ennemie.vies()










