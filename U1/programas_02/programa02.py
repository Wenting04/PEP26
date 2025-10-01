## PROGRAMA 2

# 1. Crear variable almacene entero 6
# 2. Mostrar por pantalla tipo de obj que contiene num 6 y tipo del objeto al que apunta (deberían ser iguales)
# 3. Crear otra variable que le asigne el 1º variable
# 4. Lo mismo que el punto 2 pero se refiere al punto 3
# 5. Usar operadores de identidad (is e is not) -> Comprobar y mostrar que apuntan al mismo obj y por tanto misma posición de memoria
# 6. Asignar cadena "Hola" al primer variable
# 7. Lo mismo que punto 2 pero esta vez debe ser diferente al objeto 6
# 8. Usar función isinstance() -> Comprobar y mostrar que obj que apunta la 1º ess tipo int y 2º es str#

# 1. Crear variable almacene entero 6
a = 6

# 2. Mostrar por pantalla tipo de obj que contiene num 6 y tipo del objeto al que apunta (deberían ser iguales)
print("Tipo de la 1º variable (a): ", type(a))
print("Tipo del objeto (6): ", type(6))

# 3. Crear otra variable que le asigne el 1º variable
b = a

# 4. Lo mismo que el punto 2 pero se refiere al punto 3
print("Tipo de la 1º variable (b): ", type(b))
print("Tipo del objeto (6): ", type(6))

# 5. Usar operadores de identidad (is e is not) -> Comprobar y mostrar que apuntan al mismo obj y por tanto misma posición de memoria
print("Comparar si a es b: ", a is b)
print("Comparar si a NO es b: ", a is not b)

# 6. Asignar cadena "Hola" al primer variable
a = "hola"

# 7. Lo mismo que punto 2 pero esta vez debe ser diferente al objeto 6
print("Tipo de la 1º variable (a): ", type(a))
print("Tipo del objeto (Hola): ", type("Hola"))

# 8. Usar función isinstance() -> Comprobar y mostrar que obj que apunta la 1º ess tipo int y 2º es str#
print("Comparar si a es instancia de str: ", isinstance(a, str))
print("Comparar si a es instancia de int: ", isinstance(a, int)) 