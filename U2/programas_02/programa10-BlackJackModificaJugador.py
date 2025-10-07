## PROGRAMA 10

# Lo mismo que en programa 9 pero pueda modificar nº de jugadores #
import random

numJug = int(input("Cantidad de jugadores: "))

print("Recuerde, jugador 1 - Ordenador")
jug1 = random.randrange(17, 22) #Obtiene nº entre 17 y 21

for i in range(2, numJug + 1):

    print("Turno del jugador ", i)
    jug = 0
    seguir = True
    while seguir:
        num = int(input("Sumar? Si(1) No(2): "))

        if num == 2:
            seguir = False
        else:
            jug += random.randrange(1, 6) #Genera de 1 al 5

    print("Su puntuación: ", jug)
    print("Puntuación del ordenador: ", jug1)

    if jug > jug1 and jug < 22:
        print("Ganaste, felicidades")
    elif jug == jug1:
        print("Empate")
    else:
        print("Perdiste")