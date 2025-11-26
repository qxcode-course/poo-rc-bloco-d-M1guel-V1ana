class Fone:
    def __init__(self, id: str, number: int):
        self.id = id 
        self.number = number

    def getId(self):
        return self.id 
    def getNumber(self):
        return self.number

    def __str__(self):
        return f"{self.id}:{self.number}"
    
    def isValid(self) -> bool:
        fone = fone
        if not self.id or self.number:
            return False
        if any(c.isalpha() for c in self.number):
            return False
        
    def __str__(self):
        return f"{self.id}:{self.number}"


class Contat:
    def __init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.favorited: bool = False

    def addFone(self, id: str, number:int):
        if self.fone is None:
            print("fail: lista de telefones vazia")


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
            name: 
        else:
            print("fail: comando invalido! ")


main()