import pygame
from sqlalchemy import null



#classe du jeu
class Game:

    #constructeur
    def __init__(self): 

        #definir si le jeux a commencer
        self.is_playing = False
        self.is_command = False
        self.is_credits = False
        self.is_tuto = False

    

    #maj des composants dés qu'ils sont lancés
    def lancer_jeu(self, screen):

        #code avec les initialisation du jeux et début
        pass
        

    #affichage de la page des commandes
    def affiche_command(self, screen):
        self.is_command = True

        #introduction de l'image des commandes
        image = pygame.image.load('lesCommandes.jpg')
        screen.blit(image, (0,0))

        #bouton retour

        retour = pygame.image.load('retour.png')
        retour = pygame.transform.scale(retour, (386,70))
        retour_rect = retour.get_rect()
        retour_rect.x = 319
        retour_rect.y = 600

        screen.blit(retour, (319,600))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_rect.collidepoint(event.pos):
                    #retourne au menu principale
                    self.is_command = False

        

    #affichage de la page des credits
    def affiche_credits(self, screen):
        #bouton retour

        image = pygame.image.load('noir.jpg')
        screen.blit(image, (0,0))

        retour = pygame.image.load('retour.png')
        retour = pygame.transform.scale(retour, (386,70))
        retour_rect = retour.get_rect()
        retour_rect.x = 319
        retour_rect.y = 600

        screen.blit(retour, (319,600))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_rect.collidepoint(event.pos):
                    #retourne au menu principale
                    self.is_credits = False

    #affichage de la page du tuto
    def tuto(self, screen):

    
        return null

