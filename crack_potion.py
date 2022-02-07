from item import Item

class crackPotion(Item):

    def __init__(self) -> None:
        super().__init__("crack potion", True, False)
        self.__damageMultiplier = 0.9