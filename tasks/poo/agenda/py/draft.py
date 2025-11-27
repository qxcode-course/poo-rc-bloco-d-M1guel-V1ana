class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id 
        self.__number = number
    
    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    
    def isValid(self) -> bool:
        p = "123456789()."
        return all(c in p for c in self.__number)
    
    def __str__(self):
        return f"{self.__id} {self.__number}"
