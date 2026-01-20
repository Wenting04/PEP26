# Simular batalla por turnos entre jugador y ordenador
# 1. Jugador comienza con 3 vidas y 0 puntos (ordenador no tiene vida)
# 2. Cada turno
#   a) Muestra vida del jugador
#   b) Jugador elige tipo ataque (condiciona tirada del enemigo)
#       "fuerza": carta entre 5 y 10. El enemigo se defiende mejor (carta entre 3 y 10)
#       "precisión": carta entre 3 y 8. El enemigo tambien estable (carta entre 2 y 9)
#       "riesgo": carta entre 1 y 10. El enemigo se confunde (carta entre 1 y 8)
#   c) Si carta jugador es mayor, gana turno y suma 1 punto
#   d) Si carta enemigo mayor, jugador pierde 1 vida
#   e) Si son igualrs, empate, no se suma ni se pierde
#   f) Juego continúa mientras jugador tenga vidas
#   g) Al terminar, muestra puntuación final
#
# Extra: nvl jugador
#   1. Jugador comienza con 3 vidas, 0 puntos y nvl 1
#   2. Cada 3 puntos, jugador sube de nvl y recupera vida (max 3)
#   3. Al terminar, muestra puntuación final y nvl
#
# No estructura de datos #

import random

vida = 3
puntos = 0
nvl = 0
print("- -- Partida comenzada -- -")
print("Tienes ", vida, " vidas, nivel ", nvl, " y ", puntos, " puntos")

cont = 0

while(vida != 0):
    # Menú
    print("========================================")
    print ("1. Fuerza")
    print ("2. Precisión")
    print ("3. Riesgo")
    ataque = input("Atacar (introduce dígito): ")
    ataque = int(ataque)

    if (ataque == 1):
        jug = random.randrange(5, 11) # Num entre 5 y 10
        ord = random.randrange(3, 11) # Num entre 3 y 10
    elif (ataque == 2):
        jug = random.randrange(3, 9) # Num entre 3 y 8
        ord = random.randrange(2, 10) # Num entre 2 y 9
    elif (ataque == 3):
        jug = random.randrange(1, 11) # Num entre 1 y 10
        ord = random.randrange(1, 9) # Num entre 1 y 8
    else:
        print("Ataque introducido inválido")

    if (ataque > 0 and ataque < 4):
        print("---------------------------------------")
        print("Jugador: ", jug)
        print("Enemigo: ", ord)
        if ( jug > ord):
            puntos += 1
            print("+ 1 punto")

            cont += 1
            if ( cont == 3 ):
                cont = 0
                nvl += 1
                if ( vida < 3 ):
                    vida += 1
                print("+ 1 nivel")
                print("+ 1 vida")
        elif ( jug < ord ):
            vida -= 1
            print("- 1 vida")

print("========================================")
print("Juego finalizado")
print("Usted ha alcanzado el nivel ", nvl, " con ", puntos, " puntos")
print("========================================")