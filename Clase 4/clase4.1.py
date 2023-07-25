edad = int(input("Digame su edad: "))
tipo_carnet = input("Digame su tipo de carnet (E para Estudiante \
/P Pensionista /F Familia numerosa /N nada)")
if (edad <= 35 and edad >= 25 and tipo_carnet == "E") or \
    edad < 10 or (edad >= 65 and tipo_carnet == "P") or (tipo_carnet == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento")