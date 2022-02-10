from distutils.log import debug
from re import X
import pygame
from mob1 import Mob1
from settings import *
from speed_potion import SpeedPotion
from water_block import Water_block
from water_block import Water_block_night
from grass_block import Grass_block, Grass_block_night
from wet_block import Wet_block, Wet_block_night
from player import Player
from tente import Tente, Tente_night
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
        self.items_sprites = pygame.sprite.Group()

        self.entity_list = []

        #get game screen space
        self.display_surface = pygame.display.get_surface()

        #setup the sprite
        self.create_map()

        #user interface
        self.ui = UI()

        # day n night
        self.day_duration = DAY_DURATION
        self.night_duration = NIGHT_DURATION
        self.day_pass = False

    def create_map(self):
        X_m =[]
        Y_m = []
        self.every_day_texture = []
        self.every_night_texture = []
        for row_index,row in enumerate(MAP_1):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE
                if col == 'o':
                    self.every_day_texture.append(Water_block((x,y),[self.visible_sprites, self.obstacles_sprites]))
                    self.every_night_texture.append(Water_block_night((x,y),[self.visible_sprites, self.obstacles_sprites]))
                if col == 'w':
                    self.every_day_texture.append(Wet_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append( Wet_block_night((x,y),[self.visible_sprites]))
                if col == 'p':
                    X_p = x
                    Y_p = y
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                if col == 'm':
                    X_m.append(x)
                    Y_m.append(y)
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                if col == 't':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                    X_t = x
                    Y_t = y
                    
                if col == ' ':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
        i =0
        for mob in X_m:
            self.entity_list.append(Mob1((X_m[i],Y_m[i]),[self.visible_sprites], self.obstacles_sprites))
            i+=1

        self.every_day_texture.append(Tente((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites]))
        self.every_night_texture.append(Tente_night((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites]))
        SpeedPotion((3100, 2300), [self.visible_sprites, self.items_sprites])
        SpeedPotion((3100, 2400), [self.visible_sprites, self.items_sprites])
        SpeedPotion((3100, 2500), [self.visible_sprites, self.items_sprites])
        self.player = Player(self, (X_p,Y_p), [self.visible_sprites], self.obstacles_sprites)
        self.entity_list.append(self.player)
        for texture in self.every_night_texture:
            self.visible_sprites.remove(texture)



    def create_map_night(self):
        for entity in self.entity_list:
            self.visible_sprites.remove(entity)

        for texture in self.every_day_texture:
            self.visible_sprites.remove(texture)

        for texture in self.every_night_texture:
            self.visible_sprites.add(texture)

        for entity in self.entity_list:
            self.visible_sprites.add(entity)


    def run(self):
        #draw things
        #self.visible_sprites.draw(self.display_surface)
        if pygame.time.get_ticks() >= DAY_DURATION and not self.day_pass:
            self.day_pass = True
            self.create_map_night()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)
        self.player.updateEffect()

    def interactEvent(self):
        for item in pygame.sprite.spritecollide(self.player, self.items_sprites, 1):
            self.player.addToInventory(item)
            del item
    
    def throwEvent(self, item, coords):
        if item == "Potion of swiftness":
            self.visible_sprites.remove(self.player)
            SpeedPotion(coords, [self.visible_sprites, self.items_sprites])
            self.visible_sprites.add(self.player)


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
