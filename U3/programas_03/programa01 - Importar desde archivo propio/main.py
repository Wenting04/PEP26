## PROGRAMA 1

# Crear módulo operaciones con 4 funciones básicas relacionadas con operaciones numéricas:
#   suma(a, b) --> Devuelve suma de 2 num
#   resta(a, b) --> Devuelve resta de 2 num
#   multiplicacion(a, b) --> Devuelve multiplicación de 2 num
#   division(a, b) --> Devuelve división de 2 num (controlando división entre 0)
# Crear programa inicial main.py que importe el módulo matemáticas, pida al usuario 2 num y muestre por resultados #

# Puedo o hacer: from operaciones import *
#   O: from operaciones import suma
# Estas dos hace que puedas usarlos directamente: print( suma(a, b) )
# 
# En cambio, si haces: import operaciones
#   Para usar las funciones debes de hacer por ejemplo: print( operaciones.suma(a, b) ) #
import operaciones

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

print("Suma: ", a, " + ", b, " = ", operaciones.suma(a, b)  )
print("Resta: ", a, " - ", b, " = ", operaciones.resta(a, b) )
print("Multiplicación: ", a, " x ", b, " = ", operaciones.multiplicacion(a, b)    )
print("División: ", a, " / ", b, " = ", operaciones.division(a, b)  )