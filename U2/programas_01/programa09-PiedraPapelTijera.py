## PROGRAMA 9

# Simular juego piedra, papel o tijera (usuario vs máquina)
# 1. Programa debe imprimir opciones para que jugador elija:
#       1. Piedra
#       2. Papel
#       3. Tijera
#       Seleccione una opción (1, 2 o 3):
# 2. Después, eliges num aleatorio (una jugada aleatoria)
# 3. Muestra msg si ha ganado o perdido
# Ten en cuenta que:
#       La piedra gana a la tijera pero pierde contra el papel.
#       El papel gana a la piedra pero pierde contra la tijera.
#       La tijera gana al papel pero pierde contra la piedra. #

import random

print(  "1. Piedra \t" \
        "2. Papel \t" \
        "3. Tijera")
jug1 = int(input("Seleccione una opción (1, 2 o 3): "))

# Num aleatorio de 1 al 3
jug2 = random.randrange(1, 4)
print("Jugador 2: ", jug2)

# piedra > tijera   ->  1 > 3
# piedra < papel    ->  1 < 2
# 
# papel > piedra    ->  2 > 1
# papel < tijera    ->  2 < 3
# 
# tijera > papel    ->  3 > 2
# tijera < piedra   ->  3 < 1

if jug1 > 3:
    print("Número introducido no válido")
else:
    match jug1:
        case 1:
            match jug2:
                case 1:
                    print("Piedra vs piedra: Empate")
                case 2:
                    print("Piedra vs papel: Has perdido")
                case 3:
                    print("Piedra vs tijera: Has ganado")
        case 2:
            match jug2:
                case 1:
                    print("Papel vs piedra : Has ganado")
                case 2:
                    print("Papel vs papel : Empate")
                case 3:
                    print("Papel vs tijera : Has perdido")
        case 3:
            match jug2:
                case 1:
                    print("Tijera vs piedra : Has perdido")
                case 2:
                    print("Tijera vs papel : Has ganado")
                case 3:
                    print("Tijera vs tijera : Empate")