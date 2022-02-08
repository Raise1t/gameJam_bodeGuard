from distutils.log import debug
from re import X
import pygame
from settings import *
from speed_potion import SpeedPotion
from water_block import Water_block
from player import Player
from tente import Tente
from grass import Grass
from debug import debug

class Level:
    def __init__(self):
        #sprite group
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.items_sprites = pygame.sprite.Group()

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
                    Water_block((x,y),[self.visible_sprites, self.obstacles_sprites])
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
        Tente((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites])
        SpeedPotion((1200, 1200), [self.visible_sprites, self.items_sprites])
        self.player = Player(self, (X_p,Y_p),[self.visible_sprites], self.obstacles_sprites)

    def run(self):
        #draw things
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)

    def interactEvent(self, playerRect):
        for item in self.items_sprites:
            if pygame.Rect.colliderect(playerRect, item):
                self.player.addToInventory(item)
                self.removeItem(item)
    
    def removeItem(self, item):
        pass
