#   suma(a, b) --> Devuelve suma de 2 num
#   resta(a, b) --> Devuelve resta de 2 num
#   multiplicacion(a, b) --> Devuelve multiplicación de 2 num
#   division(a, b) --> Devuelve división de 2 num (controlando división entre 0)

def suma(a, b):
    return ("Suma: ", a, " + ", b, " = ", a + b)

def resta(a, b):
    return ("Suma: ", a, " - ", b, " = ", a - b)

def multiplicacion(a, b):
    return ("Suma: ", a, " * ", b, " = ", a * b)

def division(a, b):

    if b == 0:
        result = "No es posible divisir entre 0"
    else:
        result = ("Suma: ", a, " / ", b, " = ", a / b)

    return result