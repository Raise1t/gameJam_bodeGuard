from curses import KEY_DOWN
#from typing_extensions import Self
import pygame
from entity import Entity
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
        self.stats = {'health': 100, 'attack': 10, 'speed': 6}
        self.health = self.stats['health']
        self.speed = self.stats['speed']

        #day n night
        self.game_start_at = pygame.time.get_ticks()

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
        self.timer = (pygame.time.get_ticks() - self.game_start_at) / 1000
        if self.timer >= DAY_DURATION:
            self.image = pygame.image.load('texture/player_night.png').convert_alpha()
        self.input()
        self.move(self.speed)

    def hitted(self):
        self.health = self.health - ( self.stats['health'] * 0.77 )
        if self.health <= 0:
            self.health = 0

