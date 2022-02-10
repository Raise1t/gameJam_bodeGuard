import pygame
from settings import *

class Tree1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree1.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)

class Tree_night1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree_night1.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)


class Tree2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree2.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)

class Tree_night2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree_night2.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)


class Tree3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree3.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)

class Tree_night3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tree_night3.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50,-50)


