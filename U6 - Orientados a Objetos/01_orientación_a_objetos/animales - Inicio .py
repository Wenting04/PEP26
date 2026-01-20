# Crear clase
class Animal:
    # Los atributos públicos, cualquiera puede acceder y modificar
    # Atributos privados, si queremos que se pueda cambiar, métodos setter y getter con @property #

    # Atributo de clase
    num_animales = 0
    __num_animales2 = 0 # Atributo privado


    # Constructor
    # Siempre tiene esta estructura: def __init__ (self, atributo): #
    # Los atributos creados normalmente serán PÚBLICOS, si hacemos self.__atributo, será PRIVADO #
    def __init__(self, nombre, especie, edad, id_chip, id_chip2, peso):
        # self es como this. en java
        self.nombre = nombre # Si pusiéramos self nombre = "Juan", cuando inicializamos una clase, siempre siempre el nombre será Juan
        self.especie = especie # Ahora si hacemos self especie = especie y lo declaramos en el constructor, entonces especie será lo que le pases
        self.edad = edad # AL ser público no se necesitan GETTERS ni SETTERS
        # Si hacemos self.__id_chip, crearemos un atributo PRIVADO
        self.__id_chip = id_chip # Estos atributos, cuando queremos editar o etc, usar GETTERs y SETTERS
        # Si hacemos self.__id_chip, crearemos un atributo PROTEGIDO
        self._id_chip2 = id_chip2
        self.__peso = peso

        # Cada vez que inicializar nuevo incrementa num_animales
        Animal.num_animales = Animal.num_animales +1
        Animal.__num_animales2 = Animal.__num_animales2 +1 # Atributo PRIVADO

    # Para que sepa que es una clase
    @classmethod # Recibe la clase
    def contar_animales(cls):
        return cls.__num_animales2

    # GETTERS con PROPERTY#
    # Lo comento para probar funcion property(), pero está bien
    # def get_id_chip(self):
    #    return self.__id_chip

    # Manera que recomeinda Python para usar
    @property # En el fichero decorador.py hay ejemplo
    def chip(self): # Esta vez no está el get_id_chip
        return self.__id_chip
    
    # Función que meto en la clase por la cara, no cambia nada (creo)
    @staticmethod
    def es_mayor_de_edad(edad):
        return (edad >= 2)

    # SETTERS con PROPERTY#
    # En Setters deberíamos aceptar valores string que no sean vacíos
    # Está bien, pero lo dejo en comentario para probar @property
    # def set_id_chip(self, nuevo_id_chip):
        # Si es str, entonces se sobreescribe, si no es str, no sobreescribe
    #     if ( isinstance(nuevo_id_chip, str) ):
    #         self.__id_chip = nuevo_id_chip
    #     else:
    #         raise (TypeError("El id_chip debe ser un String"))

    # Manera que recomeinda Python para usar
    @chip.setter
    def chip(self, nuevo_id_chip):
        # Si es str, entonces se sobreescribe, si no es str, no sobreescribe
        if ( isinstance(nuevo_id_chip, str) ):
            self.__id_chip = nuevo_id_chip
            print ("Se ha cambiado el chip")
        else:
            raise (TypeError("El id_chip debe ser un String"))

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso > 5 :
            self.__peso = nuevo_peso
        else:
            raise ValueError("Peso no válido")


    # Métodos #
    def saludar (self):
        # Importante la (f"comentarios {self.atributo}")
        print (f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad = self.edad +1


# = == Fuera de la clase == = #

try:
    # Atributo global #
    # Muchas maneras de usarse
    print(Animal.num_animales) # A través de clase

    # PROBAR CONSTRUCTOR
    # Inicializar una clase
        # Nombre, especie, edad, id_chip, id_chip2, peso
    animal1 = Animal("Kuma", "tigre", 10, "a123", 123, 50) # Creado mi primer objeto animal
    print(animal1.num_animales) # A través de objeto animal1

    animal2 = Animal("Miu", "gato", 5, "a234", 234, 20)
    print(animal2.num_animales) # A través de objeto animal2
    print(Animal.num_animales) # De cualqueir manera está bien
    print(animal1.num_animales) # Pq PY te da esta flexibilidad
    # Por @classmethod
    print(Animal.contar_animales()) # Lo mismo pero en caso de que contador num_animales sea un atributo privado


    # En pyhton, todos los atributos son públicos (en Java lo ponemos public atributo, etc) #
    print (animal1.nombre) # Kuma
    print (animal2.especie) # gato
    animal1.nombre = "agop"
    print (animal1.nombre) # Ahora: agop

    # PROBAR MÉTODO SALUDAR
    animal1.saludar() # Soy un tigre llamado agop y tengo 10 años
    animal1.cumplir_anios()
    animal1.edad = animal1.edad + 1 # Recordemos, en py los atributos son públicos, por tanto podemos editar incluso fuera de la clase
    animal1.saludar() # Soy un tigre llamado agop y tengo 11 años

    # ATRIBUTO PRIVADO
    #print(animal1.__id_chip) # Error
        # Es una manera de acceder a un atributo privado
    print(animal1._Animal__id_chip) # a123
    # Pero los atributos privados de normal se usa Getters y Setters
    # GETTER #
    # print(animal1.get_id_chip()) # Getter para el atributo privado # Está bien, pero lo comento para probar @property
        # Esta es la manera que recomienda python
    print(animal1.chip) # a123

    # SETTER #
    # animal1.set_id_chip("a5556")
    animal1.chip = "a5556" # Recuerda que es str
    print(animal1.chip) # a5556

    animal1.peso = 99
    print(animal1.peso) # 99

    if ( Animal.es_mayor_de_edad(animal1.edad) ):
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")



except Exception as e:
    print(e)