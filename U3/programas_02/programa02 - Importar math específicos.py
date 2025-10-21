## PROGRAMA 2

# Modifica el anterior para que se importe sólo los math que necesitas #

from math import radians, sin, cos, sqrt, pow

def menu():
    print("- -- Menú -- -")
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un num")
    print("4. Potencia de dos num")

def seno():
    angulo = float(input("Introduce ángulo en grados: "))
    radianes = radians(angulo) #Convertir a radianes
    result = sin(radianes)
    print("El seno de", angulo, "es: ", result)

def coseno():
    angulo = float(input("Introduce ángulo en grados: "))
    radianes = radians(angulo) #Convertir a radianes
    result = cos(radianes)
    print("El coseno de", angulo, "es: ", result)

def raizCuadrada():
    num = float(input("Introduce num: "))

    if num < 0:
        print("Num no válido")
    else:
        result = sqrt(num)
        print("La raíz cuadrada de ", num, "es: ", result)

def potencia():
    base = float(input("Introduce base: "))
    exponente = float(input("Introduce exponente: "))
    result = pow(base, exponente)
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