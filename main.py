#  és el menú principal i el bucle de l'aplicació.
from jocs import janken, nana

while True:

    print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, paper, Tisora")
    print("2. Jugar a Endevinar el Numeró")
    print("S. Sortir")

    opcio = input("Escull una opció: ")

    if opcio == "1":
        janken()

    elif opcio == "2":
       nana()

    elif opcio == "S":
        print("Gràcies per jugar! Fins aviat!")
        break

else:
    print("Opció incorrecta. Torna-ho a provar .")

