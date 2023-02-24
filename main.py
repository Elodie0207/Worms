import args as args
import pygame

from Jeu import Jeu
from Personnage import Personnage


def main():
    pygame.init()
    screen=pygame.display.set_mode((1080,700))
    pygame.display.set_caption("Worms")
    background=pygame.image.load("Image/NaUX7.png").convert()
    Partie=Jeu()
    run=True
    while run:
        #fenêtre du jeu
        screen.blit(background,(0,-100))
        #fenêtre du perso
        screen.blit(Partie.personnage.perso,Partie.personnage.getRect)
        Partie.bouger()
        print(Partie.personnage.vitesse)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.KEYDOWN:
                Partie.touche[event.key]= True
            elif event.type==pygame.KEYUP:
                Partie.touche[event.key]=False

        pygame.display.update()

    vitesse=10













    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
