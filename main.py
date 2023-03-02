import args as args
import pygame
import csv,os
from Jeu import Jeu
from Map import Map

from Personnage import Personnage


def main():
    pygame.init()
    screen=pygame.display.set_mode((1080,700))
    pygame.display.set_caption("Worms")
    background=pygame.image.load("Image/111130142640_50.jpg").convert()
    Partie=Jeu()
    montre=pygame.time.Clock()
    run=True
    Partie.ennemie()
    blanc=(255,255,255)
    noir=(0,0,0)
    cube_size=10
    cube_rect=pygame.Rect(0,0,cube_size,cube_size)

    while run:
        #fenêtre du jeu
        montre.tick(60)
        screen.blit(background,(0,-100))
        #fenêtre du perso
        screen.blit(Partie.personnage.perso,Partie.personnage.getRect)
        Partie.bouger()
        print(Partie.personnage.getRect.y)

        wallList=pygame.sprite.Group()
        block1= Map(40,500,50,60)
        wallList.add(block1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.KEYDOWN:
                Partie.touche[event.key]= True
            elif event.type==pygame.KEYUP:
                Partie.touche[event.key]=False


        #wallList.draw(screen)
        pygame.draw.rect(screen,(0,255,0),(Partie.personnage.getRect.x,Partie.personnage.getRect.y-10,Partie.personnage.vie/Partie.personnage.vieMax*Partie.personnage.getRect.width,5))
        if Partie.personnage.getRect.bottom>=screen.get_height():
            Partie.personnage.getRect.bottom=700
        pygame.display.update()










    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
