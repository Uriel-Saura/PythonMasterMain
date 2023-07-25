import random

print("Juego de la mazmorra\n"
      "--------------------\n"
      "Tu y tu comapañero de celda os acabais de escapar de la prision espacion, habeis burlado a los guardias y os\n"
      "dirigis hacia el exterior. Entrais en una mazmora controlada por mounstros alienigenas, uno de los guardisa\n"
      "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira\n"
      "es tu posibilidad de escapar. ¿Hacia donde te diriges?\n\n”"
      "A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo.")

opcion = input("[OPCION (A) - Puerta semiabierta] | [OPCION (B) - Escotilla en el suelo]: ")

if opcion == "A":
    print("Entras en la puerta semiabierta y otro guardia te descubre, que haces?")
    opcion = input("OPCION (A) - Te haces el dormido] | [OPCION (B) - Sales corriendo hacia la siguiente puerta]:")
    if opcion == "A":
        print("El guardia te atrapa, te encierran en una celda de maxima seguridad\nFIN")
    elif opcion == "B":
        print("Despues de esa puerta encuentras una rana mutante que te regala un puñal casero hecho con la pata de"
              "una mesa, lo aceptas?")
        opcion = input("[OPCION (A) - Si] | [OPCION (B) - No]: ")
        if opcion == "A":
            print("Coges el pincho y avanzas, hay dos pasillos circulares, no ves el final de ninguno de los dos, uno esta a la derecha y el otro avanza a la izquierda, cual tomas?")
            opcion = input("OPCION (A) - Izquierda] | [OPCION (B) - Derecha]:")
            