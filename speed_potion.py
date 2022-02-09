from item import Item

class SpeedPotion(Item):

    def __init__(self, pos, group) -> None:
        super().__init__(pos, group, "Potion of swiftness", False, False)
        self.__speedMultiplier = 1.5
    
    def useItem(self, player):
        if not player.effects['Speed']:
            player.speed = player.speed * self.__speedMultiplier
            player.addEffect('Speed')
            player.removeFromInventory(player.getItemNameFromSlot(player.selectedSlot))