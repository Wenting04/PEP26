from os import strerror

try:
    with open("c:/Users/Wenti/Documents/Instituto/DAW/PEP26/U5/Teoría/texto.txt", "rt", encoding="utf-8") as fichero:
        contenido = fichero.readlines() # Devuelve un array y hace cada línea sea una posición del array #
        print(contenido)
except Exception as exc:
    print("Error", strerror(exc.errno))