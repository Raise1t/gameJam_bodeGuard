import pygame
from settings import *

class Level:
    def __init__(self):
        #sprite group
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #get game screen space
        self.display_surface = pygame.display.get_surface()

        #setup the sprite
        self.create_map()

    def create_map(self):
        for row in MAP_1:
            print(row)

    def run(self):
        #draw things
        pass