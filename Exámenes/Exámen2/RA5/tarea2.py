from os import strerror
import csv

# Genera cabecera con los datos
cabecera = ["Nombre", "Tipo", "Lunas"]

# Datos de planetas
data = [
    ["Marte", "Rocoso", 2],
    ["Júpiter", "Gaseoso", 79],
    ["Venus", "Rocoso", 0],
]

try:
    # "w" -> Para escribir 
    with open("planetas.csv", "w") as fichero:
        # Uso de writerow() y writerows()
        writer = csv.writer(fichero)
        writer.writerow(cabecera) # Para escribir una sola línea
        writer.writerows(data) # Para escribir varias filas de una sola vez

        print("Archivo 'planetas.csv' creado correctamente")
except IOError as e:
    print("Error durante la operación de archivos: ", strerror(e.errno))
    exit(e.errno)