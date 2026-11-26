# Aquest fitxer conté la lògica dels jocs (les funcions).
import random
from robot import robot
#Joc Numero 1 (Pedra paper i tissora)

def janken():
    maquina = robot()
    jugador = 0
    ordenador = 0
    rondes = 0

    print("\n--- PEDRA, PAPER, TISORA ---")
    print("1. El primer que arribi a 3 victories")
    print("2. Al millor de 5 rondes")

    modo = input("Escull una opció: ")

    while modo not in ["1", "2"]:
        print("Opció incorrecta!")
        modo = input("Escull una opció")

    while jugador < 3 and ordenador < 3 and (modo == "1" or rondes < 5):

        print("\n--- RONDA NOVA ---")
        
        jugada = input("Escriu la teva Jugada:").lower()

        while jugada not in ["pedra", "paper", "tisora"]:
            print("Jugada incorrecta!")
            jugada =input("Torna a jugar: ").lower()

        jugada_robot = maquina.playing()
        print("Tu:", jugada_robot)
        print("Robot:", jugada_robot)

        if jugada == jugada_robot:
            print("Empat")

        elif (jugada == "pedra" and jugada_robot == "tisora") or \
             (jugada == "paper" and jugada_robot == "pedra") or \
             (jugada == "tisora" and jugada_robot == "paper"):
             print("Has guanyat aquesta ronda!")
             jugador += 1
        else:
            print("El robot guanya aquesta ronda!")
            ordenador += 1
            rondes += 1

        print("Marcador:", jugador, "-", ordenador)

    if jugador > ordenador:
        print("\nHas guanyat la partida!")

    elif ordenador > jugador:
        print("\nEl robot guanya la partida...")

    else:
        print("\nLa partida ha acabat en empat!")             
#Joc Numero 2 (Endevina el Numeró)
def nana():
     numero = random.randint(1, 100)
     intents = 0

     print("\n--- ENDEVINA EL NÚMERO ---")

     while True:

        resposta = int(input("Endevina el número (1-100): "))
        intents += 1

        if resposta > numero:
            print("Massa alt!")

        elif resposta < numero:
            print("Massa baix!")

        else:
            print("Felicitats! Has encertat!")
            print("Nombre d'intents:", intents)
            break