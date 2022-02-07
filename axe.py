from item import Item

class Axe(Item):

    def __init__(self) -> None:
        super().__init__("Axe", False, False)
        self.__damage = 5