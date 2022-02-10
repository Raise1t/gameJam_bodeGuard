from dis import dis
import pygame
from settings import *
from entity import Entity
from debug import debug

class Mob1(Entity):
    def __init__(self, pos,groups, obstacle_sprites):

        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.attack_radius = 50
        self.notice_radius = 300

        self.image = pygame.image.load('texture/mob1.png').convert_alpha()
        self.stats = {'health': 100, 'attack': 10, 'speed': 3}
        self.health = self.stats['health']
        self.speed = self.stats['speed']

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10,-10)
        self.obstacle_sprites = obstacle_sprites

        self.can_attack = True
        self.attack_cooldown_v = 400
        self.temp = 0 #pour le cooldown
        self.u =0

    def update(self):
        self.move(self.speed)

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)


    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
             direction = pygame.math.Vector2()
        return(distance, direction)

    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]
        #print(distance)
        if distance < self.attack_radius and self.can_attack:
            self.status = 'attack'
            #print('attack')
        elif distance <= self.notice_radius:
            self.status = 'move'
            #print('move')
        else:
            self.status = 'pnj'
    
    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            player.hitted()
            self.can_attack =False
            self.attack_cooldown()

        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]

        else:
            self.direction = pygame.math.Vector2()
            self.can_attack = True


    def attack_cooldown(self):
        
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            self.temp += current_time - self.u
            print(self.temp)
            if self.temp >= self.attack_cooldown_v:
                self.temp = 0
                self.u = current_time
                print(self.temp)
                self.can_attack = True
        else:
            print('attack')
