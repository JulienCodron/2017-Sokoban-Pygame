# -*- coding: utf-8 -*-

#=====================================
#File: ouverture.py
#Date:  29/11/17
#Autor: CODRON JULIEN, NEMPONT JEROME
#Projet Fin semestre 1, SOKOBAN
#=====================================

import pygame
import couleur

def execut(surface):
    '''
    Fonction lance le menu du jeu et demande au joueur s'il veut continuer
    Argument: surface - taille de la fenêtre ouverte de pygame ou l'on dessine
    return: continuer- True ou False si le joueur veut continuer ou non
    '''
    terminer=False
    continuer=False
    dessine(surface)
    pygame.display.update()
    while not terminer:
        for event in pygame.event.get():
            if event.type== pygame.QUIT :
                terminer=True
                continuer=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame. K_ESCAPE:
                    terminer=True
                    continuer=False
                if event.key==pygame.K_RETURN:
                    terminer=True
                    continuer=True
    return continuer
    

def dessine(surface):
    '''
    Fonction qui déssine le menu du jeu
    Argument: surface: taille de la fenêtre ouverte sur pygame ou l'on dessine
    '''
    
    #rectangle
    
    pygame.draw.rect(surface,couleur.NOIR,[0,0,1280,100])
    pygame.draw.rect(surface,couleur.NOIR,[0,620,1280,720])
    
    #background
    
    Background=pygame.image.load("Background2.bmp")
    surface.blit(Background, [0,100])
    
    #Personnage
    
    Personnage_Gauche=pygame.image.load("Vivant_Droite.png")
    Personnage_Droite=pygame.image.load("Vivant_Gauche.png")
    surface.blit(Personnage_Gauche,[99,240])
    surface.blit(Personnage_Droite,[1025,240])

    #Titre
    
    titre_police=pygame.font.Font("Augusta.ttf",100)
    titre1=titre_police.render("SOKOBAN",True, couleur.GRIS)
    surface.blit(titre1,[460,-5])
    titre2=titre_police.render("SOKOBAN",True, couleur.BLANC)
    surface.blit(titre2,[454,0])

    #Date

    date_police=pygame.font.Font(None,22)
    date1=date_police.render("29/11/2017",True, couleur.GRIS)
    surface.blit(date1,[10,23])
    date2=date_police.render("29/11/2017",True, couleur.BLANC)
    surface.blit(date2,[8,24])

    #Auteurs

    auteurs_police=pygame.font.Font(None,22)
    auteurs1=auteurs_police.render("Codron Julien & Nempont Jerome",True, couleur.GRIS)
    surface.blit(auteurs1,[10,696])
    auteurs2=auteurs_police.render("Codron Julien & Nempont Jerome",True, couleur.BLANC)
    surface.blit(auteurs2,[8,697])

    #Discipline

    discipline_police=pygame.font.Font(None,22)
    discipline1=discipline_police.render("Algorithme & programmation 1",True, couleur.GRIS)
    surface.blit(discipline1,[11,678])
    discipline2=discipline_police.render("Algorithme & programmation 1",True, couleur.BLANC)
    surface.blit(discipline2,[9,679])

    #Insitution

    institution_police=pygame.font.Font(None,22)
    institution1=institution_police.render("Universite d'Artois",True, couleur.GRIS)
    surface.blit(institution1,[10,6])
    institution2=institution_police.render("Universite d'Artois",True, couleur.BLANC)
    surface.blit(institution2,[8,7])

    #Instruction

    instruction_police=pygame.font.Font("Augusta.ttf",50)
    instruction1=instruction_police.render("Appuyez sur ENTRER pour commencer",True, couleur.GRIS)
    surface.blit(instruction1 ,[290,635])
    instruction2=instruction_police.render("Appuyez sur ENTRER pour commencer",True, couleur.BLANC)
    surface.blit(instruction2 ,[287,637])
   
    #Version
    
    version_police=pygame.font.Font(None,18)
    version1=version_police.render("Version: J-7.4",True, couleur.BLANC)
    surface.blit(version1,[1180,700])
 
