from os import strerror

try:
    with open("c:/Users/Wenti/Documents/Instituto/DAW/PEP26/U5/Teoría/texto.txt", "rt", encoding="utf-8") as fichero:
        for linea in fichero:
            print(len(linea))
            print(linea, end="")
except Exception as exc:
    print("Error", strerror(exc.errno))