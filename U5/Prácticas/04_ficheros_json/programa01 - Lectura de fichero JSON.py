# Crea un fichero llamado paises.json con el siguiente contenido:
# [
#   {"nombre": "Japón", "continente": "Asia", "poblacion": 125.7},
#   {"nombre": "Canadá", "continente": "América", "poblacion": 38.2},
#   {"nombre": "España", "continente": "Europa", "poblacion": 48.0}
# ]

# Escribe un programa que:
#  Abra el archivo y lo lea con json.load().
#  Muestre por pantalla cada país con un formato como:
#       Japón está en Asia y tiene 125.7 millones de habitantes.
#  Controle posibles errores con try/except #

from os import strerror
import json

try:
    # Abrir archivo
    with open("paises.json", "r", encoding="utf-8") as fichero:
        # Leer con json.load()
        datos = json.load(fichero) # Convierte json en una lista de diccionarios

        # Cada elemento de la lista es un diccionario con claves ("nombre", "continente", "poblacion")
        # Recorrer todos los países
        for pais in datos:
            print(f'{pais["nombre"]} está en {pais["continente"]} y tiene {pais["poblacion"]} millones de habitantes')
except IOError as e:
    print("Error durante la operación de archivo: ", strerror(e.errno))
    exit(e.errno)