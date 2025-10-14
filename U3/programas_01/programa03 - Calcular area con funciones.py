## PROGRAMA 3

# Programa para mostrar menú para sleccionar operación que quiera
# Puede calcular área de un círculo, un triángulo o un rectángulo
# Menú a mostrar:
#   1. Calcular área de un círculo
#   2. Calcular área de un triángulo
#   3. Calcular área de un rectángulo
#   4. Salir
#   Introduce una opción (1-4): 
# Y se ejecutará hasta que usuario meta 4
# Debe tener las siguentes funciones:
#   calcular_area_cirulo: recibe radio del círuclo y return area
#   calcular_area_triángulo: recibe base y altura y return area
#   calcular_area_rectangulo: recibe base y altura y return area
#   mostrar_menu: mostrar menu
#   main(): lectura por teclado y verificar que esté correcto para luego llamar función correcta
#   opcion1: lectura por teclado de radio y valida que sea mayor a 0 y luego llamar función para calcular area cirulo
#   opcion2: lectura de base y altura, que sea mayor a 0 y llamar funcion triángulo
#   opcion3: lectura base y altura, mayor a 0 y llamada a area rectángulo#

import math #Para usar pi

def calcular_area_circulo(radio):
    return math.pi * radio ** 2 # Pi x (radio^2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("- -- Menú -- -")
    print ("1. Calcular área de un círculo")
    print ("2. Calcular área de un triángulo")
    print ("3. Calcular área de un rectángulo")
    print ("4. Salir")

def opcion1():
    try:
        radio = float(input("Introduce radio del círculo: "))
        if radio <= 0:
            print("El radio debe se mayor a 0")
        else:
            area = calcular_area_circulo(radio)
            print("El área del círculo es: ", area)
    except ValueError:
        print("Valor no válido")

def opcion2():
    try:
        base = float(input("Introduce base del triangulo: "))
        altura = float(input("Introduce altura del triangulo: "))
        
        if base <= 0 or altura <= 0:
            print("Los datos deben ser mayor a 0")
        else:
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es de: ", area)
    except ValueError:
        print("Valor no válido")

def opcion3():
    try:
        base = float(input("Introduce base del triangulo: "))
        altura = float(input("Introduce altura del triangulo: "))

        if base <= 0 or altura <= 0:
            print("Los datos deben ser mayor a 0")
        else:
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es de: ", area)
    except ValueError:
        print("Valor no válido")

def main():
    seguir = True

    while seguir:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")

        match opcion:
            case "1": 
                opcion1()
            case "2": 
                opcion2()
            case "3": 
                opcion3()
            case "4": 
                seguir = False
            case _: 
                print("Opción no válido")


main()