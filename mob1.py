from dis import dis
import pygame
from settings import *
from entity import Entity
from debug import debug
from player import Player

class Mob1(Entity):
    def __init__(self, pos,groups, obstacle_sprites):

        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.attack_radius = 40
        self.notice_radius = 500

        self.notice_radius_day = 500
        self.notice_radius_night = 800

        self.image = pygame.image.load('texture/mob1.png').convert_alpha()
        self.stats = {'health': 100, 'attack': 10, 'speed': 4.5}

        self.health = self.stats['health']
        self.speed = self.stats['speed']

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10,-10)
        self.obstacle_sprites = obstacle_sprites

        self.can_attack = True
        self.attack_cooldown_v = 900
        self.attack_at = 0
        self.temp = 0 #pour le cooldown
        self.u =0

        #day n night
        self.game_start_at = pygame.time.get_ticks()
        self.day_pass = False
        self.night_pass = True

    def is_day_or_night(self):
        self.timer = (pygame.time.get_ticks() - self.game_start_at) / 1000

        if self.timer >= DAY_DURATION and not self.day_pass:
            self.image = pygame.image.load('texture/mob1_night.png').convert_alpha()
            self.speed = self.speed * 1.12
            self.notice_radius_night = self.notice_radius_night * 1.12
            self.notice_radius = self.notice_radius_night
            self.day_pass = True
            self.night_pass =False
            self.game_start_at = pygame.time.get_ticks()
            self.timer = 0

        if self.timer >= NIGHT_DURATION and not self.night_pass:
           
            self.game_start_at = pygame.time.get_ticks()
            self.image = pygame.image.load('texture/mob1.png').convert_alpha()
            self.notice_radius_day = self.notice_radius_day * 1.12
            self.notice_radius = self.notice_radius_day
            self.day_pass = False
            self.night_pass = True  
    
    
    
    def update(self):
        self.is_day_or_night()
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
            self.attack_cooldown()
            player.hitted()
            self.status

        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
            self.attack_cooldown()
            

        else:
            self.direction = pygame.math.Vector2()
            self.can_attack = True


    def attack_cooldown(self):
        #print('le mob peut attaquer :', self.can_attack)
        
        if not self.can_attack:
            
            count_ticks = (pygame.time.get_ticks() - self.attack_at)

            #print(self.temp)            
            if count_ticks >= self.attack_cooldown_v:
                self.can_attack = True
        else:

            self.attack_at = pygame.time.get_ticks()
            self.can_attack = False
