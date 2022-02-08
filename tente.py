import pygame
from settings import *

class Tente(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/tente.png').convert_alpha()
        #pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        