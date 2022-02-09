import pygame
from settings import *

class Grass_block(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/grass.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def __del__(self):
         pass

class Grass_block_night(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/grass_night.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        