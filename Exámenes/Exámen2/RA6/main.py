from abc import ABC, abstractmethod

# Clase abstracta
class Producto(ABC):
    # Constructor
    def __init__(self, nombre, precios):
        self._nombre = nombre
        self._precios = precios # Lista de precios (float)

    # = == Métodos PROPERTY == = #
    # Getter NOMBRE
    @property
    def nombre(self): # lectura y escritura
        return self._nombre

    # Setter NOMBRE
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (nuevo_nombre): # Si hay algo, entonces cambiar
            self._nombre = nuevo_nombre

    # Getter PRECIOS
    @property
    def precio_actual(self):
        return self._precios[-1] # La última

    # = == Métodos == = #
    def aniadir_precio(self, precio):
        if (precio > 0): # No admite precio negativo
            self._precios.append(precio)
        else:
            print("Precio en inválido, en negativo")

    @abstractmethod
    def calcular_precio_final(self):
        raise NotImplementedError
        #final = 0
        #for x in self._precios:
        #    final += x


class DiscoDuro(Producto):
    # Constructor (con super)
    def __init__(self, nombre, precios, tipo):
        super().__init__(nombre, precios)
        preciosLista = [] # Lista precios vacío
        self._precios = preciosLista
        self._tipo = tipo # HDD o SDD

    # = == Métodos == = #
    def calcular_precio_final(self):
        final = 0

        if (self._tipo == "SDD"):
            # Recargo de 20% más al precio
            for x in self._precios:
                final += (x * 1.2)
        else: # Entonces es "HDD"
            for x in self._precios:
                final += (x)

        return final

    def __str__(self):
        return f"DiscoDuro(nombre={self._nombre}, tipo={self._tipo})"

class Memoria(Producto):
    # Constructor (con super)
    def __init__(self, nombre, precios, capacidad):
        super().__init__(nombre, precios)
        preciosLista = [] # Lista precios vacío
        self._precios = preciosLista
        self._capacidad = capacidad # en GB

    # = == Métodos == = #
    def calcular_precio_final(self):
        final = 0

        if (self._capacidad == 16):
            # Recargo de 20% más al precio
            for x in self._precios:
                final += (x * 1.5)
        else: # Entonces es "HDD"
            for x in self._precios:
                final += (x)

        return final

    def __str__(self):
        return f"Memoria(nombre={self._nombre}, capacidad={self._capacidad})"



# Programa main #
print("Crear obj disco duro y otro con memoria")
disco = DiscoDuro( "disc1", 50, "SDD")
memoria = Memoria( "mem1", 100, 16)

print("Almacenar en lista (inv)")
inv = [disco, memoria]

print("Recorrer")
for x in inv:
    print(x)
    print(x.precio_actual)
    print(x.calcular_precio_final())