from ast import If
from curses import KEY_DOWN
#from typing_extensions import Self
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, level, pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.__level = level
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self._speed = 4
        self.obstacle_sprites = obstacle_sprites
        self._health = 100
        self._inventory = {}
        self.hitbox = self.rect.inflate(-10,0)

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

    ###########################################################################

    def addToInventory(self, item):
        try:
            self._inventory[item] += 1
            print("You now have ", self._inventory[item], " of ", item)
        except KeyError:
            self._inventory[item] = 1
            print("Created a spot for ", item)
    
    def removeFromInventory(self, item):
        self._inventory[item] -= 1
    

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
            self.__level.interactEvent(self.rect)

        
    
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