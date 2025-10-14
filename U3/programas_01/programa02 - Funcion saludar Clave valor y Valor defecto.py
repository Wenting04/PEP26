## PROGRAMA 2

# Crear función saludar con:
# - Entrada: 4 parámetros de entrada (4 cadenas: nombre, 1º apellido, 2º apellido y curso) y curso por defecto será 2DAW
# - Salida: No tiene
# - Funcionalidad: Imprime un msg saludando al alumno
# La función debe ser invocado varias veces y a veces cambiando el valor definido #

def saludar (nombre, apellido1, apellido2, curso = "2DAW"):
    print("Hola, ", nombre, apellido1, apellido2, " del curso ", curso)

#Pedir datos al usuario
nom = input("Introduzca su nombre: ")
apel1 = input("Introduzca el primer apellido: ")
apel2 = input("Introduzca su segundo apellido: ")
curso = input("Introduzca curso o dejalo en blanco: ")

if curso == "":
    saludar(nom, apel1, apel2)
else:
    saludar(apellido1 = nom, apellido2= apel1, curso=curso, nombre=nom)

saludar(apellido1 = "Quispe", apellido2= "Rojas", nombre="Katherine")