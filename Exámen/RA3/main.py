# 2 módulos: batalla de magia
# Cada módulo debe contener 2 funciones y programa principal los usará
# 1. Crear carpeta "batalla" con módulo "jugador" y "enemigo"
# 4. main:
#       Pide jugador el nombre, conocimiento (entre 1 y 10) y energía vital (entre 1 y 5)
#       Genera enemigo aleatorio
#       Realiza comabte de 3 rondas con:
#           Cada ronda ambos atacan (se calcula su nvl de magia)
#           El que tenga menor nvl pierde 1 punto de energía. Si empatan, ninguno pierde
#           Se muestra resultado de ronda
#       Al final, muestra quien gana (el que tenga más energía) o si hay empate
# 5. Crea un entorno virtual en Python para ejecutar el programa #
from batalla import jugador
from batalla import enemigo

print("============================================")
print(" - -- Introducir datos -- - ")
jug = input("Nombre del jugador: ")
conocJug = 0
enerJug = 0

# Bucle repite si conocJug menor de 1 y mayor de 10, y, enerJug menor de 1 y mayor de 5
while ( (conocJug < 1 or conocJug > 10) or (enerJug < 1 or enerJug > 5) ):
    conocJug = input("Conocimiento del jugador (entre 1 - 10): ")
    enerJug = input("Energía del jugador (entre 1 - 5): ")
    try:
        conocJug = int(conocJug)
        enerJug = int(enerJug)

        if ((conocJug < 1 or conocJug > 10) or (enerJug < 1 or enerJug > 5)):
            print("Datos incorrectos")

    except (ValueError):
        print("Valores no numéricos introducidos")
        conocJug = 0
        enerJug = 0

print()
print(" - -- Jugador generado -- -")
jugador.mostrar_jugador(jug, conocJug, enerJug)


print("--------------------------------------------")

print("Generando enemigo...")
ene, conocEne, enerEne = enemigo.generar_enemigo()
print()
print(" - -- Enemigo generado -- -")
jugador.mostrar_jugador(ene, conocEne, enerEne)

print()
print("============================================")
for x in range(3): # Empieza por 0 y termina en 2
    print("--------------------------------------------")
    ataqJug = jugador.ataque_jugador(conocJug, enerJug)
    print("Jugador ataca: ", ataqJug)

    ataqEne = enemigo.ataque_enemigo(conocEne, enerEne)
    print("Enemigo ataca: ", ataqEne)

    if ( ataqJug > ataqEne ):
        enerEne -= 1
    elif ( ataqJug < ataqEne ):
        enerJug -= 1

print("--------------------------------------------")
print("============================================")

if ( enerJug > enerEne ):
    print("Gana ", jug, " con ", enerJug, " de energía")
    print("Pierde ", ene, " con ", enerEne, " de energía")
elif ( enerJug < enerEne ):
    print("Gana ", ene, " con ", enerEne, " de energía")
    print("Pierde ", jug , " con ", enerJug , " de energía")
else:
    print("Empatados")
    print("Energía ", enerJug)

print("============================================")