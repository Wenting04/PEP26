# Lista de tuplas con videojuegos (título, año, género)
videojuegos = [
    ("The Legend of Zelda", 1986, "Acción"),
    ("Super Mario Odyssey", 2017, "Acción"),
    ("Plantas vs Zombies", 2009, "Estrategia"),
    ("Stardew Valley", 2016, "Rol")
]

# Recorrer lista
for juego in videojuegos:
    titulo, año, genero = juego
    print(titulo, " (", año, ") ", genero)