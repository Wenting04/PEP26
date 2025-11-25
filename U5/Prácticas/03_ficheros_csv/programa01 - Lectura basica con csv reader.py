# Programa01: Lectura básica con csv.reader()
# Crea un fichero llamado ciudades.csv con el siguiente contenido:
# Ciudad,País,Población (millones)
#   Tokio,Japón,37.4
#   Delhi,India,30.3
#   Shanghái,China,27.1
#   São Paulo,Brasil,22.0
# Escribe un programa que:
#  Lea el fichero usando csv.reader().
#  Muestre en pantalla frases como:
#    La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
#  Controle las posibles excepciones #

from os import strerror
import csv

try:
    with open("ciudades.csv") as fichero:
        # Uso de csv.reader()
        reader = csv.reader(fichero, delimiter=",")

        # Obtener la cabecera
        cabecera = next(reader)
        # Imprime nombres de cada columna separados por ,
        print(f"Los nombres de las columnas son {", ".join(cabecera)}")

        # Mostrar por pantalla cada ciudad
        for fila in reader:
            print(f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes")

# Control de excepciones
except IOError as e:
    print('Error durante la operaión de archivos: ', strerror(e.errno))
    exit(e.errno)