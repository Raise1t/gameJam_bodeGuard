class player:

    def __init__(self, name, skin) -> None :
        self.__name = name
        self.__health = 100
        self.__food = 100
        self.__inventory = {}
        self.__skin = ""