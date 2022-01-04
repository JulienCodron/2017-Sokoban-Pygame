# -*- coding: cp1252 -*-
#=====================================
#File:  couleur.py
#Date:  29/11/17
#Autor: CODRON JULIEN, NEMPONT JEROME
#Projet Fin semestre 1, SOKOBAN
#=====================================

import pygame
import couleur
import scenario

T_GRILLE = 30

def init(l,c,d,att):
    """
    initialise le personnage
    Argument: l-int position x de l'avatar
              c-int position y de l'avatar
              d-int direction ou regarde l'avatar
              (0= haut, 1 = droite, 2 = bas et 3 = gauche)
    return:
    """

    avatar={}
    avatar['pos_l']=l
    avatar['pos_c']=c 
    avatar['direc']=1
    avatar['vit_l']=0
    avatar['vit_c']=0
    avatar['img']=[]
    avatar['att']=att

    return avatar

def dessine(surface,att):
    """
    dessine l'avatar du personnage dans pygame
    Argument: surface= zone de dessin sur pygame
              att=liste- liste qui comprends un dictionnaire avec les information sur l'avatar
    """

    
    pers=pygame.image.load("perso.png")
    surface.blit(pers,[att['pos_l']*T_GRILLE+350,att['pos_c']*T_GRILLE+250])
    

    
def update(att):
    """
    fonction qui met a joueur l'avatar et les caisse quand il les pousses, quand le joueur ce déplace
    Argument: att-liste=liste de dictionnaire qui comprends les information sur l'avatar du joueur et les caisses du niveau
    """

    
    pfla=att['pos_l']+att['vit_l']        
    pfca=att['pos_c']+att['vit_c']
   
    
    for o in range (len(att["att"]["caisses"])):
        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==1:
            pflc=att["att"]["caisses"][o]['pos_l']
            pfcc=att["att"]["caisses"][o]['pos_c']+1
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_c']+=1
            else:
                att['pos_c']-=1
            #('bas')
            
        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==3:
            pflc=att["att"]["caisses"][o]['pos_l']
            pfcc=att["att"]["caisses"][o]['pos_c']-1
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_c']-=1
            else:
                att['pos_c']+=1
            #('up')
            
        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==2:
            pflc=att["att"]["caisses"][o]['pos_l']+1
            pfcc=att["att"]["caisses"][o]['pos_c']
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_l']+=1
            else:
                att['pos_l']-=1
            #('droite')
                
        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==0:
            pflc=att["att"]["caisses"][o]['pos_l']-1
            pfcc=att["att"]["caisses"][o]['pos_c']
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_l']-=1
            else:
                att['pos_l']+=1
            #('gauche')

           


    

    if est_sur_mur(pfla,pfca,att)==False:
        att['pos_l']+=att['vit_l'] 
        att['pos_c']+=att['vit_c']
        

    
    att['vit_l']=0
    att['vit_c']=0
    

def est_sur_mur(lig,col,att):
    """
    fonction qui retourne vrai s’il y a un mur en position (lig,col) dans scen
    Argument:lig-int: ligne ou ce trouve un mur
             col-int: collonne ou ce trouve un mur
             att- liste=liste de dictionnaire qui comprends toute les information du jeux
    Return: True si il y a un mur à cette coordonnée
    """
    for y in range (len(att["att"]["grille"])):
        if (col,lig)==att["att"]["grille"][y]:
            return True
    return False

def est_sur_caisse(lig,col,att):
    """
    fonction qui retourne vrai s’il y a une caisse en position (lig,col) dans scen
    Argument:lig-int: ligne ou ce trouve une caisse
             col-int: collonne ou ce trouve une caisse
             att- liste=liste de dictionnaire qui comprends toute les information du jeux
    Return: True si il y a un mur à cette coordonnée
    """
    for z in range (len(att["att"]["caisses"])):
        a=(att["att"]["caisses"][z]["pos_l"],att["att"]["caisses"][z]["pos_c"])
        if (lig,col)==a:
            return True
    return False

        

    
    


    



     
    


    
