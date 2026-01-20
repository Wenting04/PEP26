# Programa05: Listar y filtrar países
# Crear programa que:
# • Lea archivo paises.json del ejercicio 1
# • Pedir al usuario el nombre de un continente
# •  Mostrar sólo los países pertenecientes a ese continente
# • Guarde esos resultados en un nuevo archivo JSON llamado paises_filtrados.json
# 
# Estructura de paises.json
# [
#   { "nombre": "Japón", "continente": "Asia", "poblacion": 125.7 },
#   { "nombre": "Canadá", "continente": "América", "poblacion": 38.2 },
#   { "nombre": "España", "continente": "Europa", "poblacion": 48.0 }
# ] #

from os import strerror
import json

try:
    # Abrir archivo
    with open("paises.json", "r", encoding="utf-8") as fichero: # encoding="utf-8": Permitir tildes y etc
        # 1. Leer paises.json
        datos = json.load(fichero) # Convierte json en una lista de diccionarios

        # 2. Pedir al usuario el continente
        pedir_continente = input("Introduce el nombre de un continente: ")

        # 3. Filtrar los países del continente que ha pedido
        paises_pedidos = []

        for pais in datos:
            if pais["continente"].lower() == pedir_continente.lower():
                paises_pedidos.append(pais)

        # 4. Mostra los países pedidos y almacenados
        if len(paises_pedidos) == 0: # Si array paises_pedidos está vacío o cantidad es 0 (es como lenght)
            print("No se ha encontrado países de ese continente")
        else:
            print("Países del continente ", pedir_continente) # Imprime -> Países del continente nombre_continente
            for pais in paises_pedidos:
                print("->", pais["nombre"]) # Imprime -> nombre_pais

        # 5. Guardar los resultados en paises_filtrados.json
        with open("paises_filtrados.json", "w", encoding="utf-8") as fichero_salida:
            json.dump(paises_pedidos, fichero_salida, ensure_ascii=False, indent=4)
            # - json.dump: convierte en objeto de Python (lista, diccionario...) a formato JSON
            #       dump: Significa volcar o escribir
            #       Lo escribe directamente en un fichero
            #       Usado para: Guardar datos en un archivo
            # - paises_pedidos: objeto Python que quieres guardar (normalmente: lista ded iccionarios o un diccionario
            # - fichero_salida: archivo abierto en modo escritura "w"
            # - ensure_ascii=False: Permitir acentos, ñ, tildes, etc
            # - indent=4: Para que una línea se guarde de manera que ocupe 4 cajas por así decirlo
            #       Sin:
            #           [{"nombre":"España","continente":"Europa"}]
            #       Con:
            #           [
            #               {
            #                   "nombre": "España",
            #                   "continente": "Europa"
            #               }
            #           ] #
except IOError as e:
    print("Error durante la operación de archivo: ", strerror(e.errno))
    exit(e.errno)