#class player:

    #def __init__(self, name, skin):
    #    self.__name = name
    #    self.__health = 100
    #    self.__food = 100
    #    self.__inventory = {}
    #    self.__skin = ""
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)