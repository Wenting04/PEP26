# 2. Jugador:
#       ataque_jugador (conocimiento, energía): devuelve nvl de magia del jugador calculando como (conocimiento*energía)*numAleatorio entre 1 y 3
#       mostrar_jugador(nombre, conocimiento, energía): mostrar pantalla valores actuales del jugador

import random

def ataque_jugador(conocimiento, energia):
    return ( conocimiento*energia )*( random.randrange(1, 4) )

def mostrar_jugador(nombre, conocimiento, energia):
    print("Nombre: ", nombre)
    print("Conocimiento: ", conocimiento)
    print("Energia: ", energia)