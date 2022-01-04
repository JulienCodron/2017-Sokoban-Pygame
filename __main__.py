#=====================================
#File: __main__.py
#Date:  29/11/17
#Autor: CODRON JULIEN, NEMPONT JEROME
#Projet Fin semestre 1, SOKOBAN
#=====================================

import pygame
from pygame.locals import *
import scenario
import ouverture
import couleur

def main():
    
    '''La fonction main est la fonction principale du programme.
      -Initialisation de pygame
      -Initialisation de la clock
      -Initialisation de la surface
      -Ajout d'un nom
      -Remise à zéro de la surface en blanc
      -Ouverture du module ouverture permettant l'affichage de
      l'accueil du jeu.
      -SI le joueur ne souhaite pas continuer:
          alors il lui suffit de cliquer sur la croix pour quitter
       SINON:
          Initialisation du module scenario avec la mise en place du
          niveau 0.
      -Tant que terminer==False:
          -Initialisation du module scénario permettant la lecture du
          premier niveau.
          -Actualisation du programme
          - Choix de l'utilisateur:
              -Si le joueur appuie sur échap ou quitter le jeu quitte
              -Si le joueur appuie sur entrée, passage au niveau suivant          
    '''
    essais=0
    pygame.init()
    clock= pygame.time.Clock()
    surface= pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Sokoban")
    pygame.mixer.music.load('Jerome_Song.wav')
    pygame.mixer.music.play(-1)
    surface.fill(couleur.BLANC)   
    continuer=ouverture.execut(surface)
    terminer=False
    if not continuer:
        pygame.quit()
        terminer=True
    elif continuer==True:
        niveau=0
        while not terminer:
            att=scenario.init(niveau)
            execute=scenario.execute(att,niveau)
            if execute==0:
                pygame.quit()
                terminer=True
            elif execute==1:
                att=scenario.init(niveau)
                pygame.display.update()  
            elif execute==2:
                niveau+=1
            elif execute==3:
                clock.tick(2)
                surface.fill((couleur.NOIR))
                titre_police=pygame.font.Font("Augusta.ttf",100)
                titre1=titre_police.render("Bravo Vous avez fini le jeu!",True, couleur.GRIS)
                surface.blit(titre1,[130,255])
                titre2=titre_police.render("Bravo Vous avez fini le jeu!",True, couleur.BLANC)
                surface.blit(titre2,[124,260])
                pygame.display.update()
                clock.tick(0.4)
                pygame.quit()
                terminer=True       


main()
    


    
    
    
