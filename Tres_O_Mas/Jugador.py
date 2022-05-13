


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dados = list()
        self.puntuacion_total = 0


    def sumar_puntos(self, puntos):
        self.puntuacion_total += puntos
