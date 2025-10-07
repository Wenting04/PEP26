## PROGRAMA 7

# Pedir nº hasta que introduzca 0
# Luego hacer suma y media de todo los introducidos
# Hacer 2 versiones: usar break y otra no #

# No he hecho que controle por si introduce algo no numérico

print("Sin break")

num = ""
suma = 0
cont = 0

while num != "0":
    num = input("Introduce números (0 para salida): ")

    if num != "0":
        suma += int(num)
        cont += 1

if cont != 0:
    print("La suma de todos los nº introducidos es: ", suma)
    print("La media es de: ", suma/cont)
else:
    print("Salida sin valores introducidos")


print("Con break")

suma = 0
cont = 0

while True:
    num = input("Introduce números (0 para salida): ")

    if num == "0":
        break
    else:
        suma += int(num)
        cont += 1

if cont != 0:
    print("La suma de todos los nº introducidos es: ", suma)
    print("La media es de: ", suma/cont)
else:
    print("Salida sin valores introducidos")
