## PROGRAMA 6

# 1. Pide nº entre 1 al 10 y se vuelve a pedir hasta que introduzca bien
# 2. Después se muestra tabla de multiplicar
# 3. Preguntar al usuario si quiere introducir otro nº #

repetir = True

while repetir:
    num = input("Introduzca entre 1 al 10: ")

    try:
        num = int(num)

        if 1 <= num <= 10:
            for i in range(1, num + 1):
                print(num, " x ", i, " = ", num*i)

            rep = input("¿Quieres repetir? Si(1) No (2): ")
            if rep == 1:
                repetir = True
            else:
                repetir = False
        else:
            print("Valor incorrecto, dentro del rango 1 al 10")
    
    except ValueError:
        print("Valor incorrecto")