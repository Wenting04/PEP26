class AnimalTerrestre:
    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nueva_edad):
        if (nueva_edad < 0):
            raise ValueError("La edad debe ser positivo")
        else:
            self.__edad=nueva_edad

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,nuevo_peso):
        if (nuevo_peso < 0):
            raise ValueError("El peso debe ser positivo")
        else:
            self.__peso=nuevo_peso

    # Métodos #
    def saludar (self):
        # Importante la (f"comentarios {self.atributo}")
        print(f"Soy un animal terrestre llamado {self.nombre} y tengo {self.edad} años ")

    # ===== == = Métodos mágicos "dunder" = == ===== #

    # Método mágico para mostrar
    # Cuando llama directamente, ej: print(animal1), imprime esto siguiente #
    def __str__(self):
        return f"AnimalTerrestre(nombre={self.nombre}, edad={self.edad}, peso={self.peso})"

    # Método mágico de comparación (edad)
    # Usando los propios nombres podemos comparar edad, ej: animal1 < animal2 #
    def __lt__(self, otro):
        return self.edad < otro.edad

    # Método mágico para combinar
    #   nombre  :   concatenación de nombres ("Kuma-Balto")
    #   edad    :   media de ambas edades (entera o float, como prefieras)
    #   peso    :   suma de los pesos (si existen, si no, None)
    # Podemos sumar un animal con otro, ej: animal5 = animal1 + animal2, y luego print(animal5) #
    # Lo que hace es añadir el nombre al lado del otro con guión, sumar las edades y el peso (suma cada atributo, si es string, concatena con guión, si es num, se suman)
    def __add__(self, otro):
        return AnimalTerrestre(self.nombre + "-" + otro.nombre,self.edad + otro.edad, self.peso + otro.peso)    
    # =============== == = FIN == = ================ #

# HERENCIA #
class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias

    @property
    def gestacion_dias(self):
        return self.__gestacion_dias

    @gestacion_dias.setter
    def gestacion_dias(self,nueva_gestacion_dias):
        if (nueva_gestacion_dias < 0):
            raise ValueError("Los días de gestación deben ser positivos")
        else:
            self.__gestacion_dias=nueva_gestacion_dias

    # Sobreescribo #
    def saludar (self):
        # Importante la (f"comentarios {self.atributo}")
        print(f"Soy un mamimefero llamado {self.nombre}, tengo {self.edad} años  y mi gestación es de {self.__gestacion_dias}")

    # Cuando llama por su nomre, imprime lo siguiente, ej: print(animal3) #
    def __str__(self):
        return f"Mamifero(nombre={self.nombre}, edad={self.edad}, peso={self.peso}, gestacion_dias={self.__gestacion_dias})"


class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    @puede_volar.setter
    def peso(self, nuevo_puede_volar):
        self.__puede_volar = nuevo_puede_volar

    # Sobreescribo #
    def saludar (self):
        # Importante la (f"comentarios {self.atributo}")
        print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} años")
        if (self.__puede_volar):
            print(" y puedo volar")

    # Cuando llama por su nomre, imprime lo siguiente, ej: print(animal2) #
    def __str__(self):
        return f"Ave(nombre={self.nombre}, edad={self.edad}, peso={self.peso}, puede_volar={self.__puede_volar})"


# FUERA DE LA CLASE #

# Las ques están fuera de las clases son funciones main #
try:
    print("== = Inicializar animales (1, 2, 3, y 4) = ==")
    animal1 = AnimalTerrestre("Kuma",10, 100)
    animal2 = AnimalTerrestre("Miu", 5,  6)
    animal3 = Mamifero("Log", 10, 90, 200)
    animal4 = Ave("Uff", 4, 3, True)

    print("== = Saludar animales = ==")
    # Como Mamifero hereda de AnimalTerrestre, podemos usar métodos de AnimalTerrestre pero no al revés
    animal1.saludar()
    animal2.saludar()
    animal3.saludar()
    animal4.saludar()

    #print("== = Usar método mamífero (siendo ave) sin tener tal método = ==")
    #print(animal2.gestacion_dias()) # No funciona pq es AnimalTerrestre y no tiene métodos de Mamífero
    #print(animal3.gestacion_dias())
    # ¿Pq no funciona?
    # gestacion_dias NO es método, es una propiedad (@property)
    # Cuando usamos @property, Python permite acceder al valor como si fuera un atributo, sin paréntesis
    # Nuestra property:
    #   @property
    #   def gestacion_dias(self):
    #       return self.__gestacion_dias
    # Eso convierte gestacion_dias en un atributo de sola lectura, no una función llamable
    # Lo correcto es sin paréntesis #
    print("== = Imprimir gestación de días de animal 3 == =")
    print(animal3.gestacion_dias)

    print("== = Imprimir todos los datos de animales == =")
    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)

    print("== = Comparar animales (edad) = ==")
    print("animal1 < animal2")
    print(animal1 < animal2)
    print("animal2 < animal3")
    print(animal2 < animal3)

    print("== = Sumar animales (suma todos los atributos) = ==")
    print("animal5 = animal1 + animal2")
    animal5 = animal1 + animal2
    print(animal5)

except Exception as e:
    print(e)