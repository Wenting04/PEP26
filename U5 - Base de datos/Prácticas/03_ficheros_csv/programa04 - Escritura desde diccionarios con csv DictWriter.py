# Crea un programa que escriba un archivo patrimonios.csv con información sobre ciudades con lugares Patrimonio de la Humanidad:
# patrimonios = [
#   {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
#   {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
#   {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
# ]
# El programa debe:
#  Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar emblemático"].
#  Escribir la cabecera con writeheader() y las filas con writerows().
#  Cambiar el delimitador a ;.
#  Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente." #

from os import strerror
import csv

# Estructura cabecera
cabecera = ["Ciudad", "País", "Lugar emblemático"]

# Contenido
patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    # newline="" para que no añada saltos de línea automñaticos
    # encoding="utf-8" permite escribir con tildes
    with open("patrimonios.csv", "w", newline="", encoding="utf-8") as fichero:
        # DictWriter permite escrbir archivos CSV usando diccionarios en vez de listas
        # fieldnames indica nombres de las columnas
        # delimiter lo que usará para separarlos
        # Osea, va a meter al fichero siguiendo la estructura de la cabecera, es decir, mira las claves para poner cada cosa en su sitio
            # Si las claves no coinciden, no imprime nada
        writer = csv.DictWriter(fichero, fieldnames=cabecera, delimiter=";")
        writer.writeheader() # Escribe automáticamente la cabecera en el archivo CSV
        writer.writerows(patrimonios)
        print("Archivo 'patrimonios.csv' generado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos: ", strerror(e.errno))
    exit(e.errno)