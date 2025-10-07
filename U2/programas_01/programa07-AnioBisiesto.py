## PROGRAMA 7

# Pedir un año
# Decir si es bisiesto o no
#   Bisiesto: si es múltiplo de 4 pero no múltiplo de 100
#   Aunque los múltiplosd e 400 sí lo son

# Es decir, si num se divide entre 4 o 400, de resto debe ser 0
# Ahora dividirlo entre 100, debería de tener de resto cualquier num excepto 0 #

num = input("Introduce año: ")

if num == "":
    print("Valor no introducido")
else:
    num = int(num)

    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print("El año ", num, " es bisiesto")
    else:
        print("El año ", num, " no es bisiesto")