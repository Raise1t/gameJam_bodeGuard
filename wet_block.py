import pygame
from settings import *

class Wet_block(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/wet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)