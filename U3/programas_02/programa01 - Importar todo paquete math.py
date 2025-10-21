## PROGRAMA 1

# Importar math completo y preguntar al usuario qué hacer
# 1. Seno de un ángulo
# 2. Coseno de ángulo
# 3. Raíz cuadrada de un num
# 4. Potencia de dos num #

import math

def menu():
    print("- -- Menú -- -")
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un num")
    print("4. Potencia de dos num")

def seno():
    angulo = float(input("Introduce ángulo en grados: "))
    radianes = math.radians(angulo) #Convertir a radianes
    result = math.sin(radianes)
    print("El seno de", angulo, "es: ", result)

def coseno():
    angulo = float(input("Introduce ángulo en grados: "))
    radianes = math.radians(angulo) #Convertir a radianes
    result = math.cos(radianes)
    print("El coseno de", angulo, "es: ", result)

def raizCuadrada():
    num = float(input("Introduce num: "))

    if num < 0:
        print("Num no válido")
    else:
        result = math.sqrt(num)
        print("La raíz cuadrada de ", num, "es: ", result)

def potencia():
    base = float(input("Introduce base: "))
    exponente = float(input("Introduce exponente: "))
    result = math.pow(base, exponente)
    print(base, "elevado a", exponente, "es: ", result)


def main():
    menu()
    opcion = input("Elige una opción (1-4): ")

    match opcion:
        case "1":
            seno()
        case "2":
            coseno()
        case "3":
            raizCuadrada()
        case "4":
            potencia()

main()