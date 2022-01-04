# -*- coding: cp1252 -*-
#=====================================
#File: scenario.py
#Date:  29/11/17
#Autor: CODRON JULIEN, NEMPONT JEROME
#Projet Fin semestre 1, SOKOBAN
#=====================================

import pygame
import couleur
import avatar
import caisse

#— # : mur
#— $ : caisse
#— . : destination
#— @ : personnage


NIVEAU0= ["nnnnnnnnnnnnn",
          "nnnnnnnnnnnnn",
          "nnnnnn#######",
          "nnnnnn#@$  .#",
          "nnnnnn#######"]

NIVEAU1= ["nnnn#####nnnnnnnnnn",
          "nnnn#   #nnnnnnnnnn",
          "nnnn#$  #nnnnnnnnnn",
          "nn###  $##nnnnnnnnn",
          "nn#  $ $ #nnnnnnnnn",
          "### # ## #SSS######",
          "#   # ## #####  ..#",
          "# $ $           ..#",
          "##### ### #@##  ..#",
          "nnnn#     #########",
          "nnnn#######nnnnnnnn"]

NIVEAU2= ["nnnnnn#######",
          "nnnnnn#. # .#",
          "nnnnnn# $ $ #",
          "nnnnnn# #@  #",
          "nnnnnn# $ $ #",
          "nnnnnn#. # .#",
          "nnnnnn#######"]

NIVEAU3= ["nnnnnn########n",
          "nnnnnn#   # .#n",
          "nnnnnn#      ##",
          "nnnnnn## ##$ .#",
          "nnnnnn## #.@$##",
          "nnnnnn## ##$ ##",
          "nnnnnn#     ###",
          "nnnnnn#   # #nn",
          "nnnnnn#######nn"]

NIVEAU4= ["nnnnnn###n###nn",
          "nnnnnn#.### ##n",
          "nnnn###.     ##",
          "nnnn#   # #   #",
          "nnnn## # $   ##",
          "nnnn#  #$ $#  #",
          "nnnn#    $ #  #",
          "nnnn#  ### # ##",
          "nnnn#    @  ..#",
          "nnnn### ### ##n",
          "nnnnnn###n###nn"]


GRILLE=[NIVEAU0,NIVEAU1,NIVEAU2,NIVEAU3,NIVEAU4]
T_GRILLE = 30



def init(num):
    '''
    Cette fonction permet d'initialisé le niveau choisi
    Argument: num= int- le niveau choisi, compri dans la liste GRILLE
    Return:  att= dictionnaires Comprends 4 attribut du niveau:
                -joueur,caisses,grille(position des murs),grille2(position cible)
    '''

    lvl=GRILLE[num]

    att={}
    att["caisses"]=[]
    att["grille"]=[]
    att["grille2"]=[]
    att["avatar"]=[]
    att["sol"]=[]
    liste_caisses=[]
    
    for i in range (len(lvl)):
        for j in range (len(lvl[i])):
            if lvl[i][j]=="#":
                att["grille"]+=[(i,j)]

            if lvl[i][j]==".":
                att["grille2"]+=[(i,j)]

            if lvl[i][j]==" " or lvl[i][j]=="@" or lvl[i][j]=="$":
                att["sol"]+=[(i,j)]

            if lvl[i][j]=="$":
                ca=caisse.init(j,i)
                liste_caisses+=[ca]
                att["caisses"]=liste_caisses

            if lvl[i][j]=="@":
                att["avatar"]+=[(i,j)]
    
    att["joueur"]=avatar.init(att["avatar"][0][1],att["avatar"][0][0],2,att)
    
    return att


def dessine_mur(surface,l,c):
    '''
    Fonction qui dessine sur pygame un carré de représentant un murs
    Argument: surface= zone de dessin sur pygame
              l= int- numéro de la ligne ou déssiner le carré
              c= int- numéro de la colonne ou déssiner le carré        
    '''
    
    murs=pygame.image.load("murs.png")
    surface.blit(murs,[l*T_GRILLE+350,c*T_GRILLE+250])

def dessine_cible(surface,l,c):
    '''
    Fonction qui dessine sur pygame un carré de représentant une cible
    Argument: surface= zone de dessin sur pygame
              l= int- numéro de la ligne ou déssiner le carré
              c= int- numéro de la colonne ou déssiner le carré        
    '''
    cibles=pygame.image.load("cibles.png")
    surface.blit(cibles,[l*T_GRILLE+350,c*T_GRILLE+250])

