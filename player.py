from curses import KEY_DOWN
from tkinter.font import families
#from typing_extensions import Self
import pygame
from entity import Entity
from settings import *
from debug import debug


class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
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

        # stats
        self.stats = {'health': 100, 'attack': 10, 'speed': 8}
        self.health = self.stats['health']
        self.speed = self.stats['speed']

         # atack
        self.attack_right_animation = False
        self.attack_left_animation = False
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
            self.get_status()

            # ANIMATIONS CONTROLER-----------------------------        

    def animate(self):
        
        animation = self.sprites[self.status]
        #loop over the frame index
        self.index += self.speed_sprite
        if self.index >= 4:
            print('dans if')
            self.index = 0
        #set the image
        self.image = animation[int(self.index)] 
        print('uwu')   
        

    def update(self):
        self.input()
        self.animate()
        self.move(self.speed)
        #if pygame.time.get_ticks() >= DAY_DURATION:
         #   self.animate()    
        
