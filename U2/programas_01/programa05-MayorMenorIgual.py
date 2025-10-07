## PROGRAMA 5

# Pedir 2 nº
# Indicar cuál menor y cuál mayor o si son iguales #

num1 = input("Introduzca el 1º nº para comparar: ")
num2 = input("Introduzca el 2º nº para comparar: ")

if num1 == "" and num2 == "":
    print("Valor del 1º y 2º están vacías")
else:
    if num1 == "":
        print("Valor del 1º está vacía")
    elif num2 == "":
        print("Valor del 2º está vacía")
    else:
        num1 = float(num1)
        num2 = float(num2)

        if num1 == num2:
            print(num1, " es igual que ", num2)
        elif num1 < num2:
            print(num1, " es menor que ", num2)
        elif num2 < num1:
            print(num1, " es mayor que ", num2)