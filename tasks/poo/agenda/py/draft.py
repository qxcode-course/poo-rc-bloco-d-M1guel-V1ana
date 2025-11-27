class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id 
        self.__number = number
    
    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    
    def isValid(self) -> bool:
        p = "0123456789()."
        return all(c in p for c in self.__number)
    
    def __str__(self):
        return f"{self.__id} {self.__number}"



class Contat:
    def __init__(self, name: str):
        self.__name = name
        self.__fones:  list[Fone] = []
        self.__favorited: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)

        if fone.isValid():
            self.__fones.append(fone)
        if not fone.isValid():
            print("fail: invalid number")
            return

    
    def rmFone(self, index: int):
        if index < 0 or index >= len(self.__contacts):
            print("fail: indice invalido")
            return
        
        self.__fones.pop(index)

    def toogleFavorited(self) -> bool:
        self.__favorited = not self.__favorited
    
    def isFavorited(self):
        return self.__favorited
    def getFones(self) -> list[Fone]:
        return self.__fones
    def getName(self):
        return self.__name
    def setName(self, name: str):
        self.__name = name
    
    def __str__(self):
        list_fom = ", ".join(str(fone) for fone in self.__fones)
        fav = "@" if self.__favorited else "-"
        return f"{fav} {self.__name} [{list_fom}]"


    
class Agenda:
    def __init__(self):
        self.__contacts: list[Contat] = []


    def findPosByName(self, name: str):

        for i in range (len(self.__contacts)):
            if self.__contacts[i].getName() == name:
                return i
        
        return -1

        
    def addContact(self, name: str, fone: list[Fone]):
        if self.findPosByName(name) != -1:
            print("fail: contato já existe ")
            return
        c = Contat(name)
        for c in fone:
            c.addFone(fone.getId(), fone.getName())

        
        self.__contacts.append(c)

    def __str__(self):
        cotacts = 

            












def main():
    agd = Agenda()


    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agd)
        elif args[0] == "add":
            name = args[1]
            agd.addContact(name, [])
        else:
            print("fail: comando invalido")
        
main()