## PROGRAMA 2

# Modificar programa principal main.py del ejer anterior para que siga la sigueinte estructura:
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

#########################################################################################

# imports de la librería estándar
#Librerías que ya viene incorporadas en Python
import math
import os

# imports de librerías de terceros (no estándar)


# imports de módulos propios
import operaciones

# Definición de funciones principales
def main():
    # """Función principal del programa"""
    true = False

    while not(true):
        a = input("Introduce el 1º num: ")
        b = input("Introduce el 2º num: ")

        try:
            a = int(a)
            b = int(b)

            true = True
        except ValueError:
            print("Introduzca números por favor")

    print("--------------------------------------------")
    print(operaciones.suma(a, b)  )
    print(operaciones.resta(a, b) )
    print(operaciones.multiplicacion(a, b)    )
    print(operaciones.division(a, b)  )
    print("--------------------------------------------")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
    print("Me han ejecutado directamente")
else:
    main()
    print("Me han importado")

print("--------------------------------------------")
