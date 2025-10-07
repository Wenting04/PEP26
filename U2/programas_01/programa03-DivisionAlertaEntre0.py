## PROGRAMA 3

# Pedir 2 nº y mostrar división
# Tener en cuanta que no se divide entre 0 --> Avisar #

print("Divisor/dividendo = Cociente")

num1 = input("Introduzca el 1º nº (dividendo): ")
num2 = input("Introduzca el 2º nº (divisor): ")

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

        if num2 == 0 :
            print("No es posible dividir entre 0")
        else:
            print(num1, " / ", num2, " = ", num1/num2)




    