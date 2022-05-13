from Dado import Dado
from Jugador import Jugador


RONDAS = 10
NUMERO_DADOS = 5


def mostrar_puntuacion(jugadores):
    for jugador in jugadores:
        print(f"{jugador.nombre} tiene: {jugador.puntuacion_total} puntos")


def sumar_puntos(jugador, puntos):
    jugador.sumar_puntos(puntos)


def comprobar_puntos(jugador, ronda):
    dados = jugador.dados[ronda]
    puntos = 0
    for dado in dados:
        iguales = list()
        escalera = False
        print(dado)
    return puntos


def main():
    jugar = True
    while(jugar):
        opcion_menu = input("¿Desea Jugar? Si/No: ").lower()
        if opcion_menu != "si":
            print("¡Adios!")
            jugar = False
            break

        print("Iniciando partida...")
        jugador1 = Jugador("Usuario1")
        jugador2 = Jugador("Usuario2")
        for ronda in range(RONDAS):
            print(f"::::: Ronda: {ronda+1} :::::")
            dados_ronda_jugador1 = list()
            dados_ronda_jugador2 = list()
            for _ in range(NUMERO_DADOS):
                dados_ronda_jugador1.append(Dado().tirar())
                dados_ronda_jugador2.append(Dado().tirar())
            jugador1.dados.append(dados_ronda_jugador1)
            jugador2.dados.append(dados_ronda_jugador2)
            print(f"{jugador1.nombre} ha sacado: {dados_ronda_jugador1}")
            print(f"{jugador2.nombre} ha sacado: {dados_ronda_jugador2}")
            mostrar_puntuacion((jugador1, jugador2))
            print("---------------------------------")



if __name__ == "__main__":
    main()
