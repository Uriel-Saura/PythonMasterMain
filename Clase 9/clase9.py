import random

vida_pikachu = 80
vida_incial_pikachu = 80
bola_voltio = 10
onda_trueno = 11

vida_squartle = 90
vida_incial_squartle = 90
placaje = 10
pistola_agua = 12
burbuja = 9

divisor = 0

ataque_pikachu = random.randint(1,2)

while vida_pikachu > 0 and vida_squartle > 0:

    print("Turno de pikachu")
    if ataque_pikachu == '1':
        print("Pikachu ataca con bola voltio")
        vida_squartle -= 10
    else : 
        print("Pikachu ataca con onda trueno")
        vida_squartle -= 11

    divisor = vida_incial_pikachu % 10 
    print("La vida de pikachu es {} y la vida de Squartle es {}".format(vida_pikachu,vida_squartle))
    input("Enter para cuantinar")

    print("Turno Squartle")
    ataque_squartle = None
    while ataque_squartle != "P" and ataque_squartle != "A" and ataque_squartle != "B":
        ataque_squartle = input("¿Que ataque deceas realizaf? [P]lacaje. Pistola[A]gua, [B]urbuja: ")
        if ataque_squartle == "P":
            print("Squartle uso placaje")
            vida_pikachu -= 10 
        elif ataque_squartle == "A":
            print("Squartle uso pistola agua")
            vida_pikachu -= 12 
        elif ataque_squartle == "B":
            print("Squartle uso burbuja") 
            vida_pikachu -= 9
        else:
            print("Ingresa una opcion valida")    
        print("La vida de pikachu es {} y la vida de Squartle es {}".format(vida_pikachu,vida_squartle))
        input("Enter para cuantinar")

if vida_pikachu > vida_squartle:
    print("El ganador es Pikachu")
else:
    print("El ganador es Squartle")