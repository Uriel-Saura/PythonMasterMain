import random
numero = random.randint(1,10)
intento  = int(input("Elige un numero: "))
if numero == intento:
    print("Has ganado!")
else:
    print("El numero ganador era: {}".format(numero))