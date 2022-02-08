from distutils.log import debug
from re import X
import pygame
from settings import *
from block import Block
from player import Player
from tente import Tente
from grass import Grass
from debug import debug

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
                    Block((x,y),[self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    X_p = x
                    Y_p = y
                    Grass((x,y),[self.visible_sprites])
                if col == 't':
                    Grass((x,y),[self.visible_sprites])
                    X_t = x
                    Y_t = y
                    
                if col == ' ':
                    Grass((x,y),[self.visible_sprites])
        Tente((X_t,Y_t),[self.visible_sprites])
        self.player = Player((X_p,Y_p),[self.visible_sprites], self.obstacles_sprites)

    def run(self):
        #draw things
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)