## PROGRAMA 2

# Pedir nº par y verificar
#   Si no es correcto, avisar
# Si es correcto, pedir impar y verificar
#   Lo mismo

# Los dos pueden ser negativo o positivos#

par = input ("Introduzca nº par: ")

if par == "":
    print("Valor no introducido")
else:
    par = int(par)

    if par % 2 != 0:
        print ("Valor par incorrecto")
    else:
        impar = input("Ahora un impar: ")

        if impar == "":
            print("Valor no introducido")
        else:
            impar = int(impar)

            if impar % 2 == 0:
                print ("Valor impar incorrecto")
            else:
                print("Los dos ( par = ", par, ", impar = ", impar, ") están correctos")
