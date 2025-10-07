## PROGRAMA 1

# Que pida 1º un nº par, y luego impar (positivos o negativos)
# Si uno de los dos no es correcto (tipo, par cuando impar, etc) -> Muestre aviso#

par = input("Introduzca un nº par: ")
impar = input("Ahora un nº impar: ")

if (par == "") and (impar == ""):
    print("Ningún valor introducido")
else:
    par = int(par)
    impar = int(impar)

    if (par % 2 != 0) and (impar % 2 == 0):
        print("El 1º (", par, ") no es par y el segundo (", impar, ") no es impar")
    elif (par % 2 != 0):
        print("El 1º (", par, ") no es par")
    elif (impar % 2 == 0):
        print("El 2º (", impar, ") no es impar")
    else:
        print("Los dos ( par = ", par, ", impar = ", impar, ") están correctos")