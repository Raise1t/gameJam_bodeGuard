from item import Item

class Log(Item):

    def __init__(self) -> None:
        super().__init__("wood log", False, True)
        self.__burnDuration = 100