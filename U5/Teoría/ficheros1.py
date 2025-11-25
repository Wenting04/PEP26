# - -- Pruebas -- - #

from os import strerror

try:
    # Abrir fichero
    fichero = open("c:/Users/Wenti/Documents/Instituto/DAW/PEP26/U5/Teoría/texto.txt", "rt", encoding="utf-8")
        # b -> modo texto, el cómo se le va a tratar
        # rb -> modo binario, se lee a nvl de bytes, tendré que controlar cómo se gestiona a líneas
        # si no pongo nada -> lo mismo que rt #
    # Si no tengo una ruta absoluta, se busca desde la carpeta actual
    # Para que tanto en linux como en windows se pueda usar, se usa barra, ns

    try:
        # Una forma de leer el fichero es leerlo entero
        contenido = fichero.read()
        # Otra forma:
        # contenido = fichero.readlines()
        # Devuelve un array y hace cada línea sea una posición del array #

        print(contenido)
    except Exception as exc:
        print("Error", strerror(exc.errno))
    finally:
        fichero.close()

    # Debemos de cerrar el archivo siempre después de usarlo
except Exception as exc:
    print("Error", strerror(exc.errno))

# Hay que tener en cuenta que cuando lo ejecutamos, estamos en la ruta de la carpeta abierta
# Debemos de situarnos en la ruta de este fichero para poder ejecutarse #