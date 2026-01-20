# 3. Enemigo:
#       generar_enemigo(): generar aleatoriamente atributos del enemigo (nombre, conocimiento - entre 1 y 10 -, energía - entre 1 y 5 -) y los devuelve
#           Para generar enemigo podemos usar
#               nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"] y luego nombre = random.choice(nomrbes)
#        ataque_enemigo(conocimiento, energía): devuelve nvl de magia del enemigo
#       mostrar_enemigo(nombre, conocimiento, energía): muestra en pantalla los valores actuales del enemigo

import random

def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"]
    nombre = random.choice(nombres)

    conocimiento = random.randrange(1, 11) # Entre 1 y 10
    energia = random.randrange(1, 6) # Entre 1 y 5

    return nombre, conocimiento, energia

def ataque_enemigo(conocimiento, energia):
    return ( conocimiento*energia )*( random.randrange(1, 4) )

def mostrar_enemigo(nombre, conocimiento, energia):
    print("Nombre: ", nombre)
    print("Conocimiento: ", conocimiento)
    print("Energia: ", energia)