from sqlalchemy import false, true


from item import Item

class DeadBranch(Item) :

    def __init__(self) -> None :
        super().__init__("Dead branch", False, True)
        self.__burnDuration = 50