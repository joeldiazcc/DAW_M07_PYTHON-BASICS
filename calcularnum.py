from random import randrange
from random import random

nUser = int(input("Adivina en que número estoy pensando de 1-100, tienes 5 intentos: "))
nRandom = randrange(100)
intentos = 5
print(nRandom)

while intentos > 0 and nUser != nRandom: 


    if nUser > nRandom:

        print("Menos")
        intentos -= 1

        nUser = int(input("Adivina en que número estoy pensando de 1-100, tienes 5 intentos: "))

    elif nUser < nRandom:

        print("Más")
        intentos -= 1

        nUser = int(input("Adivina en que número estoy pensando de 1-100, tienes 5 intentos: "))

    elif nUser == nRandom:
        break

if nUser == nRandom:

    print("¡Felicidades lo has adivinado!")

            


