# Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
# Debe:
#  Mostrar los nombres de las columnas (fieldnames).
#  Recorrer las filas e imprimir información como:
# {Ciudad} ({País}) tiene una población aproximada de {Población
# (millones)} millones.

#  Si el archivo no incluye cabecera, define manualmente los campos necesarios #
from os import strerror
import csv

try:
    with open("ciudades.csv") as fichero:
        reader = csv.DictReader(fichero)

        # Si no incluye cabecera, definirla manualmente
        if reader.fieldnames is None:
            reader.fieldnames = ["Ciudad", "Pais", "Poblacion (millones)"]

        # Mostrar nombres de columnas (fieldnames)
        cabeceras = reader.fieldnames
        print(f"Los nombres de las columnas son {cabeceras}")

        # Recorrer filas e imprimir info
        for fila in reader:
            print(f'{fila["Ciudad"]} ({"Pais"}) tiene una población aproximada de {fila["Poblacion (millones)"]} millones')
except IOError as e:
    print("Error durante la operación de archivos: ", strerror(e.errno))
    exit(e.errno)