## PROGRAMA 5

# Pedir un nº y mostrar lista de nº desde 1 al nº
# Se debe controlar que nº sea mayor que 1 y menor que 10
#   Si es así, se pide de nuevo #

repetir = True

while repetir:
    num = input("Introduzca un nº del 1 al 10: ")

    try:
        num = int(num)

        if 1 <= num and num <= 10:
            for i in range (1, num + 1):
                print(i)

            repetir = False #Para dejar de repetir
        else:
            print("Valor fuera de rango")
    except ValueError:
        print("Valor no numérico")

print("Completado")