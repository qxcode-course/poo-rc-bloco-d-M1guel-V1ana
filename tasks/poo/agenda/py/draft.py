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
    
    def isValid(self) -> bool:
        fone = Fone 
        if not self.id or self.numero:
            return False
        if any(c.isalpha() for c in self.numero):
            return False
        return True
class 