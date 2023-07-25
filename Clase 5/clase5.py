titulo = "Bienvenido al test de quesos"
print(titulo +"\n" + "-"*len(titulo))
puntuacion = 0
opcion = input("""Pregunta 1: Que haces cuando ves uan tabla de quesos
A - Salgo corriendo
B - Pruebo uno de los quesos o incluso varios
C - No puedo evitar devorarla
""")
               
if opcion == "A":
    puntuacion = puntuacion + 0
elif  opcion == "B":
    puntuacion = puntuacion + 5
elif opcion == "C":
    puntuacion = puntuacion + 10
else: 
    print("Las opciones posibles son A,B y C")
    exit()

if puntuacion >= 10:
    print("Te encanta el queso")
elif puntuacion >= 5:
    print("Te gusta el queso")
else:
    print("No te gusta el queso")   