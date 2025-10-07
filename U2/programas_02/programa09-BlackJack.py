## PROGRAMA 9

# Black Jack
# El ordenador obtiene num aleatorio entre 17 y 21 -> Su puntuación
# Jugador saca cartas (aleatorio pero valor entre 1 y 5)
#   Se irá sumando para obtener puntuación, hasta que él quiera
# Si se pasa de 21 pierde
# Si puntuación igual o menor, pierde
# Si superior, gana #

# jug1 -> Ordenador     jug2 -> Usuario

import random

jug1 = random.randrange(17, 22) #Obtiene nº entre 17 y 21

jug2 = 0
seguir = True
while seguir:
    jug2 += random.randrange(1, 6) #Genera de 1 al 5
    num = int(input("Sumar? Si(1) No(2): "))

    if num == 2:
        seguir = False

print("Su puntuación: ", jug2)
print("Puntuación del ordenador: ", jug1)

if jug2 > jug1 and jug2 < 22:
    print("Ganaste, felicidades")
elif jug2 == jug1:
    print("Empate")
else:
    print("Perdiste")