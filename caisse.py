# -*- coding: cp1252 -*-
import pygame
import couleur
import scenario

T_GRILLE=30

def init(l,c):
    
    '''Fonction qui permet de définir les attributs permettant de calculer
       la position de la caisse avec un système de ligne/colonne.
       Des attributs de vitesse sont utilisées permettant l'actualisation des
       caisses et leurs déplacements'''
    
    caisse={}
    caisse["pos_l"]=l
    caisse["pos_c"]=c
    caisse["vit_l"]=0
    caisse["vit_c"]=0
    return caisse

def dessine_caisse(surface,att):
    '''
    Fonction qui dessine sur pygame un carré représentant une caisse
    Argument: surface= zone de dessin sur pygame
              l= int- numéro de la ligne ou déssiner le carré
              c= int- numéro de la colonne ou déssiner le carré        
    '''

    cibles=pygame.image.load("caisses.png")
    surface.blit(cibles,[att['pos_l']*T_GRILLE+350,att['pos_c']*T_GRILLE+250])


def update(l_caisses):
    for a in range (len (l_caisses)):
        l_caisses[a]['pos_l']+=l_caisses[a]['vit_l']
        l_caisses[a]['pos_c']+=l_caisses[a]['vit_c']
        l_caisses[a]['vit_l']=0
        l_caisses[a]['vit_c']=0




    

