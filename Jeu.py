import pygame


from Personnage import Personnage
from Ennemie import Ennemie

from Grenade import Grenade

from terrain import Terrain


class Jeu:
    def __init__(self,screen):
        self.personnage = Personnage()
        self.grenade = Grenade(0,0,0)
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
        self.all_sprites.add(self.grenade)
        self.all_sprites.add(self.spriteTerrain)
        self.collisions=False
        self.playerEtat=False

#Collisions entre les personnages et la map
    def collide(self):
        if pygame.sprite.spritecollide(self.personnage, self.spriteTerrain, False):
            self.personnage.parachute = False
            for objet in pygame.sprite.spritecollide(self.personnage, self.spriteTerrain, False):
                if self.personnage.rect.bottom > objet.rect.top or self.personnage.rect.top > objet.rect.bottom :
                        self.personnage.rect.bottom = objet.rect.top+1 #ajout de +1 pour effacer le vide entre le personnage et la plateforme

                else:
                    self.collisions = False
        else:
            self.collisions = False
            if self.personnage.parachute is True : # Si le personnage tombe d'une plateforme en parachute, fais varier la gravité
                self.personnage.rect.y += 5

            elif self.personnage.saut is not True  : # Si le personnage tombe d'une plateforme sans sauter, je lui met une gravité de 20 pour qu'il redescende rapidement
                self.personnage.rect.y += 20

            elif  self.ennemie.parachute is True:
                self.ennemie.rect.y += 5
            elif self.ennemie.parachute is not True:
                self.ennemie.rect.y += 20



        if pygame.sprite.spritecollide(self.ennemie, self.spriteTerrain, False):
            self.ennemie.parachute = False
            for objet in pygame.sprite.spritecollide(self.ennemie, self.spriteTerrain, False):
                if self.ennemie.rect.bottom > objet.rect.top:
                    self.ennemie.rect.bottom = objet.rect.top+1
                else:
                    self.collisions = False
        else:
            self.collisions = False
            self.ennemie.rect.y+=5

        if pygame.sprite.collide_rect(self.personnage, self.ennemie):
            if self.personnage.rect.right > self.ennemie.rect.left: #and self.personnage.deplacement == "droite":
                self.personnage.rect.right = self.ennemie.rect.left
            elif self.personnage.rect.left < self.ennemie.rect.right: #and self.personnage.deplacement == "gauche":
                self.personnage.rect.left = self.ennemie.rect.right

            else:
                self.collisions = False
        else:
            self.collisions = False


        if pygame.sprite.collide_rect(self.grenade, self.ennemie):
            if self.playerEtat==True:
                self.ennemie.life-=10

        if pygame.sprite.collide_rect(self.grenade, self.personnage):
            if self.playerEtat==False:
                self.personnage.life-=10

        if pygame.sprite.spritecollide(self.grenade, self.spriteTerrain, False):
            for objet in pygame.sprite.spritecollide(self.grenade, self.spriteTerrain, False):
               if self.grenade.rect.bottom > objet.rect.top or self.grenade.rect.top > objet.rect.bottom :
                        self.grenade.rect.bottom=450


        else:
            self.collisions = False


#Fonction qui permet de bouger le personnage de Gauche
    def bougerPlayer(self,screen):
        self.collide()
        player_pos = (self.personnage.rect.x, self.personnage.rect.y)

        if self.touche.get(pygame.K_d) and self.personnage.rect.x + self.personnage.rect.width < 1080 and self.collisions is False:
            self.personnage.bouger_droite()
        elif self.touche.get(pygame.K_q) and self.personnage.rect.x > 0 and self.collisions is False:
            self.personnage.bouger_gauche()

        if self.touche.get(pygame.K_z) and self.personnage.saut is False and self.collisions is False:
            self.personnage.saut = True
            self.personnage.nbJump = self.personnage.nbJumpMax

        if self.personnage.saut is True and self.collisions is False:
            self.personnage.sauter()

        if self.touche.get(pygame.K_UP):
            self.grenade.adjust_angle("up")
        elif self.touche.get(pygame.K_DOWN):
            self.grenade.adjust_angle("down")

        if self.touche.get(pygame.K_g) and self.grenade.flag is False:
            self.grenade = Grenade(0,0,0)
            self.grenade.flag = True


        if self.grenade.flag is True and self.grenade.usable is True:
            self.grenade.placement(player_pos)
            self.grenade.trajectoire(screen, self.personnage.is_facing_left)
            self.grenade.draw(screen)
            if self.touche.get(pygame.K_SPACE):
                self.grenade.charging = True
                self.grenade.power += 1
                print("throwing power = ", self.grenade.power)
            else:
                self.grenade.charging = False

        if self.grenade.charging is False and self.grenade.power > 0 and self.grenade.thrown is False:
            self.grenade.charging = False
            self.grenade.thrown = True
            self.grenade.flag = False
            self.grenade.usable = False
            self.grenade.lancer(self.personnage.is_facing_left)
            self.grenade.power = 0
            print("throw")

        if self.grenade.thrown is True:
            self.grenade.draw(screen)
            self.grenade.update()

        if self.touche.get(pygame.K_p) and self.collisions is False: # Activer le parachute
            self.personnage.parachute = True
            print("Parachute activé")


         #gérer la collisions



#Fonction qui permet de bouger le personnage de Droite
    def bougerPlayerBis(self,screen):
        self.collide()
        player_pos = (self.ennemie.rect.x, self.ennemie.rect.y)

        if self.touche.get(pygame.K_d) and self.ennemie.rect.x + self.ennemie.rect.width < 1080 and self.collisions is False:
            self.ennemie.bouger_droite()
        elif self.touche.get(pygame.K_q) and self.ennemie.rect.x > 0 and self.collisions is False:
            self.ennemie.bouger_gauche()

        if self.touche.get(pygame.K_z) and self.ennemie.saut is False and self.collisions is False:
            self.ennemie.saut = True
            self.ennemie.nbJump = self.ennemie.nbJumpMax

        if self.ennemie.saut is True and self.collisions is False:
            self.ennemie.sauter()

        if self.touche.get(pygame.K_UP):
            self.grenade.adjust_angle("up")
        elif self.touche.get(pygame.K_DOWN):
            self.grenade.adjust_angle("down")

        if self.touche.get(pygame.K_g) and self.grenade.flag is False:
            self.grenade = Grenade(0, 0, 0)
            self.grenade.flag = True

        if self.grenade.flag is True and self.grenade.usable is True:
            self.grenade.placement(player_pos)
            self.grenade.trajectoire(screen, self.ennemie.is_facing_left)
            self.grenade.draw(screen)
            if self.touche.get(pygame.K_SPACE):
                self.grenade.charging = True
                self.grenade.power += 1
                print("throwing power = ", self.grenade.power)
            else:
                self.grenade.charging = False

        if self.grenade.charging is False and self.grenade.power > 0 and self.grenade.thrown is False:
            self.grenade.charging = False
            self.grenade.thrown = True
            self.grenade.flag = False
            self.grenade.usable = False
            self.grenade.lancer(self.ennemie.is_facing_left)
            self.grenade.power = 0
            print("throw")

        if self.grenade.thrown is True:
            self.grenade.draw(screen)
            self.grenade.update()

        if self.touche.get(pygame.K_p) and self.collisions is False: # Activer le parachute
            self.ennemie.parachute = True
            print("Parachute activé")

         #gérer la collisions


    def victoire(self,screen,player):
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Gagnant {player}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(500, 100))
        screen.blit(text, text_rect)










