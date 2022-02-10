import pygame
from item import Item

class CrackPotion(Item):

    def __init__(self, pos, group) -> None:
        super().__init__(group, "Potion of crack", True, False)
        self.image = pygame.image.load('texture/crack_potion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.__damageMultiplier = 0.6
        self._startTime = 0
        self._effectDuration = 10000
    
    @property
    def effectDuration(self):
        return self._effectDuration
    
    @effectDuration.setter
    def effectDuration(self, time):
        self._effectDuration = time * 1000

    @property
    def startTime(self):
        return self._startTime
    
    def useItem(self, player, startTime):
        if not player.effects['Crack']:
            self._startTime = startTime
            player.setArmor(self.__damageMultiplier)
            player.addEffect('Crack', self)
            player.removeFromInventory(player.getItemNameFromSlot(player.selectedSlot))

    def endEffect(self, player):
        if player.effects['Crack']:
            player.setArmor(1)
            player.removeEffect('Crack')