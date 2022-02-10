import pygame, sys
from settings import *
from debug import debug
from level import Level
import time


class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('BODE GUARD')
        self.clock = pygame.time.Clock()
        self.lancer_partie = False

        #backgroud du menu principale
        self.bg = pygame.image.load('texture/bg_menu.jpg')

        #self.level = Level(num_map)




        # les différents modes
        self.is_playing = False
        self.is_command = False
        self.is_credits = False
        self.is_tuto = False
        self.is_niveau = False

        self.num_map = 1
        self.is_lunch = False

        #ecran pour choisir le niveau
    def affiche_niveau(self, screen):

            #bouton niveau 1
        niv1 = pygame.image.load('texture/niveau1.png')
        niv1 = pygame.transform.scale(niv1, (386,70))
        niv1_rect = niv1.get_rect()
        niv1_rect.x = 319
        niv1_rect.y = 300

        screen.blit(niv1, (319,300))

       

            #bouton niveau 2
        niv2 = pygame.image.load('texture/niveau2.png')
        niv2 = pygame.transform.scale(niv2, (386,70))
        niv2_rect = niv2.get_rect()
        niv2_rect.x = 319
        niv2_rect.y = 400

        screen.blit(niv2, (319,400))




        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if niv1_rect.collidepoint(event.pos):
                    #retourne au menu principale
                    self.is_niveau = False
                    self.num_map = 1
                    self.is_playing = True
                elif niv2_rect.collidepoint(event.pos):
                    #retourne au menu principale
                    self.is_niveau = False
                    self.num_map = 2
                    self.is_playing = True

                






    #maj des composants dés qu'ils sont lancés
    def lancer_jeu(self, screen):

        #code avec les initialisation du jeux et début
        if not self.is_lunch:
            self.level = Level(self.num_map)
            self.is_lunch = True
        test = self.level.run(self.num_map)
        return test

       
        #self.level.run()



    #affichage de la page des commandes
    def affiche_command(self, screen):
        self.is_command = True

        #introduction de l'image des commandes
        image = pygame.image.load('texture/lesCommandes.jpg')
        screen.blit(image, (0,0))

        #bouton retour
        retour = pygame.image.load('texture/retour.png')
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
        

        image = pygame.image.load('texture/noir.jpg')
        screen.blit(image, (0,0))

        retour = pygame.image.load('texture/retour.png')
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

    
        pass

    def set_is_playing(self, bool):
       self.is_playing = bool

    
    def run(self):
        self.clock_sec = time.gmtime().tm_sec
        self.temp = self.clock_sec
 
        while True:


            #arrière paln du jeux
            self.screen.blit(self.bg, (0,0))

            #vérifier si le jeux à commencer
            if game.is_playing:
                #déclancher les instructions de la partie
                game.is_playing = self.lancer_jeu(self.screen)

            #vérifier que l'on clique sur le bouton commande
            elif game.is_command:
                #déclanche la page des commandes
                self.affiche_command(self.screen)
            #vérifier que l'on clique sur le bouton credits
            elif game.is_credits:
                #déclanche la page des credits
                self.affiche_credits(self.screen)
            #vérifier que l'on clique sur le bouton tuto
            elif game.is_tuto:
                #déclanche la page du tutoriel
                self.tuto(self.screen)
            #vérifier si le jeu n'a pas commencé
            elif game.is_niveau:
                #affiche la page du niveau
                self.affiche_niveau(self.screen)
            #menu principal
            else:
                #importer charger le logo
                logo = pygame.image.load('texture/logo.png')
                logo = pygame.transform.scale(logo, (452,366))
                #importer charger le bouton pour lancer le jeu
                play = pygame.image.load('texture/play.png')
                play = pygame.transform.scale(play, (386,70))
                play_rect = play.get_rect()
                play_rect.x = 319
                play_rect.y = 359

                #importer charger le bouton pour les commandes
                command = pygame.image.load('texture/commandes.png')
                command = pygame.transform.scale(command, (386,70))
                command_rect = command.get_rect()
                command_rect.x = 319
                command_rect.y = 459

                #importer charger le bouton pour les credits
                credits = pygame.image.load('texture/credits.png')
                credits = pygame.transform.scale(credits, (386,70))
                credits_rect = credits.get_rect()
                credits_rect.x = 319
                credits_rect.y = 559

                #importer charger le boutton tuto pour lancer le tutoriel
                tuto = pygame.image.load('texture/tuto.png')
                tuto = pygame.transform.scale(tuto, (164,181))
                tuto_rect = tuto.get_rect()
                tuto_rect.x = 860
                tuto_rect.y = 587

                #ajouter écran bienvenue
                self.screen.blit(play, (319,359))
                self.screen.blit(command, (319,459))
                self.screen.blit(credits, (319,559))
                self.screen.blit(tuto, (860,587))
                self.screen.blit(logo, (286,0))

            #maj écran
            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                #vérifi pour savoir si le boutton play est cliqué
                    if play_rect.collidepoint(event.pos):
                        #jeux en mode lancer
                        self.is_niveau = True
                        #self.is_playing = True
                    if command_rect.collidepoint(event.pos):
                        #jeux en mode lancer
                        self.is_command = True
                    elif credits_rect.collidepoint(event.pos):
                        #jeux en mode lancer
                        self.is_credits = True
                    elif tuto_rect.collidepoint(event.pos):
                        #jeux en mode lancer
                        self.is_tuto = True

            self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()