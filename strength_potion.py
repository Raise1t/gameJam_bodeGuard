from item import Item

class strengthPotion(Item):

    def __init__(self) -> None:
        super().__init__("Strength potion", True, False)
        self.__damageMultiplier = 1.2