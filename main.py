#  és el menú principal i el bucle de l'aplicació.
from jocs import janken, nana
print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
print("1. Jugar a Pedra, paper, Tisora")
print("2. Jugar a Endevinar el Numeró")
print("3. Sortir")

opcio = input("Escull una opció: ").upper()

if opcio == "1":
    janken()
elif opcio == "2":
    nana()
elif opcio == "3":
    print("Gràcies per jugar! Fins aviat!")

else:
       print("Opció incorrecta. Torna-ho a provar .")
    