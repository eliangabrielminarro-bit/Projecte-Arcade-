# Aquest fitxer conté la lògica dels jocs (les funcions).
#Joc Numero 1
#Joc Numero 2 
import random

def nana():
    numero_secret= random.randint(1,100)
    intents= 0

    Print("Estic pensant en un número entre 1 i 100. Prova d'endevinar-lo! ")

    while True:
        text = input("Quin número creus que és")

        #Si no és un número enter , mostrem lérror i tornem a preguntar
        try:
            numero