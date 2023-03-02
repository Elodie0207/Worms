import pygame

from Jeu import Jeu
from Map import Map


def main():
    pygame.init()
    screen=pygame.display.set_mode((1080,700))
    pygame.display.set_caption("Worms")
    background=pygame.image.load("Image/111130142640_50.jpg").convert()
    Partie=Jeu()
    montre=pygame.time.Clock()
    run=True
    blanc=(255,255,255)
    noir=(0,0,0)
    cube_size=10
    cube_rect=pygame.Rect(0,0,cube_size,cube_size)
    Partie.vie()
    temps,texte=60,'60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    player=True
    while run:
        #fenêtre du jeu
        montre.tick(60)
        screen.blit(background,(0,-100))
        #fenêtre du perso
        screen.blit(Partie.personnage.perso,Partie.personnage.getRect)
        screen.blit(Partie.ennemie.perso,Partie.ennemie.getRect)



        print(Partie.ennemie.vie)

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

        #wallList.draw(screen)
        screen.blit(font.render(texte, True, (0, 0, 0)), (32, 48))
        pygame.draw.rect(screen,(0,255,0),(Partie.personnage.getRect.x,Partie.personnage.getRect.y-10,Partie.personnage.vie/Partie.personnage.vieMax*Partie.personnage.getRect.width,5))
        pygame.draw.rect(screen,(0,255,0),(Partie.ennemie.getRect.x,Partie.ennemie.getRect.y-10,Partie.ennemie.vie/Partie.ennemie.vieMax*Partie.ennemie.getRect.width,5))
        if Partie.personnage.getRect.bottom>=screen.get_height():
            Partie.personnage.getRect.bottom=700
        pygame.display.update()





    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
