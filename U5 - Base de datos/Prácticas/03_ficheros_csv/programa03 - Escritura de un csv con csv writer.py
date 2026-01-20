# Programa03: Escritura de un CSV con csv.writer()
# Crea un programa que genere un fichero nuevo llamado capitales.csv con los siguientes datos:
#   Ciudad País Continente
#   París Francia Europa
#   Canberra Australia Oceanía
#   Nairobi Kenia África
#   Ottawa Canadá América
# El programa debe:
#  Escribir la cabecera y los datos con writerow() y writerows().
#  Usar un bloque try/except con os.strerror() para capturar errores de E/S.
#  Confirmar con un mensaje final: "Archivo 'capitales.csv' creado correctamente." #

from os import strerror
import csv

# Genera cabecera con los datos
cabecera = ["Ciudad", "Pais", "Continente"]

# Datos de países
data = [
    ["Paris", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceania"],
    ["Nairobi", "Kenia", "Africa"],
    ["Ottawa", "Canada", "America"],
]

try:
    # "w" -> Para escribir 
    with open("capitales.csv", "w") as fichero:
        # Uso de writerow() y writerows()
        writer = csv.writer(fichero)
        writer.writerow(cabecera) # Para escribir una sola línea
        writer.writerows(data) # Para escribir varias filas de una sola vez
    
    print("Archivo 'capitales.csv' creado correctamente")
except IOError as e:
    print("Error durante la operación de archivos: ", strerror(e.errno))
    exit(e.errno)