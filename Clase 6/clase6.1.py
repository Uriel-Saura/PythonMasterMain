ios_android = input("Cual sistema te gusta mas \
                    A - Android \
                    B - iOS")
if ios_android == "A":
    dinero = input("Tienes dinero \
                   S - Si \
                   N - No")
    if dinero == "S":
        camara = input("Te importa la camara del movil \
                       S - Si \
                       N - No")
        if camara == "S":
            print("Comprate el Google Pixel Supercamara")
        elif camara == "N":
            print("Android calidad-precio")
        else:
            print("No ha escogido una opcion valida")
            exit()
    elif dinero == "N":
        print("Andriod chino 100 dolares")
    else:
            print("No ha escogido una opcion valida")
            exit()
elif ios_android == "B":
     dinero = input("Tienes dinero \
                   S - Si \
                   N - No")
     if dinero == "S":
        print("Iphone Ultra Pro Max")
     elif dinero == "N":
         print("iPhone de segunda mano")
     else:
        print("No ha introduzido una opcion valida")
        exit();     
else:
    print("No ha introduzido una opcion valida")
    exit();    