def dessine_sol(surface,l,c):
    '''
    Fonction qui dessine sur pygame des carré de représentant le sol
    Argument: surface= zone de dessin sur pygame
              l= int- numéro de la ligne ou déssiner le carré
              c= int- numéro de la colonne ou déssiner le carré        
    ''' 
    pygame.draw.rect(surface,couleur.GRIS,[l*T_GRILLE+350,c*T_GRILLE+250,T_GRILLE,T_GRILLE])

def dessine(att,surface):
    '''
    Fonction qui dessine sur pygame les murs et les cibles du niveau.
    Argument: surface= zone de dessin sur pygame
              att= dictionnaire- comprends les attributs du niveau        
    '''
    
    surface.fill((couleur.NOIR))
    Fond=pygame.image.load_basic("Fond_Game.bmp")
    surface.blit(Fond,[0,0])
    for h in range (0,len(att['sol'])):
         dessine_sol(surface,(att["sol"][h][1]),(att["sol"][h][0]))
    for i in range (0,len(att['grille'])):
         dessine_mur(surface,(att["grille"][i][1]),(att["grille"][i][0]))
    for j in range (0,len(att['grille2'])):
         dessine_cible(surface,(att["grille2"][j][1]),(att["grille2"][j][0]))
    for l in range (0,len(att["caisses"])):
         caisse.dessine_caisse(surface,(att["caisses"][l]))
    avatar.dessine(surface,att["joueur"])

def caisses_sur_cibles(att):
    win=0
    for c in range (len(att["grille2"])):
        for b in range (len(att["caisses"])):
            if (att["caisses"][b]['pos_c'],att["caisses"][b]['pos_l'])== att["grille2"][c]:
                win+=1            
    if win==len(att["grille2"]):
        return True


def execute(att,niveau):
    '''
    Fonction qui execute l'enssemble des fonction précédente permetant de
    déssiné le niveau, et qui permet également de configurer des touches sur
    pygame.
    Argument: att= dictionnaire- comprends les attributs du niveau 
    '''
    clock=pygame.time.Clock()
    mouv=0
    terminer=False
    while not terminer:
        for event in pygame.event.get():
            if event.type== pygame.QUIT :
                return 0 
                terminer=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 0 
                    terminer=True
                if event.key==pygame.K_r:
                    return 1 
                if event.key==pygame.K_RETURN:
                    
                    if niveau+1==len(GRILLE):
                        return 3
                    else:
                        return 2
                if event.key==pygame.K_LEFT:
                    att["joueur"]["vit_l"]=-1
                    att["joueur"]["vit_c"]=0
                    att["joueur"]["direc"]=0
                    mouv+=1
                    
                    
                if event.key==pygame.K_RIGHT:
                    att["joueur"]["vit_l"]=1
                    att["joueur"]["vit_c"]=0
                    att["joueur"]["direc"]=2
                    mouv+=1
                    
                if event.key==pygame.K_UP:
                    att["joueur"]["vit_l"]=0
                    att["joueur"]["vit_c"]=-1
                    att["joueur"]["direc"]=3
                    mouv+=1
                    
                if event.key==pygame.K_DOWN:
                    att["joueur"]["vit_l"]=0
                    att["joueur"]["vit_c"]=1
                    att["joueur"]["direc"]=1
                    mouv+=1 
                                                      
        surface= pygame.display.set_mode((1280,720))           
        surface.fill((couleur.NOIR))
        clock.tick(150)
        
        if caisses_sur_cibles(att)==True:
            if niveau+1==len(GRILLE):
                return 3
            
            else:
                clock.tick(2)
                surface.fill((couleur.NOIR))
                titre_police=pygame.font.Font("Augusta.ttf",100)
                titre1=titre_police.render("Loading...",True, couleur.GRIS)
                surface.blit(titre1,[420,255])
                titre2=titre_police.render("Loading...",True, couleur.BLANC)
                surface.blit(titre2,[414,260])
                pygame.display.update()
                clock.tick(0.4)
                return 2
        
        else:
            
            avatar.update(att["joueur"]) 
            caisse.update(att["caisses"])
            dessine(att,surface)
            
        #Compteur de mouvement
            
        mouvement_police=pygame.font.Font("Augusta.ttf",50)
        mouvement1=mouvement_police.render("Mouvements:"+str(mouv),True, couleur.BLANC)
        mouvement2=mouvement_police.render("Mouvements:"+str(mouv),True, couleur.NOIR)
        surface.blit(mouvement2,[495,602])
        surface.blit(mouvement1,[490,600])
        
        pygame.display.update()

    


        

        
              
        

            
         
        
    

    

    
    
    
    
