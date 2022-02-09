from ast import If
from curses import KEY_DOWN
from xxlimited import new
#from typing_extensions import Self
import pygame
from settings import *
from item import Item

class Player(pygame.sprite.Sprite):
    def __init__(self, level, pos,groups,obstacle_sprites) -> None:
        super().__init__(groups)
        self.__level = level
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self._speed = 4
        self.obstacle_sprites = obstacle_sprites
        self._health = 100
        self._inventory = {}
        self._selectedSlot = 0
        self.hitbox = self.rect.inflate(-10,0)
        
        #stats
        self.stats = {'health': 100, 'attack': 10, 'speed': 5}
        self.health = self.stats['health']
        self.speed = self.stats['speed']

    #########################################################################

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, newHealth):
        if newHealth < 0:
            raise ValueError
        else:
            self._health = newHealth
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, newSpeed):
        self._speed = newSpeed
    
    @property
    def selectedSlot(self):
        return self._selectedSlot
    
    @selectedSlot.setter
    def selectedSlot(self, newSlot):
        if newSlot >= 0 and newSlot < 4:
            self._selectedSlot = newSlot
    
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
    
    def removeFromInventory(self, slot):
        if len(self._inventory) > slot:
            item = self.getItemNameFromSlot(slot)
            if self._inventory[item] > 1:
                self._inventory[item] -= 1
            else:
                del self._inventory[item]

            self.__level.throwEvent(item, (self.hitbox.x, self.hitbox.y))
        
    
    def getItemNameFromSlot(self, slot) -> str :
        count = 0
        name = ""
        for i in self._inventory.keys():
            if count == slot:
                name = i
            count+=1
        return name



    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_z] or key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.direction.x = 1
        elif key[pygame.K_q] or key[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if key[pygame.K_j]:
            self.__level.interactEvent()
        if key[pygame.K_r]:
            item = self.removeFromInventory(self._selectedSlot)
        
        if key[pygame.K_i]:
            self.selectedSlot = self.selectedSlot - 1
        if key[pygame.K_o]:
            self.selectedSlot = self.selectedSlot + 1
        if key[pygame.K_AMPERSAND]:
            self.selectedSlot = 0
        if key[233]:
            self.selectedSlot = 1
        if key[pygame.K_QUOTEDBL]:
            self.selectedSlot = 2
        if key[pygame.K_QUOTE]:
            self.selectedSlot = 3
        
    
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

    def update(self):
        self.input()
        self.move(self.speed)