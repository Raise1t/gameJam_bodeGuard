class Item :
    
    def __init__(self, name, consumable, fuel) -> None:
        self.__name = name
        self.__consumable = consumable
        self.__fuel = fuel
    
    def getName(self):
        return self.name
    
    def isConsumable(self):
        return self.consumable
    
    def isFuel(self) : 
        return self.fuel