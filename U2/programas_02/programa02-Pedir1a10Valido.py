## PROGRAMA 2

# Pedir al usuario un nº entre 1 al 10
# Repetir hasta que datos sean válidos #

#Por ahora es false, va a repetir hasta meter correcto
correcto = False

#Se repite mientras correcto sea false
while not correcto:
    num = input("Introduzca nº entre 1 al 10: ")

    if num == "":
        print("Valo no introducido")
    else:
        try:
            num = int(num)
            if 1 <= num and num <= 10:
                correcto = True
                print("Correcto")
            else:
                print("Valores fuera de rango")
        except ValueError:
            print("Valor no numérico")