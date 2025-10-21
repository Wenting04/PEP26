# a_bin(n): devuelve representación binaria de num entero en forma de cadena
# a_hexadecimal(n): devuelve representación hexadecimal de num entero en forma de cadena
# a_entero(texto): convierte una cadena numérica en entero (controlando errores si el texto no válido)

def a_bin(n):
    return bin(n)

def a_hexadecimal(n):
    return hex(n)

def a_entero(texto):
    try:
        n = int(texto)
    except ValueError:
        n = "No es un número"

    return n