# Método donde le pasas una función y amplía
def decorador(f):
    # Crea la función nueva a partir de la función que pasa al método
    def funcion_nueva():
        print("Funcionalidad extra")
        f() # Este f hace referencia a la f de: def decorador(f):
    return funcion_nueva

# decorador es para ampliar una función
@decorador
def funcion_inicial():
    print("Funcionalidad inicial")

# Ejemplo 2
def hola1():
    print ("Holaaaaa 1")

@decorador
def hola2():
    print ("Holaaaaa 2")

# No podemos llamar a decorador() el método es para pasarle una función y si hacemos sólo decorador() no funciona
# Imprime función decorador() y funcion_incial()
funcion_inicial() # Funcionalidad extra  Funcionalidad inicial
# Imprime sólo hola1()
hola1() # Holaaaaa 1
# Imrime decorador() y hola2()
hola2() # Funcionalidad extra  Holaaaaa 2