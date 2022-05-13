from Dado import Dado
from Jugador import Jugador


RONDAS = 10
NUMERO_DADOS = 5


def mostrar_puntuaciones(jugadores):
    for jugador in jugadores:
        print(f"{jugador.nombre} tiene: {jugador.puntuacion_total} puntos")


def comprobar_escalera(dados):
    numero = 0
    contador_escalera = 0
    dados.sort()
    for dado in dados:
        if dado - numero == 1:
            contador_escalera += 1
        numero = dado
    if contador_escalera == 5:
        return True
    return False


def sumar_puntos(jugador, ronda):
    dados = jugador.dados[ronda]
    puntos = 0
    numero_repetido = 0
    escalera = comprobar_escalera(dados)
    for dado in dados:
        vecesDado = dados.count(dado)
        if vecesDado == 3:
            if numero_repetido != dado:
                puntos += 3
            numero_repetido = dado
        elif vecesDado == 4:
            if numero_repetido != dado:
                puntos += 6
            numero_repetido = dado
        elif vecesDado == 5:
            if numero_repetido != dado:
                puntos += 10
            numero_repetido = dado
    if escalera:
        puntos += 5
    jugador.sumar_puntos(puntos)


def main():
    jugar = True
    mensaje_jugar = "¿Desea jugar? Si/No: "
    while(jugar):
        opcion_menu = input(mensaje_jugar).lower()
        if opcion_menu != "si":
            print("¡Adios!")
            jugar = False
            break

        print("Iniciando partida...")
        jugador1 = Jugador("Máquina")
        jugador2 = Jugador("Humano")
        for ronda in range(RONDAS):
            print(f"::::: Ronda: {ronda+1} :::::")
            dados_ronda_jugador1 = list()
            dados_ronda_jugador2 = list()
            for _ in range(NUMERO_DADOS):
                dados_ronda_jugador1.append(Dado().tirar())
            jugador1.dados.append([dados_ronda_jugador1])
            sumar_puntos(jugador1, ronda)
            print(f"{jugador1.nombre} ha sacado: {dados_ronda_jugador1}")

            tirar_dados = input("¿Tirar dados? ").lower()
            if tirar_dados == "si":
                for _ in range(NUMERO_DADOS):
                    dados_ronda_jugador2.append(Dado().tirar())
                jugador2.dados.append(dados_ronda_jugador2)
                sumar_puntos(jugador2, ronda)
            else:
                jugador2.dados.append([])

            print(f"{jugador2.nombre} ha sacado: {dados_ronda_jugador2}")
            mostrar_puntuaciones((jugador1, jugador2))
            print("---------------------------------")

        mensaje_jugar = "¿Desea volver a jugar? Si/No: "


if __name__ == "__main__":
    main()
