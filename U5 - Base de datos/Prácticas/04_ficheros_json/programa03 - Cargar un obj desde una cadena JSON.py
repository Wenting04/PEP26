# Programa03: Cargar un objeto desde una cadena JSON
# Define en tu programa la siguiente cadena:

# import json
# cadena_json = '''
# [
#   {"nombre": "Chile", "moneda": "Peso chileno"},
#   {"nombre": "Egipto", "moneda": "Libra egipcia"}
# ]
# '''

# • Convierte la cadena en un objeto Python con json.loads().
# • Muestra el tipo de dato que se obtiene.
# • Imprime cada país con su moneda. #

import json

# Cadena JSON
cadena_json = '''
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

# Convertir la cadena en obj Python
data = json.loads(cadena_json)

# Mostrar tipo de dato
print("Tipo: ", type(data)) # Debe imprimir <class 'list'>

# Recorrer e imprimir cada país con su moneda
for pais in data:
    print(f'{pais["nombre"]} tiene de moneda el {pais["moneda"]}')