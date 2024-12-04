class Jugador:
    def __init__(self, nombre,):
        self.nombre = nombre
        self.mano = []
        self.puntos = 0

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def mostrar_mano(self):
        return [str(carta) for carta in self.mano]

    def ganar_punto(self, puntos):
        self.puntos += puntos
        
        return puntos

