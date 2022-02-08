import pygame
from game import Game

pygame.init()


# générer la fenetre du jeu
pygame.display.set_caption('Bode guard')
screen = pygame.display.set_mode((1024,768))

#backgroud du menu principale
bg = pygame.image.load('bg_menu.jpg')

#boucle pour le début
running = True

#charger le jeux
game = Game()

while running:


    #arrière paln du jeux
    screen.blit(bg, (0,0))

    #vérifier si le jeux à commencer
    if game.is_playing:
        #déclancher les instructions de la partie
        game.lancer_jeu(screen)
    #vérifier que l'on clique sur le bouton commande
    elif game.is_command:
        #déclanche la page des commandes
        game.affiche_command(screen)
    #vérifier que l'on clique sur le bouton credits
    elif game.is_credits:
        #déclanche la page des credits
        game.affiche_credits(screen)
    #vérifier que l'on clique sur le bouton tuto
    elif game.is_tuto:
        #déclanche la page du tutoriel
        game.tuto(screen)
    #vérifier si le jeu n'a pas commencé
    else:
        #importer charger le logo
        logo = pygame.image.load('logo.png')
        logo = pygame.transform.scale(logo, (452,366))

        #importer charger le bouton pour lancer le jeu
        play = pygame.image.load('play.png')
        play = pygame.transform.scale(play, (386,70))
        play_rect = play.get_rect()
        play_rect.x = 319
        play_rect.y = 359

        #importer charger le bouton pour les commandes
        command = pygame.image.load('commandes.png')
        command = pygame.transform.scale(command, (386,70))
        command_rect = command.get_rect()
        command_rect.x = 319
        command_rect.y = 459

        #importer charger le bouton pour les credits
        credits = pygame.image.load('credits.png')
        credits = pygame.transform.scale(credits, (386,70))
        credits_rect = credits.get_rect()
        credits_rect.x = 319
        credits_rect.y = 559

        #importer charger le boutton tuto pour lancer le tutoriel
        tuto = pygame.image.load('tuto.png')
        tuto = pygame.transform.scale(tuto, (164,181))
        tuto_rect = tuto.get_rect()
        tuto_rect.x = 860
        tuto_rect.y = 587

        #ajouter écran bienvenue
        screen.blit(play, (319,359))
        screen.blit(command, (319,459))
        screen.blit(credits, (319,559))
        screen.blit(tuto, (860,587))
        screen.blit(logo, (286,0))


    #maj écran
    pygame.display.flip()



    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #vérif venemetn fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()




        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérifi pour savoir si le boutton play est cliqué
            if play_rect.collidepoint(event.pos):
                #jeux en mode lancer
                game.is_playing = True
            if command_rect.collidepoint(event.pos):
                #jeux en mode lancer
                game.is_command = True
            elif credits_rect.collidepoint(event.pos):
                #jeux en mode lancer
                game.is_credits = True
            elif tuto_rect.collidepoint(event.pos):
                #jeux en mode lancer
                game.is_tuto = True

            


