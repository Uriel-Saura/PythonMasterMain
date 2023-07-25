respuesta = None

while respuesta != "A" or "B" or "C":
    respuesta = input("¿Que opcion prefieres [A,B,C]?")
    if respuesta == "A":
        print("Has elegido bine")
    elif respuesta == "B":
        print("Podrias elegir mejor")
    elif respuesta == "C":
        print("Elegiste mal")
    else:
        print("No me has dado una respuesta con sentido")