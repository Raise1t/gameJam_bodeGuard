from sqlalchemy import false
from item import Item

class Iron(Item) :

    def __init__(self) -> None:
        super().__init__("iron", False, False)