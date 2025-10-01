## PROGRAMA 6

#Escribir varias veces printf() para
#   1. Mostrar operaciones de operadores aritméticos entre 2 nº
#       Operadores aritméticos -> División, suma, resta, etc
#   2. Mostrar op de operadores lógicos de python con valores booleanos
#       Operadores lógicos -> True y False
#   3. Mostrar op de operadores de comparación de python con valores de booleanos y/o nº
#       Operadores de comparación ==, !=, <, >, >=, <=

# Practicar operadores en Python y mostrar resultado con varios print()
# Tema 1.5 - Operadores (página 18)
a = 5
b = 10

# Operadores aritméticos:
print("Aritméticos")
# print() con f-strings
print("Suma")
print(f"{a} + {b} = {a + b}")

# Método str.format()
print("Resta")
print("{} - {} = {}".format(a, b, a - b))

# Estilo clásico tipo printf de C con %
print("División (float)")
print("%d / %d = %f" % (a, b, a / b)) 
    # %f para float
    # %d para enteros

# Más normal supongo
print("División entera")
print(b, " // ", a, " = ", b//a)

print("Módulo")
print(a, " % ", b, " = ", a%b)

print("Potencia")
print(a, " ** ", b, " = ", a**b)

print("Multiplicación")
print(a, " * ", b, " = ", a*b)

print("Identidad")
print(" +", b, " = ", +b)

print("negación")
print(" -", b, " = ", -b)


print("")
# Operadores lógicos
x = True
y = False

print("Lógicos")

print(x, " and ", y, " = ", x and y)
print(x, " or ", y, " = ", x or y)
print("not ", y, " = ", not y)
print("not ", y, " = ", not x)


print("")
# Operadores comparación
#Imprime True o False

print("Comparación")

print(a, " == ", b, " = ", a == b)
print(a, " != ", b, " = ", a != b)
print(a, " < ", b, " = ", a < b)
print(a, " > ", b, " = ", a > b)
print(a, " <= ", b, " = ", a <= b)
print(a, " >= ", b, " = ", a >= b)