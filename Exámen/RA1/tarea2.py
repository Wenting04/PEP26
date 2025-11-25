# No condicional ni estructura de datos #

# Pedir 3 datos al usuario: entero, decimal y cadena
entero = input("Introduzca un número entero: ")
decimal = input("Introduzca un número decimal: ")
cadena = input("Introduzca cadena: ")

# Convertirlo al tipo correspondiente
entero = int(entero)
decimal = float(decimal)

# Mostrar valor y tipo de variable
print()
print("Valor: ", entero, ", tipo: ", type(entero))
print("Valor: ", decimal, ", tipo: ", type(decimal))
print("Valor: ", cadena, ", tipo: ", type(cadena))

# Comprobar si tipo correcto
print()
print("Comprobar si " , entero, " es int: ", isinstance(entero, int))
print("Comprobar si " , decimal, " es float: ", isinstance(decimal, float))
print("Comprobar si " , cadena, " es str: ", isinstance(cadena, str))

# Almacenar comprobaciones en boolean
enteroCorrecto = isinstance(entero, int)
decimalCorrecto = isinstance(decimal, float)
cadenaCorrecto = isinstance(cadena, str)

# Mostrar si todas son correctas o no
print()
print("Entero ", entero, " es ", enteroCorrecto)
print("Decimal ", decimal, " es ", decimalCorrecto)
print("Cadena ", cadena, " es ", cadenaCorrecto)
print("Todas son ", enteroCorrecto and decimalCorrecto and cadenaCorrecto)

# Si todas correctas, muestra suma de num entero y num decimal
# Si alguna no lo es, mostrar msg de error
