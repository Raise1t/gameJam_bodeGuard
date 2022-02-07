from item import Item

class Rock(Item) :
    def __init__(self) -> None:
        super().__init__("rock", False, False)