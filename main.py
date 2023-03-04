import pygame

from Jeu import Jeu
from Map import Map
from terrain import Terrain

def main():
    pygame.init()
    screen=pygame.display.set_mode((1080,700))
    pygame.display.set_caption("Worms")

    background=pygame.image.load("Image/ciel.jpg").convert()
    Partie=Jeu(screen)
    montre=pygame.time.Clock()
    run=True
    Partie.vie()
    temps,texte=60,'60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    player=True
    terrain=Terrain(screen)
    Partie.collide()
    while run:
        #fenêtre du jeu
        montre.tick(60)
        screen.blit(background,(0,-100))
        #fenêtre des perso
        screen.blit(Partie.personnage.image, Partie.personnage.rect)
        screen.blit(Partie.ennemie.image, Partie.ennemie.rect)
        terrain.run()


        print(Partie.personnage.rect.x)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.KEYDOWN:
                Partie.touche[event.key]= True

            elif event.type==pygame.KEYUP:
                Partie.touche[event.key]=False
            if event.type==pygame.USEREVENT:
                if temps >0:
                    temps -=1
                    texte = str(temps).rjust(3)
                else:
                    if player==False:
                        temps,texte=60,'60'.rjust(3)
                        player=True
                    else:
                        temps,texte=60,'60'.rjust(3)
                        player=False


        if player==True:
            Partie.bougerPlayer(screen)
        else:
            Partie.bougerPlayerBis(screen)



        screen.blit(font.render(texte, True, (0, 0, 0)), (32, 48))
        pygame.draw.rect(screen, (0,255,0), (Partie.personnage.rect.x, Partie.personnage.rect.y - 10, Partie.personnage.vie / Partie.personnage.vieMax * Partie.personnage.rect.width, 5))
        pygame.draw.rect(screen, (0,255,0), (Partie.ennemie.rect.x, Partie.ennemie.rect.y - 10, Partie.ennemie.vie / Partie.ennemie.vieMax * Partie.ennemie.rect.width, 5))
        if Partie.personnage.rect.bottom>=screen.get_height():
            Partie.personnage.rect.bottom=700
        pygame.display.update()





    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
