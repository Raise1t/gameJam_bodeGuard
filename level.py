import pygame
from settings import *
from block import Block

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
        for row_index,row in enumerate(MAP_1):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE
                if col == 'o':
                    Block((x,y),[self.visible_sprites])

    def run(self):
        #draw things
        self.visible_sprites.draw(self.display_surface)