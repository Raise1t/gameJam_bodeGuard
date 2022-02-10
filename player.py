
from ast import If
from curses import KEY_DOWN
from operator import getitem
#from xxlimited import new
from tkinter.font import families
#from typing_extensions import Self
import pygame
from sympy import false
import pygame, sys
from entity import Entity
from game import Game
from settings import *
from item import Item



class Player(Entity):

    def __init__(self,level,pos,groups,obstacle_sprites) -> None:
        super().__init__(groups)
        self.__level = level
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        self._inventory = {}
        self._selectedSlot = 0
        self.hitbox = self.rect.inflate(-10,0)

        #day n night
        self.game_start_at = pygame.time.get_ticks()
        self.day_pass = False
        self.night_pass = True
        
        #stats
        self.stats = {'health': 100, 'attack': 10, 'speed': 6.5, 'armor': 1}
        self._effects = {'Speed' : None, 'Strength' : None, 'Crack' : None}
        self.health = self.stats['health']
        self.speed = self.stats['speed']

        #self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.path = 'texture/Player1/animations/'
        self.sprites = {'left': [],'right': [], 'right_idle':[],'left_idle':[]}


        
        self.sprites['right_idle'].append(pygame.image.load(self.path + 'right_idle/idle_1.png').convert_alpha())
        self.sprites['right_idle'].append(pygame.image.load(self.path + 'right_idle/idle_2.png').convert_alpha())
        self.sprites['right_idle'].append(pygame.image.load(self.path + 'right_idle/idle_3.png').convert_alpha())
        self.sprites['right_idle'].append(pygame.image.load(self.path + 'right_idle/idle_4.png').convert_alpha())

        #self.sprites_idle_left
        self.sprites['left_idle'].append(pygame.image.load(self.path + 'left_idle/idle_1.png').convert_alpha())
        self.sprites['left_idle'].append(pygame.image.load(self.path + 'left_idle/idle_2.png').convert_alpha())
        self.sprites['left_idle'].append(pygame.image.load(self.path + 'left_idle/idle_3.png').convert_alpha())
        self.sprites['left_idle'].append(pygame.image.load(self.path + 'left_idle/idle_4.png').convert_alpha())

        #self.sprites_w_right = []
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_1.png').convert_alpha())
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_2.png').convert_alpha())
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_3.png').convert_alpha())
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_4.png').convert_alpha())
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_5.png').convert_alpha())
        self.sprites['right'].append(pygame.image.load(self.path + 'right/right_6.png').convert_alpha())            
            
        #self.sprites_w_left = []
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_1.png').convert_alpha())
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_2.png').convert_alpha())
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_3.png').convert_alpha())
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_4.png').convert_alpha())
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_5.png').convert_alpha())
        self.sprites['left'].append(pygame.image.load(self.path + 'left/left_6.png').convert_alpha())                      

        #self.sprites_idle_left    

        self.index = 0 #general index for sprites

        self.speed_sprite = 0.35

        self.image = self.sprites['right_idle'] [0]

        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites
        self.hitbox = self.rect.inflate(-10, 0)

        # idle
        self.idle_right_animation = True
        self.idle_left_animation = False
        # walking
        self.walk_right_animation = False
        self.walk_left_animation = False

        self.direction = pygame.math.Vector2()
        self.status = 'right_idle'

        self.right_direction = True
        self.left_direction = False



    #########################################################################
    
    @property
    def selectedSlot(self):
        return self._selectedSlot
    
    @selectedSlot.setter
    def selectedSlot(self, newSlot):
        if newSlot >= 0 and newSlot < 4:
            self._selectedSlot = newSlot

    @property
    def effects(self):
        return self._effects
    
    def getInventory(self):
        return self._inventory

    ###########################################################################

    def addToInventory(self, item) -> None :
        try:
            self._inventory[item.getName()] += 1
            print("You now have ", self._inventory[item.getName()], item.getName())
        except KeyError:
            self._inventory[item.getName()] = 1
            print("Created a slot for", item.getName())
            print("You now have", self._inventory[item.getName()], item.getName())
    
    def removeFromInventory(self, item):
            if self._inventory[item] > 1:
                self._inventory[item] -= 1
            else:
                del self._inventory[item]
        
    
    def getItemNameFromSlot(self, slot) -> str :
        count = 0
        name = ""
        for i in self._inventory.keys():
            if count == slot:
                name = i
            count+=1
        return name

    def addEffect(self, effect, potionObject):
        self._effects[effect] = potionObject
    
    def removeEffect(self, effect):
        self._effects[effect] = None
    
    def updateEffect(self):
        for key, value in self.effects.items():
            if value:
                if pygame.time.get_ticks() > value.startTime + value.effectDuration:
                    value.endEffect(self)
    
    def setArmor(self, armorValue):
        self.stats['armor'] = armorValue
        

    def wich_direction_stop(self): #if player stops, wich direction to look?
        if self.right_direction:
                self.idle_right_animation = True
                self.idle_left_animation = False
                self.walk_right_animation = False
                self.walk_left_animation = False
        if self.left_direction:
                self.idle_left_animation =True    
                self.idle_right_animation = False
                self.walk_right_animation = False
                self.walk_left_animation = False

    def get_status(self): 
        #idle
        if self.direction.x == 0 and self.direction.y == 0:
            if self.right_direction:
                self.status = 'right_idle'
            if self.left_direction:
                self.status = 'left_idle'


        elif self.direction.x == -1: #gauche
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = True
            self.right_direction = False
            self.walk_right_animation = False
            self.walk_left_animation = True
            self.status = 'left'


        elif self.direction.x == 1 :#droite
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = False
            self.right_direction = True
            self.walk_right_animation = True
            self.walk_left_animation = False
            self.status = 'right'

        elif self.direction.x == -1 and self.direction.y == -1 :# diagonale gauche haut
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = True
            self.right_direction = False
            self.walk_right_animation = False
            self.walk_left_animation = True
            self.status = 'left'   

        elif self.direction.x == -1 and self.direction.y == 1 :#diagonale gauche bas
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = True
            self.right_direction = False
            self.walk_right_animation = False
            self.walk_left_animation = True
            self.status = 'left'

        elif self.direction.x == 1 and self.direction.y == -1 :#diagonale droite haut            self.idle_left_animation = False
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = False
            self.right_direction = True
            self.walk_right_animation = True
            self.walk_left_animation = False
            self.status = 'right'

        elif self.direction.x == 1 and self.direction.y == -1:#diagonale droite bas            self.idle_left_animation = False
            self.idle_left_animation = False
            self.idle_right_animation = False
            self.left_direction = False
            self.right_direction = True
            self.walk_right_animation = True
            self.walk_left_animation = False
            self.status = 'right'  

        elif self.direction.x == 0 and self.direction.y == -1: # haut
            if self.right_direction:
                self.idle_left_animation = False
                self.idle_right_animation = False
                self.left_direction = False
                self.right_direction = True
                self.walk_right_animation = True
                self.walk_left_animation = False
                self.status = 'right'

            if self.left_direction:
                self.idle_left_animation = False
                self.idle_right_animation = False
                self.left_direction = True
                self.right_direction = False
                self.walk_right_animation = False
                self.walk_left_animation = True
                self.status = 'left'

        elif self.direction.x == 0 and self.direction.y == 1: # bas
            if self.right_direction:
                self.idle_left_animation = False
                self.idle_right_animation = False
                self.left_direction = False
                self.right_direction = True
                self.walk_right_animation = True
                self.walk_left_animation = False
                self.status = 'right'
                

            if self.left_direction:
                self.idle_left_animation = False
                self.idle_right_animation = False
                self.left_direction = True
                self.right_direction = False
                self.walk_right_animation = False
                self.walk_left_animation = True
                self.status = 'left'        

    def input(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_z] or key[pygame.K_UP]:
            self.direction.y = -1
            self.get_status()

        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.direction.y = 1
            self.get_status()
            
        else:
            self.direction.y = 0
            self.get_status()

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.get_status()
        elif key[pygame.K_q] or key[pygame.K_LEFT]:
            self.direction.x = -1
            self.get_status()
        else:
            self.direction.x = 0
        
        if key[pygame.K_AMPERSAND]:
            self.selectedSlot = 0
        if key[233]:
            self.selectedSlot = 1
        if key[pygame.K_QUOTEDBL]:
            self.selectedSlot = 2
        if key[pygame.K_QUOTE]:
            self.selectedSlot = 3
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_j:
                    item = self.getItemNameFromSlot(self._selectedSlot)
                    if item == "" or not Item.items[item].isConsumable:
                        self.__level.interactEvent()
                    else:
                        Item.items[item].useItem(self, pygame.time.get_ticks())

                if event.key == pygame.K_r:
                    if len(self._inventory) > self._selectedSlot:
                        item = self.getItemNameFromSlot(self._selectedSlot)
                        self.removeFromInventory(item)
                        self.__level.throwEvent(item, (self.hitbox.x, self.hitbox.y))
        
                if event.key == pygame.K_i:
                    self.selectedSlot = self.selectedSlot - 1
                if event.key == pygame.K_o:
                    self.selectedSlot = self.selectedSlot + 1
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()*0.80

        #self.rect.x += self.direction.x*speed
        self.hitbox.x += self.direction.x*speed
        self.colision('hor')

        #self.rect.y += self.direction.y*speed
        self.hitbox.y += self.direction.y*speed
        self.colision('ver')

        #self.rect.center += self.direction * speed
        self.rect.center = self.hitbox.center

    def colision(self, direction):
        if direction == 'hor':
            for sprite in self.obstacle_sprites:
                #if sprite.rect.colliderect(self.rect):
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        #self.rect.right = sprite.rect.left
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        #self.rect.left = sprite.rect.right
                        self.hitbox.left = sprite.hitbox.right


        if direction == 'ver':
            for sprite in self.obstacle_sprites:
                #if sprite.rect.colliderect(self.rect):
                if sprite.hitbox.colliderect(self.hitbox):   
                    if self.direction.y > 0:
                        #self.rect.bottom = sprite.rect.top
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        #self.rect.top = sprite.rect.bottom
                        self.hitbox.top = sprite.hitbox.bottom

    def is_day_or_night(self):
        self.timer = (pygame.time.get_ticks() - self.game_start_at) / 1000
        if self.timer >= DAY_DURATION and not self.day_pass:
            self.speed = self.speed * 1.08
            self.image = pygame.image.load('texture/player2.png').convert_alpha()
            self.day_pass = True
            self.night_pass =False
            self.game_start_at = pygame.time.get_ticks()
            self.timer = 0

        if self.timer >= NIGHT_DURATION and not self.night_pass:
            
            self.game_start_at = pygame.time.get_ticks()
            self.image = pygame.image.load('texture/player.png').convert_alpha()
            self.day_pass = False
            self.night_pass = True  


    #le joueur est mort
    def death(self):
        if self.health <= 0:
            
            return True
        else:
            return False
            #Game.set_is_playing(False)
            
    def reset(self):
        self.health = self.stats["health"]
        print('reset')
        
    def hitted(self):
        if self.night_pass:
            self.health = self.health - ( self.stats['health'] * 1/6 )
        else:
            self.health = self.health - ( self.stats['health'] * 1/3 )

            # ANIMATIONS CONTROLER-----------------------------        

    def animate(self):
        
        animation = self.sprites[self.status]
        #loop over the frame index
        self.index += self.speed_sprite
        if self.index >= 4:
            self.index = 0
        #set the image
        self.image = animation[int(self.index)]  
        

    def update(self):
        self.is_day_or_night()
        self.input()
        self.animate()
        self.move(self.speed)
        #if pygame.time.get_ticks() >= DAY_DURATION:
         #   self.animate()    
        

