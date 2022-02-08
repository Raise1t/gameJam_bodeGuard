#class player:

    #def __init__(self, name, skin):
    #    self.__name = name
    #    self.__health = 100
    #    self.__food = 100
    #    self.__inventory = {}
    #    self.__skin = ""
from ast import If
from curses import KEY_DOWN
#from typing_extensions import Self
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self._speed = 5
        self.obstacle_sprites = obstacle_sprites
        self._health = 100

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

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_z]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_q]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()*0.80

        self.rect.x += self.direction.x*speed
        self.colision('hor')
        self.rect.y += self.direction.y*speed
        self.colision('ver')
        #self.rect.center += self.direction * speed

    def colision(self, direction):
        if direction == 'hor':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'ver':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)