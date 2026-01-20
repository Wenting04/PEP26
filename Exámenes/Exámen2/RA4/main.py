# Enunciado:
# 1. Usar diccionario con estructura clave valor
#   Clave: código de producto (str)
#   Una tupla que contenga exactamente dos elementos:
#       Nombre del producto (str)
#       Lista con historial de precios de ese producto (float)

# agregar_producto(inventario, codigo, nuevo_precio)
# 1. Si código no existe, crea entrada en diccionario. La lista de precio #

def crear_inventario():
    return {} # Diccionario vacío
    # Estructura diccionario:
    # Diccionario = { Clave : Valor }
    # Inventario = {
    #   codigo: {"datos": tupla} #
    # }
    # tupla = (nombre, lista de precios)

def agregar_producto(inventario, codigo, nombre, precio_inicial): # (diccionario, cod_producto, nom_producto, precio_inicial)

    # Pasarlo a minúsculas
    codigo = codigo.lower()

    try:
        precio_inicial = float(precio_inicial)

        if codigo in inventario: # Si existe, retorna false, no se agrega
            print("Producto ya existe")
            return True
        else:
            # Crear tupla
            tupla = (nombre, precio_inicial)

            # Agregar a diccionario
            inventario[codigo] = tupla

            print("Producto añadido correctamente")
            return False
    except ValueError:
        print("Precio inválido")

def actualizar_precio(inventario, codigo, nuevo_precio):
    # Buscar producto por su código : Recorrer inventario y buscar por clave
    # Si existe, añade nuevo_precio a lista de precios que está dentro de la tupla y retorna true
    # Si código no existe, retorna false


    # Pasarlo a minúsculas
    codigo = codigo.lower()

    try:
        nuevo_precio = float(nuevo_precio)
        if codigo in inventario: # Si clave coincide
            tupla = inventario[codigo]["datos"] # Obtener tupla (nombre y lista de precios)
            precios = tupla[-1] # Obtengo último elemento de la tupla, es decir, la lista
            precios.append(nuevo_precio) # Añadir precio
            tupla[-1] = precios
            inventario[codigo]["tupla"] = tuple(tupla) # Volverlo tupla y añadirmo

            return True
        else:
            return False
    except ValueError:
        print("Precio inválido")

def obtener_producto (inventario, codigo):
    # Devuelve cadena que muestra producto con sigueinte formato:
    #   PRODUCTO:[Nombre] PRECIO ACTUAL:[Último precio de la lista]
    # Si producto no existe, devuelve cadena vacía

    # Pasarlo a minúsculas
    codigo = codigo.lower()

    if codigo in inventario: # Si clave coincide
        tupla = inventario[codigo]["datos"] # Obtener tupla (nombre y lista de precios)
        nombre, precios = tupla # Obtengo nombre y lista
        return f"PRODUCTO: {nombre}  PRECIO ACTUAL{precios[-1]}" # Imprime nombre y último producto
    else:
        return ""

def analizar_precios_producto(inventario, codigo):
    # Pasarlo a minúsculas
    codigo = codigo.lower()
    precios_ordenados = []

    if codigo in inventario:
        tupla = inventario[codigo]["datos"] # Obtener tupla (nombre y lista de precios)
        precios = tupla[-1] # Obtengo nombre y lista

        # Hacer una copia para ordenarlos y no perder la anterior
        precios_ordenados = precios

        # Ordenar precios
        precios_ordenados.sort()

        return precios_ordenados
    else:
        return precios_ordenados

# main #
print("- --  -- -")
# Crear inventario vacío
print("- -- Crear inventario vacío -- -")
inv = crear_inventario()

# Añadir 2 productos
print("- -- Añadir 2 productos -- -")
agregar_producto(inv, "P001", "Portátil", "1200")
agregar_producto(inv, "P002", "Teclado", "15.50")

# Añadir producto duplicado
print("- -- Añadir producto duplicado -- -")
agregar_producto(inv, "P001", "Portátil", "1200")

# Actualizar precio de 2
print("- -- Actualizar precio 2 productos -- -")
actualizar_precio(inv, "P001", 1150.50)
actualizar_precio(inv, "P002", 16)

# Mostrar uno de los 2 productos
print("- -- Mostrar uno de los 2 productos -- -")
print(obtener_producto(inv, "P001"))

# Analizar precio de 1 de los productos
print("- -- Analizar precio de 1 de los producto -- -")
precios = analizar_precios_producto(inv, "P001")


# Si lista precios vacío, imprimir vacío
# Si no vacío, imprimir lista

# Gestion de error