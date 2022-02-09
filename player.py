from curses import KEY_DOWN
#from typing_extensions import Self
import pygame
from entity import Entity
from game import Game
from settings import *
from debug import debug


class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.obstacle_sprites = obstacle_sprites
        self.hitbox = self.rect.inflate(-10,0)

        #stats
        self.stats = {'health': 100, 'attack': 10, 'speed': 8}
        self.health = self.stats['health']
        self.speed = self.stats['speed']
        #le joueur est en vie
        self.alive = True

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

    def update(self):
        if pygame.time.get_ticks() >= DAY_DURATION:
            self.image = pygame.image.load('texture/player_night.png').convert_alpha()
        self.input()
        self.move(self.speed)


    #le joueur est mort
    def death(self, health):
        if self.health <= 0:
            self.alive = False
            #Game.set_is_playing(False)
            

    #le joueur perd de la vie
    def lost_life(self, pv_lost):
        if self.alive:
            self.health = self.health - pv_lost
            self.death(self.health)
            print('pv =')
            print(self.health)
