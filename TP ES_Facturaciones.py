print("Bienvenido/a al departamento de facturación")
print("A")
print("A continuación se le pedirá 3 precios de los cuales se realizará una suma, dando el resultado total")
Precio1 = int(input("Ingrese primer precio: "))
Precio2 = int(input("Ingrese segundo precio: "))
Precio3 = int(input("Ingrese tercer precio: "))
sumadeprecios = "La suma de los precios especificados es de " + str((Precio1 + Precio2 + Precio3))
print(sumadeprecios)
print("B")
print("A continuación se le pedirá 3 precios de los cuales se realizará un promedio")
Precio1b = int(input("Ingrese primer precio: "))
Precio2b = int(input("Ingrese segundo precio: "))
Precio3b = int(input("Ingrese tercer precio: "))
promediodeprecios = "El promedio entre los 3 precios especificados tiene un valor de " + str((Precio1b+Precio2b+Precio3b)/3)
print(promediodeprecios)
print("C")
print("A continuación se le pedirá 3 precios, los cuales se sumarán, agregando el porcentaje de IVA(21%)")
Precio1c = int(input("Ingrese primer precio: "))
Precio2c = int(input("Ingrese segundo precio: "))
Precio3c = int(input("Ingrese tercer precio: "))
tasadeiva = float(0.21)
Preciototal = (Precio1c + Precio2c + Precio3c)
iva = Preciototal * tasadeiva
Preciototal_iva = Preciototal + iva
print("El total más el IVA es de " +str(Preciototal_iva) )
