## PROGRAMA 8

# Simular juego entre 2 jugadores tirando 2 dados
# El que saque puntuación total mayor, gana
# Si coincide, gana el que sacó un nº mayor
# Si nº mayor tmb coincide, empatan

# Tips:
#   Podemos pedir por pantalla o 
#   usar función random.randrange(1,7)
#   Para num entre 1 y 6
#   Hay que importar random al inicio del programa #

import random

# Puedo crear 2 arrays para almacenar los 2 dados lanzados
print("Jugador 1 está lanzando dados...")
user1 = [random.randrange(1,7), random.randrange(1,7)]
print("Dados del jug 1: ", user1[0], user1[1])

print("Jugador 2 está lanzando dados...")
user2 = [random.randrange(1,7), random.randrange(1,7)]
print("Dados del jug 2: ", user2[0], user2[1])

#Podemos tmb usar sum(user1) para sumar todo el contenido del array
total1 = user1[0] + user1[1]
total2 = user2[0] + user2[1]

if total1 > total2:
    print("Jugador 1 ha ganado")
elif total1 < total2:
    print("Jugador 2 ha ganado")
else:

    #Para sacar el valor más alto, podemos usar max(user1) en vez de todo el siguiente if
    if user1[0] > user1[1]:
        num1 = user1[0]
    else:
        num1 = user1[1]

    if user2[0] > user2[1]:
        num2 = user2[0]
    else:
        num2 = user2[1]

    if num1 == num2:
        print("Empate")
    elif num1 > num2:
        print("Jugador 1 ha ganado")
    else:
        print("Jugador 2 ha ganado")