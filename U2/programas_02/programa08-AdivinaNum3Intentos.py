## PROGRAMA 8

# Jugar adivia nº
# Genera nº entre 1 al 20
# Luego va pidiendo nº
#   Y va respondiendo si nº es mayor o menor que la introducida
# Nº aleatorio: random.randrange(1, 21)
# Recuerda importar random al inicio
# Usuario sólo tiene 3 intentos #

import random

intentos = 0
numAle = random.randrange(1, 21)
print("Nº aleatorio: ", numAle)

num = 0
acertar = False

# Se usa and pq si cualquiera de las 2 condiciones falla, bucle se detiene
while intentos < 3 and not acertar:
    num = input("Introduce nº (tienes 3 intentos): ")

    try:
        num = int(num)

        if num == numAle:
            print("Acertaste, felicidades")
            acertar = True
        elif num < numAle:
            print("Incorrecto, es mayor")
            intentos += 1
        else:
            print("Incorrecto, es menor")
            intentos += 1
    except ValueError:
        print("Nº introducido no válido")


if intentos == 3:
    print("Se acabaron los intentos")