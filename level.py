from distutils.log import debug
from re import X
from telnetlib import SE
import pygame
from mob1 import Mob1
from settings import *
from speed_potion import SpeedPotion
from crack_potion import CrackPotion
from water_block import Water_block
from water_block import Water_block_night
from grass_block import Grass_block, Grass_block_night
from wet_block import Wet_block, Wet_block_night
from player import Player
from tente import Tente, Tente_night
from ui import UI
from bode import Bode, Bode_night
from tree import *



class Level:
    def __init__(self, num):
        #sprite group
        #self.visible_sprites = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.items_sprites = pygame.sprite.Group()

        self.entity_list = []
        self.map = num

        #get game screen space
        self.display_surface = pygame.display.get_surface()

        #setup the sprite
        self.create_map(num)
        
        #user interface
        self.ui = UI()

        # day n night
        self.day_duration = DAY_DURATION
        self.night_duration = NIGHT_DURATION
        self.game_start_at = pygame.time.get_ticks()
        self.day_pass = False
        self.night_pass = True

        

    def create_map(self, num_map):

        if num_map == 1:
            map= MAP_1
        elif num_map ==2:
            map = MAP_2
        elif num_map ==3:
            map = MAP_3
        else:
            map = MAP_0

        X_ps =[]
        Y_ps = []
        X_pc =[]
        Y_pc = []
        X_m =[]
        Y_m = []

        X_a1 =[]
        Y_a1 = []
        X_a2 =[]
        Y_a2 = []
        X_a3 =[]
        Y_a3 = []

        X_t = 0
        X_p = 0
        Y_p = 0
        Y_t = 0
        X_b = 0
        Y_b = 0
        
        self.every_day_texture = []
        self.every_night_texture = []
        for row_index,row in enumerate(map):
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
                if col == 's':
                    X_ps.append(x)
                    Y_ps.append(y)
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                if col == 'c':
                    X_pc.append(x)
                    Y_pc.append(y)
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))


                if col == 'b':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                    X_b = x
                    Y_b = y

                if col == 'a1':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                    X_a1.append(x)
                    Y_a1.append(y)

                if col == 'a2':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                    X_a2.append(x)
                    Y_a2.append(y)

                if col == 'a3':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))
                    X_a3.append(x)
                    Y_a3.append(y)
                if col == ' ':
                    self.every_day_texture.append(Grass_block((x,y),[self.visible_sprites]))
                    self.every_night_texture.append(Grass_block_night((x,y),[self.visible_sprites]))

        i = 0
        for mob in X_m:
            self.entity_list.append(Mob1((X_m[i],Y_m[i]),[self.visible_sprites], self.obstacles_sprites))
            i+=1

        i = 0
        for ps in X_ps:
            potion = SpeedPotion((X_ps[i],Y_ps[i]), [self.visible_sprites, self.items_sprites])
            self.every_night_texture.append(potion)
            i += 1

        i = 0
        for pc in X_pc:
            potion = CrackPotion((X_pc[i],Y_pc[i]), [self.visible_sprites, self.items_sprites])
            self.every_night_texture.append(potion)
            i += 1

        i = 0
        for a1 in X_a1:
            tree = Tree1((X_a1[i],Y_a1[i]),[self.visible_sprites, self.obstacles_sprites])
            self.every_day_texture.append(tree)
            tree = Tree_night1((X_a1[i],Y_a1[i]),[self.visible_sprites, self.obstacles_sprites])
            self.every_night_texture.append(tree)
            i += 1
        
        i = 0
        for a2 in X_a2:
            self.every_day_texture.append(Tree2((X_a2[i],Y_a2[i]),[self.visible_sprites, self.obstacles_sprites]))
            self.every_night_texture.append(Tree_night2((X_a2[i],Y_a2[i]),[self.visible_sprites, self.obstacles_sprites]))
            i += 1
        i = 0
        for pc in X_a3:
            self.every_day_texture.append(Tree3((X_a3[i],Y_a3[i]),[self.visible_sprites, self.obstacles_sprites]))
            self.every_night_texture.append(Tree_night3((X_a3[i],Y_a3[i]),[self.visible_sprites, self.obstacles_sprites]))
            i += 1

        self.every_day_texture.append(Tente((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites]))
        self.every_night_texture.append(Tente_night((X_t,Y_t),[self.visible_sprites, self.obstacles_sprites]))

        self.every_day_texture.append(Bode((X_b,Y_b),[self.visible_sprites, self.obstacles_sprites]))
        self.every_night_texture.append(Bode_night((X_b,Y_b),[self.visible_sprites, self.obstacles_sprites]))

        self.player = Player(self,(X_p,Y_p), [self.visible_sprites], self.obstacles_sprites)
        self.entity_list.append(self.player)
        
        for texture in self.every_night_texture:
            self.visible_sprites.remove(texture)
        



    def create_map_night(self, map):
        for entity in self.entity_list:
            self.visible_sprites.remove(entity)
        
        for texture in self.every_day_texture:
            self.visible_sprites.remove(texture)

        for texture in self.every_night_texture:
            self.visible_sprites.add(texture)

        for entity in self.entity_list:
            self.visible_sprites.add(entity)

    def reset(self, player, entity_list, obstacles_list):
        player.reset()
        entity_list.clear()
        self.day_pass = False


    def return_to_day(self):
        for entity in self.entity_list:
            self.visible_sprites.remove(entity)

        for texture in self.every_day_texture:
            self.visible_sprites.add(texture)

        for texture in self.every_night_texture:
            self.visible_sprites.remove(texture)

        for entity in self.entity_list:
            self.visible_sprites.add(entity)


    def is_day_or_night(self):
        self.timer = (pygame.time.get_ticks() - self.game_start_at) / 1000
        if self.timer >= DAY_DURATION and not self.day_pass:

            self.create_map_night(self.map)
            self.day_pass = True
            self.night_pass =False
            self.game_start_at = pygame.time.get_ticks()
            self.timer = 0

        if self.timer >= NIGHT_DURATION and not self.night_pass:
            self.game_start_at = pygame.time.get_ticks()
            self.return_to_day()
            self.day_pass = False
            self.night_pass = True


    def run(self, num_map):
        #draw things
        #self.visible_sprites.draw(self.display_surface)
        if self.map == 0:
            return False
        if not self.player.death():
            
            self.is_day_or_night()
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.ui.display(self.player)
            self.player.updateEffect()
            debug(self.timer)
            return True
        else:
            self.reset(self.player, self.entity_list, self.obstacles_sprites)
            return False

        



    def interactEvent(self):
        for item in pygame.sprite.spritecollide(self.player, self.items_sprites, 1):
            self.player.addToInventory(item)
            if item in self.every_day_texture:
                self.every_day_texture.remove(item)
            if item in self.every_night_texture:
                self.every_night_texture.remove(item)

            del item
    
    def throwEvent(self, item, coords):
        if item == "Potion of swiftness":
            self.visible_sprites.remove(self.player)
            potion = SpeedPotion(coords, [self.visible_sprites, self.items_sprites])
            self.every_night_texture.append(potion)
            self.visible_sprites.add(self.player)
        elif item == "Potion of crack":
            self.visible_sprites.remove(self.player)
            potion = CrackPotion(coords, [self.visible_sprites, self.items_sprites])
            self.every_night_texture.append(potion)
            self.visible_sprites.add(self.player)
    
    def updatePlayerEffect(self):
        effects = []
        for key, value in self.player.effects.items():
            if value:
                effects.append(key)
        self.ui.showEffectDuration(effects)


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
