# -*- coding: cp1252 -*-
import pygame
import couleur
import scenario

T_GRILLE=30

def init(l,c):
    
    '''Fonction qui permet de d�finir les attributs permettant de calculer
       la position de la caisse avec un syst�me de ligne/colonne.
       Des attributs de vitesse sont utilis�es permettant l'actualisation des
       caisses et leurs d�placements'''
    
    caisse={}
    caisse["pos_l"]=l
    caisse["pos_c"]=c
    caisse["vit_l"]=0
    caisse["vit_c"]=0
    return caisse

def dessine_caisse(surface,att):
    '''
    Fonction qui dessine sur pygame un carr� repr�sentant une caisse
    Argument: surface= zone de dessin sur pygame
              l= int- num�ro de la ligne ou d�ssiner le carr�
              c= int- num�ro de la colonne ou d�ssiner le carr�        
    '''

    cibles=pygame.image.load("caisses.png")
    surface.blit(cibles,[att['pos_l']*T_GRILLE+350,att['pos_c']*T_GRILLE+250])


def update(l_caisses):
    for a in range (len (l_caisses)):
        l_caisses[a]['pos_l']+=l_caisses[a]['vit_l']
        l_caisses[a]['pos_c']+=l_caisses[a]['vit_c']
        l_caisses[a]['vit_l']=0
        l_caisses[a]['vit_c']=0




    

