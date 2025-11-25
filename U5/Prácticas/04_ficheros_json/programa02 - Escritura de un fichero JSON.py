# Crea un programa que genere un archivo capitales.json con la siguiente información:
# capitales = [
#   {"país": "Francia", "capital": "París"},
#   {"país": "Australia", "capital": "Canberra"},
#   {"país": "Kenia", "capital": "Nairobi"},
#   {"país": "Brasil", "capital": "Brasilia"}
# ]

# Debe:
# • Escribir los datos en formato JSON con json.dump().
# • Usar los parámetros ensure_ascii=False y indent=4 para mejorar la legibilidad.
# • Mostrar el mensaje: "Archivo 'capitales.json' creado correctamente." #

from os import strerror
import json

try:
    # Datos
    capitales = [
        {"país": "Francia", "capital": "París"},
        {"país": "Australia", "capital": "Canberra"},
        {"país": "Kenia", "capital": "Nairobi"},
        {"país": "Brasil", "capital": "Brasilia"}
    ]

    # Abrir fichero y escribir
    with open("capitales.json", "w") as fichero:
        # ensure_ascii=False -> Permite carácteres especiales (acentos, ñ, símbolos)
        # indent=4 -> Controla cantidad de espacios que usan para indentación de cada nvl del JSON
            # Si fuera indent=0 (por defecto) -> todo en una sola línea
            # indent=4 -> cada nvl se sangra 4 espacios, muestra estructura jerárquica
        json.dump(capitales, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'capitales.json' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)