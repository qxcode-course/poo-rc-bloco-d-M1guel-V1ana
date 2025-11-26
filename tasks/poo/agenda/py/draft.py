class Fone:
    def __init__(self, id: str, numero: int):
        self.id = id 
        self.numero = numero

    def getId(self):
        return self.id 
    def getNumero(self):
        return self.numero
    
    def __str__(self):
        return f"{self.id}:{self.nome}"
    


class Contato:
    def __init__(self, nome: str):
        self.nome = nome 
        self.fone = list[Fone] = []
