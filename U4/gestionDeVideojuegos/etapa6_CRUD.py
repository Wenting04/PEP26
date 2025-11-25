catalogo = {}
# ===== CRUD ====== #
# - -- Create -- - #
# Como un constructor
def crear(clave, titulo, anio, genero):
    # Convertir clave en minúsculas
    clave = clave.lower()

    if clave in catalogo:
        print("Juego ya creada")
    else:
        catalogo[clave] = {"titulo": titulo, "anio": anio, "genero": {genero}}
        print("Juego añadido correctamente")

# - -- Read -- - #
def leer(clave):
    juego = catalogo.get(clave.lower())

    # Si juego no está vacío, entonces imprime juego
    if juego:
        print("Título:", juego['titulo'])
        print("Año:", juego['anio'])
        print("Género:", ",".join(juego['genero'])) # Lo convierte en un conjunto de texto ("," es para separarlos por coma si hay más de 1 género)
    else:
        print("No se encontró juego")

# - -- Update -- - #
# Por defecto, los valores van a ser none para que ccuando se ejecute la función, pueda elegir qué va a actualizar
def actualizar(clave, titulo=None, anio=None, genero=None):
    clave = clave.lower()
    # Si clave está en nel catalogo:
    if clave in catalogo:
        # Si valores tienen contenido, entonces entra en el if
        if titulo:
            catalogo[clave]["titulo"] = titulo
        if anio:
            catalogo[clave]["anio"] = anio
        if genero:
            catalogo[clave]["genero"] = genero
    else:
        print("No existe ese juego")

# - -- Delete -- - #
def eliminar(clave):
    clave = clave.lower()
    if clave in catalogo:
        del catalogo[clave]
        print("Juego eliminado correctamente")
    else:
        print("No exite ese juego")
# ================= #

## Pruebas
crear('zel', 'zelda', 2006, 'mundo abierto')
leer('zel')
actualizar('zel', 'ganon')
leer('zel')
eliminar('zel')
leer('zel')