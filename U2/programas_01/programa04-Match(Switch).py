## PROGRAMA 4

# Pedir al usuario nº real (float) entre 1 al 10
#   Simular que es una nota numérica
# Imprimir calificación dependiendo de si:
#   Insuficiente: [0, 5)
#   suficiente: [5, 6) 
#   Bien: [6, 7)
#   Notable: [7, 9)
#   Sobresaliente: [9, 10]
# Si num introducido no está en el rango,
#   imprimir error e indicar nota no válida
# Hay que usar match #

num = input("Introduzca su calificación: ")

if num == "":
    print("Vacío")
else:
    num = float(num)

    # | --> or
    match num:
        case 0 | 1 | 2 | 3 | 4:
            print("Insuficiente")
        case 5:
            print("Suficiente")
        case 6:
            print("Bien")
        case 7 | 8:
            print("Notable")
        case 9 | 10:
            print("Sobresaleinte")
        case _:
            print("Nota no válida")