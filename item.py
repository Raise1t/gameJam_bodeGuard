import pygame

class Item(pygame.sprite.Sprite):

    items = {}
    
    def __init__(self, pos, group, name, consumable, fuel) -> None:
        super().__init__(group)
        self.image = pygame.image.load('texture/speed_potion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self._name = name
        self._consumable = consumable
        self._fuel = fuel
        Item.items[self._name] = self
    
    def getImage(self):
        return self.image
    
    def getName(self):
        return self._name
    
    def isConsumable(self):
        return self._consumable
    
    def isFuel(self) : 
        return self._fuel