class Item :
    
    def __init__(self, name, consumable, fuel) -> None:
        self._name = name
        self._consumable = consumable
        self._fuel = fuel
    
    def getName(self):
        return self.name
    
    def isConsumable(self):
        return self.consumable
    
    def isFuel(self) : 
        return self.fuel