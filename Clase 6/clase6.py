dolarEuro = 0.89
dolarLibra = 0.76
opcion = input("Escoga su divisa (E para euro, L para libra) ")
cantidad = float(input("Cuantos dolares desea cambiar "))
if opcion == "E":
    cambio = cantidad * dolarEuro
    print("La cantidad de euros al cambio son: ",cambio)
elif opcion == "L":
    cambio = cantidad * dolarLibra
    print("La cantidad de libras al cambio son: ",cambio)
else:
    print("No escogio una divisa valida")   
