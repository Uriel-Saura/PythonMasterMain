print("Voy a la cocina")
print("Abre la nevera")
leche = input("¿Hay leche? (S/N) ")
if leche == "S":
    print("Sacamos la leche de la nevera")
    colaco = input("¿Tenemos colaco? (S/N) ")
    if colaco == "S":
        print("Sacamos el colaco")
        print("Ponemos la leche en el vaso")
        print("Ponemos el colaco en el vaso")
        print("Mezclamos")
    else :
        print("No hay colaco")  
        print("Voy a comprar al super...")  
else:
    print("No hay leche")
    print("Voy a comprar al super...")  
