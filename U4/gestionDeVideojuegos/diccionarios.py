# Transforma tu colección en un diccionario donde:
# ◦ La clave sea un identificador único ( título normalizado).
# ◦ El valor sea otro diccionario con datos de la videojuego.
# {
#  "titulo": str,
#  "anio": int,
#  "genero": set
# }
#  Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el catálogo
# usando la clave.
#  Implementa funciones de búsqueda:
# ◦ Exacta por título.
# ◦ Parcial (contenga un fragmento en el título).
# ◦ Por género o rango de años.
#  Calcula estadísticas:
# ◦ Número total de videojueg #

# Catálogo de videojuegos (lo que ya hay y lo siguiente es que le vamos a meter o algo así)
# "clave": {"titulo": str,"anio": int,"genero": set}
catalogo = {
    "zelda": {"titulo": "The Legend of Zelda", "anio": 1986, "genero": {"Acción"} },
    "mario": {"titulo": "Super Mario Odyssey", "anio": 2017, "genero": {"Acción"} },
    "plantavszombie": {"titulo": "Plantas vs Zombies", "anio": 2009, "genero": {"Estrategia"} },
    "stardew": {"titulo": "Stardew Valley", "anio": 2016, "genero": {"Rol"} },
}

# - -- Funciones CRUD (Crear, Leer, Actualizar, Eliminar) -- - #
# Como un constructor
def crear(clave, titulo, anio, genero):
    # Convertir clave en minúsculas
    catalogo[clave.lower()] = {"titulo": titulo, "anio": anio, "genero": genero}

def leer(clave):
    return catalogo.get(clave.lower(), None)

# Por defecto, los valores van a ser none para que ucando se ejecute la función, pueda elegi qué va a actualizar
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

def eliminar(clave):
    clave = clave.lower()
    if clave in catalogo:
        del catalogo[clave]
    else:
        print("No exite ese juego")

# - -- Funciones de búsquedas -- - #
# Exacta por título [devuelve 1 videojuego exacto]
def buscar_por_titulo(titulo):
    # Crear lista vacía para guardar resultados
    result = None

    # Recorrer todo el catalogo y devuelve el dicho videojuego con todos los datos (por eso .value)
    for x in catalogo.values(): # catalogo.value() devuelve una lista de todos los valores (diccionarios internos)
        if x["titulo"].lower() == titulo.lower():
            result = x
    
    print(result)

# Parcial (contenga un fragmento en el título) [Devuelve varios]
def buscar_parcial(trozo):
    result = []

    for x in catalogo.values():
        # Obtener título
        titulo = x["titulo"]

        # Comprobar si trozo está dentro del título
        if trozo.lower() in titulo.lower():
            # Si coincide, lo añadimos a la lista de resultados
            result.append(x)

    # Si lista result NO está vacía
    ##if result:
    #    print("Videojuego encontrado: ")
    #    for x in result:
    #        print(x["titulo"], x["anio"], x["genero"])
    #else:
    #    print("No encontrado")

    # Devuelve lista de juegos con coincidencias
    print(result)

# Por género o rango de años [Devuelve varios]
def buscar_por_genero(genero_buscar):
    result = []
    for x in catalogo.values():
        # genero = x["genero"] -> Al ser por ejemplo {"Acción"}, entonces no es una cadena, no posible usar esto
        for genero in x["genero"]:
            if genero.lower() == genero_buscar.lower():
                result.append(x)

    print(result)

def buscar_por_rango_anios(min, max):
    result = []
    for x in catalogo.values():
        anio = x["anio"]
        if min <= anio <= max:
            result.append(x)

    print(result)

# - -- Calcular estadísticas -- - #
# Num total de videojuegos
def total_juegos():
    total = len(catalogo)

    print(total)

def cont_por_genero():
    cont = {}

    # Recorrer todo el catálogo
    for x in catalogo.values():
        # Cada juego puede tener 1 o varios géneros
        for genero in x["genero"]:
            # Si genero existe, sumamos, si no, iniciamos a 1
            if genero in cont:
                cont[genero] += 1
            else:
                cont[genero] = 1

    print (cont) # Ej: {'Acción': 2, 'Rol': 3, ...}

# - -- Ejemplos -- - #

#print ("Crear un juego nuevo")
#crear("halo", "Halo Infinite", 2021, {"Acción", "Shooter"})
#print(catalogo["halo"])
#print ("")

#print ("Leer un juego")
#leer("mario")
#print ("")

#print ("Actualizar un juego")
#actualizar("zelda", anio=1987, genero={"Aventura"})
#print(catalogo["zelda"])
#print ("")

#print ("Eliminar un juego")
#eliminar("stardew")
#print(catalogo)
#print ("")

#print ("Buscar por título exacto")
#buscar_por_titulo("Super Mario Odyssey")
#print ("")

#print ("Buscar por fragmento en el título")
#buscar_parcial("Mario")
#print ("")

#print ("Buscar por género")
#buscar_por_genero("Acción")
#print ("")

#print ("Buscar por rango de años")
#buscar_por_rango_anios(2000, 2020)
#print ("")

#print ("Total de juegos")
#total_juegos()
#print ("")

#print ("Conteo por género")
#cont_por_genero()
#print ("")