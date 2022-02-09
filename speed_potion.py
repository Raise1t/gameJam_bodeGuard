from item import Item

class SpeedPotion(Item):

    def __init__(self, pos, group) -> None:
        super().__init__(pos, group, "Potion of swiftness", False, False)
        self.__speedMultiplier = 1.3
    
    def useItem(self, player):
        player.speed = player.speed * self.__speedMultiplier