import random

numero = random.randint(1,10)

print("\nFinal Boss - Levantarse una mañana")
print("----------------------------------\n")
print("Eres un estudiante universitario que generalmente se queda en la madrugada jugando a videojuegos, pero al dia siguiente tiene clases a las 7:00 am. Al terminar de jugar alrededor de las 3:00am pone una alarma para intentar levantarse e ir a la universidad. ¿Pero realmente podra hacerlo?")
print("El tiempo pasa y se acerca la hora de despertar, que haces?\n")
opcion = input("[OPCION (A) - Escuchas la alarma y te levantas] | [OPCION (B) - La ignoras y sigues durmiendo]: ")
if opcion == "A":
    print("Te levantas y intentas detener la alarma, para quitarla debes resolver una operacion matematica")
    print("Tienes que resolver la siguiente operacion")
    operacion = int(input("(3 * {}) + 5 = ".format(numero)))
    resulatdo = ((3*numero)+5)
    if operacion == resulatdo:
        print("Haz detenido la alarma")
        print("Vez la hora y dices que tienes que irte, quieres llevar el movil?")
        opcion = input("[OPCION (A) - Si] | [OPCION (B) - No]: ")
        if opcion == "A":
            print("Sales con el movil y vas a la universidad tomas clases normal sales a las 2:00pm de regreso a casa te detiene un delicuente pidiendote el telefono")
            opcion = input("[OPCION (A) - Se lo das] | [OPCION (B) - No se lo das]: ")
            if opcion == "A":
                print("El dilecuente toma el telefono y se va. Despues de ver que se fue, terminas corrinedo a casa para descansa del dia.\nFin")
            elif opcion == "B":
                print("El dilecuente ve el telefono procede a dispararte, toma el telefono y se va. Mueres y no podras ir a descansar a casa.\nFin")
            else: 
                 print("Haz ingresado una opcion no valida")
                 exit()  
        elif opcion == "B":
            print("Sales sin el movil y vas a la universidad tomas clases normal sales a las 2:00pm de regreso a casa te detiene un delicuente pidiendote el telefono") 
            print("Al no tener telefono el delicuente te dispara por no poder robarte, ya no podras llevar a descansar en casa.\nFin")
        else: 
            print("Haz ingresado una opcion no valida")
            exit() 
    else:
        print("No podiste detener la alarma, por el enojo tiras el movil contra la pared por lo cual se rompe y sales sin movil hacia la universidad")
        print("Tomas clases normal sales a las 2:00pm de regreso a casa te detiene un delicuente pidiendote el telefono")
        print("Al no tener telefono el delicuente te dispara por no poder robarte, ya no podras llevar a descansar en casa.\nFin")
elif opcion == "B":
    print("Te quedas dormido y no vas a la universidad.")
else:
    print("Haz ingresado una opcion no valida")
    exit()    

