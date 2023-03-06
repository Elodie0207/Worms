import pygame

from Jeu import Jeu
from Map import Map
from terrain import Terrain
import time
import threading



def menu():
    pygame.init()
    screen = pygame.display.set_mode((1080, 700))
    pygame.display.set_caption("Menu")

    background = pygame.image.load("Image/bgMenu.jpg").convert()

    font = pygame.font.SysFont('Consolas', 30)

    play = pygame.Rect(450, 100, 200, 50)
    quit = pygame.Rect(450, 200, 200, 50)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.collidepoint(event.pos):
                    main()

                if quit.collidepoint(event.pos):
                    pygame.quit()
                    quit()


        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, (0, 0, 0), play)
        pygame.draw.rect(screen, (0, 0, 0), quit)

        JouerTexte = font.render("Jouer", True, (255, 255, 255))
        QuitterTexte = font.render("Quitter", True, (255, 255, 255))

        screen.blit(JouerTexte, (play.x + 60, play.y + 10))
        screen.blit(QuitterTexte, (quit.x + 40, quit.y + 10))

        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 700))
    pygame.display.set_caption("Worms")

    background = pygame.image.load("Image/ciel.jpg").convert()
    Partie = Jeu(screen)
    montre = pygame.time.Clock()
    run = True
    # Partie.vie()
    temps, texte = 15, '15'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    Partie.playerEtat = True
    terrain = Terrain(screen)
    player = None
    Partie.collide()
    Partie.ennemie.vie()
    sleep = False
    fin=False

    while run:
        # fenêtre du jeu
        montre.tick(60)
        screen.blit(background, (0, -100))
        # fenêtre des perso
        screen.blit(Partie.personnage.perso, Partie.personnage.rect)
        screen.blit(Partie.ennemie.perso, Partie.ennemie.rect)
        terrain.run()

        #print(Partie.ennemie.life)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                Partie.touche[event.key] = True

            elif event.type == pygame.KEYUP:
                Partie.touche[event.key] = False
            if event.type == pygame.USEREVENT:
                if temps > 0:
                    temps -= 1
                    texte = str(temps).rjust(3)
                else:
                    if Partie.playerEtat == False:
                        temps, texte = 15, '15'.rjust(3)

                        Partie.playerEtat = True
                        player = "Joueur1"
                    else:
                        temps, texte = 15, '15'.rjust(3)

                        Partie.playerEtat = False
                        player = "Joueur2"






        if Partie.playerEtat == True and sleep == False:
            Partie.bougerPlayer(screen)
        elif Partie.playerEtat == False and sleep == False:
            Partie.bougerPlayerBis(screen)

        if (Partie.ennemie.life <= 0 or Partie.personnage.life <= 0):
            Partie.victoire(screen, player)
            menu()
        screen.blit(font.render(texte, True, (0, 0, 0)), (32, 48))
        pygame.draw.rect(screen, (0, 255, 0), (Partie.personnage.rect.x, Partie.personnage.rect.y - 10,
                                               Partie.personnage.life / Partie.personnage.vieMax * Partie.personnage.rect.width,
                                               5))
        pygame.draw.rect(screen, (0, 255, 0), (Partie.ennemie.rect.x, Partie.ennemie.rect.y - 10,
                                               Partie.ennemie.life / Partie.ennemie.vieMax * Partie.ennemie.rect.width,
                                               5))
        if Partie.personnage.rect.bottom >= screen.get_height():
            Partie.personnage.rect.bottom = 700
        pygame.display.update()
    if fin is True:
        run=False
    pygame.quit()
    quit()

if __name__ == "__main__":
    menu()
