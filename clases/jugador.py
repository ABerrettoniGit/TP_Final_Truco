class Jugador:
    def __init__(self, nombre, es_humano = False):
        self.nombre = nombre
        self.mano = []
        self.puntos = 0

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def mostrar_mano(self):
        return [str(carta) for carta in self.mano]

    def ganar_punto(self, puntos):
        self.puntos += puntos

    def calcular_puntos_envido(self):
        """
        Calcula los puntos de envido en función de las cartas en la mano.
        Devuelve el puntaje más alto que puede obtener.
        """
        puntos = 0
        palos = {}
        for carta in self.mano:
            valor = int(carta.valor) if carta.valor.isdigit() else 0
            if valor > 7:  # 10, 11, 12 no suman en envido
                valor = 0
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(valor)
        
        for palo, valores in palos.items():
            if len(valores) > 1:
                valores.sort(reverse=True)
                puntos = max(puntos, 20 + valores[0] + valores[1])
        
        return puntos

