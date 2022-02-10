import pygame
from item import Item

class SpeedPotion(Item):

    def __init__(self, pos, group) -> None:
        super().__init__(group, "Potion of swiftness", True, False)
        self.image = pygame.image.load('texture/speed_potion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.__speedMultiplier = 1.4
        self._effectDuration = 90000
    
    @property
    def effectDuration(self):
        return self._effectDuration
    
    @effectDuration.setter
    def effectDuration(self, time):
        self._effectDuration = time * 1000
    
    def useItem(self, player):
        if not player.effects['Speed']:
            player.speed = player.speed * self.__speedMultiplier
            player.addEffect('Speed')
            player.removeFromInventory(player.getItemNameFromSlot(player.selectedSlot))
    
    def endEffect(self, player):
        if player.effects['Speed']:
            player.speed = player.speed / self.__speedMultiplier
            player.RemoveEffect('Speed')