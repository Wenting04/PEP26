# = == Explicación Método Abstracto == =
# - NO tiene implementación
# - Obliga a las clases hijas a implementarlo
# Resumen: "Todas las subclases tienen que saber hacer esto, pero cada una a su manera"
# 
# Ejemplo: la clase Animal dice: "Todo animal debe poder saludar()"
#   Pero no sabe cómo, porque un perro no saluda igual que un pájaro
# 1. Importar ABC
# 2. Creamos la clase Animal y le insertamos el ABC
# 3. Dentro de esta clase creamos el método saludar(self) pero usando @abstractmethod
# 4. Creamos otra clase Perro que herede de Animal con el método saludar(self) y que imprima "Guau"
# Ejemplo código:
#  from abc import ABC, abstractmethod
#   class Animal(ABC):
#       @abstractmethod
#       def saludar(self)
#         pass
# 
#   class Perro(Animal):
#       def saludar(self):
#           print("Guau")

from abc import ABC, abstractmethod

class AnimalMarino(ABC):
    # Constructor (atributo nombre)
    def __init__(self, nombre):
        self.__nombre = nombre

    # Getter
    @property
    def nombre(self):
        return self.__nombre

    # Setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))

    # Método abstracto saluda
    @abstractmethod
    def saluda(self):
        raise NotImplementedError
    # NotImplementedError
    # Lanza una excepción que significa "Este método existe, pero aún no está implementado"
    # Otra forma de decir "Si alguein llegó hasta aquí, es un error de diseño" #
    # Además, en clases padre, estos métodos no están diseñados para que devuelva algo o contener algo #
    # En cambio, en clases hijos, sí debe de tener este método pero no necesariamente debe devolver algo #

    # Método abstracto sonido
    @abstractmethod
    def sonido(self):
        raise NotImplementedError


class Delfin(AnimalMarino):

    # SOBREESCRIBE Constructor (atributo nombre)
    def __init__(self, nombre):
        super().__init__(nombre)

    # SOBREESCRIBE Método abstracto saluda
    def saluda(self):
        print(f"Soy un delfin llamado {self.nombre}")

    # SOBREESCRIBE Método abstracto sonido
    def sonido(self):
        print("Clicks y silbidos")


class Tiburon(AnimalMarino):

    # SOBREESCRIBE Constructor (atributo nombre)
    def __init__(self, nombre):
        super().__init__(nombre)

    # SOBREESCRIBE Método abstracto saluda
    def saluda(self):
        print(f"Soy un tiburon llamado {self.nombre}")

    # SOBREESCRIBE Método abstracto sonido
    def sonido(self):
        print("No tiene un sonido audible característico")


# FUERA DE LA CLASE #

# Las ques están fuera de las clases son funciones main #
try:
    print("== = Inicializar animales 1, 2, 3 y 4 = ==")
    animal1 = Delfin("Flipper")
    animal2 = Tiburon("Tiburon Blanco")
    animal3 = Delfin("Alex")
    animal4 = Tiburon("Mai")

    print("== = Crear lista animales con objetos dentro = ==")
    animales=[animal1, animal2, animal3, animal4]
    print("== = Saludar a todos los de la lista usando forEach == =")
    for animal in animales:
        animal.saluda()
        animal.sonido()

except Exception as e:
    print(e)