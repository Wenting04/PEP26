# area_rectangulo(base, altura): devuelve área
# area_triangulo(base, altura): devuelve área
# area_circulo(radio): devuelve área

# De la práctica "programa_01/programa03"
import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)  # Pi x (radio^2)