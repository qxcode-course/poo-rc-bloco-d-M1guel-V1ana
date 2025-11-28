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
        return f"{self.__id}:{self.__number}"



class Contat:
    def __init__(self, name: str):
        self.__name = name
        self.__fones:  list[Fone] = []
        self.__favorited: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)

        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: invalid number")

    
    def rmFone(self, index: int):
        if index < 0 or index >= len(self.__fones):
            print("fail: indice invalido")
            return
        
        self.__fones.pop(index)

    def toogleFavorited(self) -> bool:
        self.__favorited = not self.__favorited
        return self.__favorited
    
    def isFavorited(self):
        return self.__favorited
    def getFones(self) -> list[Fone]:
        return self.__fones
    def getName(self):
        return self.__name
    def setName(self, name: str):
        self.__name = name
    
    def __str__(self):
         p = "@" if self.__favorited else "-"
         names_ctt = ", ".join(str(fone) for fone in self.__fones)
         return f"{p} {self.__name} [{names_ctt}]"


    
class Agenda:
    def __init__(self):
        self.__contacts: list[Contat] = []

    def getContacts(self) -> list[Contat]:
        return self.__contacts

    def findByName(self, name: str) -> int:
        name = name.lower()

        for i in range(len(self.__contacts)):
            if self.__contacts[i].getName().lower() == name:
                return i
        return -1

    def getContact(self, name: str):
        pos = self.findByName(name)

        if pos == -1:
            return None
        return self.__contacts[pos]

    def addContact(self, name: str):
        if self.findByName(name) != -1:
            print("fail: contato já existe")
            return

        self.__contacts.append(Contat(name))

    def rmContact(self, name: str) -> bool:
        pos = self.findByName(name)

        if pos == -1:
            print("fail: contato não encontrado")
            return False
        self.__contacts.pop(pos)
        return True

    def __str__(self):
        order = sorted(self.__contacts, key=lambda c: c.getName().lower())
        return "\n".join(str(contato) for contato in order)


def main():

    agd = Agenda()

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agd)
        elif args[0] == "add":
            name = args[1]
            contato = agd.getContact(name)
            if contato is None:
                agd.addContact(name)
                contato = agd.getContact(name)

            for token in args[2:]:
                op, num = token.split(":")
                contato.addFone(op, num)



main()