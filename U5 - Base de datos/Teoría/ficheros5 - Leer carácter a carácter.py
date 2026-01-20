from os import strerror
try:
    # Podemos usar with open("texto.txt", etc...) sólo si nos situamos en dicha carpeta
    # el programa no se ejecuta correctamente porque de normal nos situamos en la carpeta PEP26
    with open("c:/Users/Wenti/Documents/Instituto/DAW/PEP26/U5/Teoría/texto.txt", "rt", encoding="utf-8") as fichero:
        c=fichero.read(2)
        while c:
            print(c, end="")
            c = fichero.read(1)
except Exception as exc:
    print("Error", strerror(exc.errno))