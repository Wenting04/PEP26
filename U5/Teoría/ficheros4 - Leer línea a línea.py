from os import strerror
try:
    with open("c:/Users/Wenti/Documents/Instituto/DAW/PEP26/U5/Teoría/texto.txt", "rt", encoding="utf-8") as fichero:
        linea = fichero.readline().strip()
        # strip() quita espacios delante y atrás
        while linea:
            print(linea)
            linea = fichero.readline().strip()
except Exception as exc:
    print("Error", strerror(exc.errno))