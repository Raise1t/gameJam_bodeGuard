from item import Item

class Pickaxe(Item):

    def __init__(self) -> None:
        super().__init__("pickaxe", False, False)