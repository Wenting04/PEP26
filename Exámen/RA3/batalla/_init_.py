print("Inicializando mi_paquete...")

from .jugador import ataque_jugador, mostrar_jugador
from .enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo

# Controlar lo que se importa si hacemos: from matemáticas import *
__all__ = [
    "ataque_jugador", "mostrar_jugador",
    "generar_enemigo", "ataque_enemigo", "mostrar_enemigo"
]

## No me funciona, no usaré el init