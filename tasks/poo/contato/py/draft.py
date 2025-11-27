class Fone:
    def __init__(self, id: str , number: str):
        self.__id = id 
        self.__number = number

    def getId(self):
        return self.__id 
    def getNumber(self):
        return self.__number

    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
    def isValid(self) -> bool:
        p = "0123456789()."
        return all((c in p for c in self.__number))

    def __str__(self):
        return f"{self.__id}:{self.__number}"


class Contat:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)

        if fone.isValid():
           self.__fones.append(fone) # print("fail: invalid number")
        if not fone.isValid():
            print("fail: invalid number")
            return 

    def rmFone(self, index: int): 
        if index < 0 or index >= len(self.__fones): 
            print("fail: indice invalido")
        
        self.__fones.pop(index)
    
    def toogleFavorited(self):
        self.__favorited = not self.__favorited



    def __str__(self):
        lista_fones = ", ".join(str(fone) for fone in self.__fones)
        favorite = "@" if self.__favorited else "-"
        return f"{favorite} {self.__name} [{lista_fones}]"

def main():
    ctt = None

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] =="show":
            print(ctt)
        elif args[0] == "init":
            ctt = Contat(args[1])
        elif args[0] == "add":
           id = args[1]
           number = args[2]
           ctt.addFone(id, number)
        elif args[0] == "rm":
            r = int(args[1])
            ctt.rmFone(r)
        elif args[0] == "tfav":
            ctt.toogleFavorited()
        else:
            print("fail: comando invalido! ")

main()