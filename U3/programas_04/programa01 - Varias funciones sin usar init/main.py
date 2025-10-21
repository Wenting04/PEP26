## PROGRAMA 1

# Mostrar un menú que permita elegir entre:
#   Operaciones matemáticas
#   Cálculo de áreas geométricas
# Según la elegida, pida al user los datos necesarios y muestre el resultado correspondiente #

# - -- Estructura a seguir -- - 
    # imports de la librería estándar
    # imports de librerías de terceros
    # imports de módulos propios
    # Definición de funciones principales
#   def main():
#   """Función principal del programa"""
#   print("Hola, este es el programa principal")
    # Bloque para asegurar ejecución sólo si el archivo es el principal
#   if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
#   main()

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
from matemáticas import conversiones
from matemáticas import figuras
from matemáticas import operaciones

# Definición de funciones principales
def main():
    # """Función principal del programa"""
    print("Hola, este es el programa principal")

    print("--------------------------------------------")
    menu()
    print("Seleccione")
    opcion = elegir()
    print("--------------------------------------------")

    if opcion == "1":
        pedirOperaciones()
    elif opcion == "2":
        pedirArea()
    else:
        print("No válido")
    print("--------------------------------------------")

def menu():
    print(" - -- Menú -- - ")
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")

def elegir():
    select = input()

    return select

def pedirOperaciones():

    print("Introduce el 1º num")
    a = elegir()
    print("Introduce el 2º num")
    b = elegir()

    a = conversiones.a_entero(a)
    b = conversiones.a_entero(b)

    #Comparamos si lo que devuelve es int o str
    if ( isinstance(a, int) and isinstance(b, int) ):
        print("--------------------------------------------")
        print(operaciones.suma(a, b)  )
        print(operaciones.resta(a, b) )
        print(operaciones.multiplicacion(a, b)    )
        print(operaciones.division(a, b)  )
        print("--------------------------------------------")
    else:
        print(a)

    

def pedirArea():

    print("1. Área rectángulo")
    print("2. Área triángulo")
    print("3. Área círculo")
    opcion = elegir()

    opcion = conversiones.a_entero(opcion)

    #Comparamos si lo que devuelve es int o str
    if ( isinstance(opcion, int) ):
        match opcion:
            case 1: # Rectángulo
                print("Introduzca la base")
                b = conversiones.a_entero(elegir())
                print("Introduzca la altura")
                h = conversiones.a_entero(elegir())

                print("Área de rectángulo = ", figuras.calcular_area_rectangulo(b, h))
            case 2: # Triángulo
                print("Introduzca la base")
                b = conversiones.a_entero(elegir())
                print("Introduzca la altura")
                h = conversiones.a_entero(elegir())

                print("Área de triángulo = ", figuras.calcular_area_triangulo(b, h))
            case 3: # Círculo
                print("Introduzca la radio")
                n = conversiones.a_entero(elegir())

                print("Área de círculo = ", figuras.calcular_area_circulo(n))
    else:
        print (opcion)

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
    print("Me han ejecutado directamente")
else:
    main()
    print("Me han importado")