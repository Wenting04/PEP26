print("Inicializando mi_paquete...")

# Puedo poner import * o import nombre
from .operaciones import suma, resta, multiplicacion, division
from .conversiones import a_entero
from .figuras import *

# Controlar lo que se importa si hacemos: from matemáticas import *
__all__ = [
    "suma", "resta", "multiplicacion", "division",
    "calcular_area_rectangulo", "calcular_area_triangulo", "calcular_area_circulo",
    "a_bin", "a_hexadecimal", "a_entero"
]