class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.nombre = f"{valor} de {palo}"

    def __str__(self):
        return self.nombre
    
    def __eq__(self, other):
        if isinstance(other, Carta):
            return self.valor == other.valor and self.palo == other.palo
        return False