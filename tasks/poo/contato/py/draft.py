class Fone:
    def __init__(self, id: str , number: str):
        self.id = id 
        self.number = number

    def getId(self):
        return self.id 
    def getNumber(self):
        return self.number

    def __str__(self):
        return f"{self.id}:{self.number}"
    
    def isValid(self) -> bool:
        if self.id == "":
            return False
        if not self.number.isdigit():
            return False
        return True

    def __str__(self):
        return f"{self.id}:{self.number}"


class Contat:
    def __init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.favorited: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)

        if not fone.isValid():
            print("fail: invalid number")
            return
        
        self.fones.append(fone)

    def rmFone(self, index: int): 
        if index < 0 or index >= len(self.fones): 
            print("fail: indice invalido")
        
        self.fones.pop(index)



    def __str__(self):
        lista_fones = ", ".join(str(fone) for fone in self.fones)
        return f"- {self.name} [{lista_fones}]"

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
        else:
            print("fail: comando invalido! ")


main()