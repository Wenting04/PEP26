## PROGRAMA 1

# Programa hacer uso de función llamada saludar y que cumpla lo sigueinte:
# 1. Entrada: 3 parámetros de entrada (son 3 cadenas de texto: nombre, 1º apellido y 2º apellido)
# 2. Salida: No tiene parámetros de salida
# 3. Funcionalidad: Imprimir saludo a la persona usando los parámetros #

# Hacer función llamada saludar(), crear 3 cadenas (nombre, apellido1, apellido2) y no devuelve nada, sólo saluda

#Crear función
def saludar(nombre, apellido1, apellido2):
    print("¡Hola, ", nombre, apellido1, apellido2, "!")

#Pedir datos al usuario
nom = input("Introduzca su nombre: ")
apel1 = input("Introduzca el primer apellido: ")
apel2 = input("Introduzca su segundo apellido: ")

#Usamos la función
saludar(nom, apel1, apel2)