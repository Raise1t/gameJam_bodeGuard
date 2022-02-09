from distutils.log import debug
from re import X
import pygame
from mob1 import Mob1
from settings import *
from water_block import Water_block
from grass_block import Grass_block
from wet_block import Wet_block
from player import Player
from tente import Tente
from debug import debug
from ui import UI
import time
from entity import Entity


class Level:
    def __init__(self):
        #sprite group
        #self.visible_sprites = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #get game screen space
        self.display_surface = pygame.display.get_surface()

        #setup the sprite
        self.create_map()

        #user interface
        self.ui = UI()

        # day n night
        self.day_duration = DAY_DURATION
        self.night_duration = NIGHT_DURATION

    def create_map(self):
        for row_index,row in enumerate(MAP_1):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE
                if col == 'o':
                    Water_block((x,y),[self.visible_sprites, self.obstacles_sprites])
                if col == 'w':
                    Wet_block((x,y),[self.visible_sprites])
                if col == 'p':
                    X_p = x
                    Y_p = y
                    Grass_block((x,y),[self.visible_sprites])
                if col == 'm':
                    X_m = x
                    Y_m = y
                    Grass_block((x,y),[self.visible_sprites])
                if col == 't':
                    Grass_block((x,y),[self.visible_sprites])
                    X_t = x
                    Y_t = y
                    
                if col == ' ':
                    Grass_block((x,y),[self.visible_sprites])
        Mob1((X_m,Y_m),[self.visible_sprites], self.obstacles_sprites)
        Tente((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites])
        self.player = Player((X_p,Y_p),[self.visible_sprites], self.obstacles_sprites)

    def run(self):
        #draw things
        #self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_witdh = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_witdh
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
        #for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') if sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
