# Programa para gestionar "batalla de personajes" #

# Importamos para el método abstracto
from abc import ABC, abstractmethod
import random

# = == 3.1.1. Clase base (Herencia básica) == = #
class Personaje(ABC):
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    # = == Métodos PROPERTY == = #

    # Getter NOMBRE
    @property
    def nombre(self): # Sólo lectura
        return self._nombre

    # Getter VIDA
    @property
    def vida(self): # Lectura y escritura
        return self._vida

    # Setter
    @vida.setter
    def vida(self, nueva_vida): # Nunca debe ser negativo
        self._vida = max(0, nueva_vida) # Evita vida negativa

    # Getter VIVO
    @property
    def vivo(self): # Sólo lectura y devuelve True/False
        return self._vida > 0

    # Método abstracto
    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError


# = == 3.1.2. Subclase Guerrero y composición con Arma == = #
# = == Subclases == = #
class Arma:
    # Constructor
    def __init__(self, nombre, danio):
        self._nombre = nombre
        self._danio = danio

    # = == Métodos PROPERTY == = #

    # Getter NOMBRE
    @property
    def nombre(self): # Sólo lectura
        return self._nombre

    # Getter DAÑO
    @property
    def danio(self): # Sólo lectura
        return self._danio

class Guerrero(Personaje): # Hereda de Personaje
    # Constructor (con super)
    def __init__(self, nombre, vida, arma):
        super().__init__(nombre, vida)
        self._arma = arma

    # Getter Arma
    @property
    def arma(self): # Sólo lectura
        return self._arma

    # = == Métodos == = #

    # Del método abstracto atacar de la clase base/principal
    def atacar(self, objetivo):

        # Obtener daño que va a provocar el arma que tiene el actual psj
        danioAtacar = self._arma.danio + random.randint(0, 5) # Num del 0 al 5

        # Conseguimos la vida del ooponente y le restamos
        objetivo.vida -= danioAtacar # Restar vida del objetivo

        print(f"El {self.nombre} atacó al {objetivo.nombre}, le ha restado {danioAtacar} puntos de vida")


# = == 3.1.3. Subclase Mago con un diccionario de hechizos == = #
class Mago(Personaje):
    # Constructor
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos # Diccionario externo

    # Getter Hechizos
    @property
    def hechizos(self): # Sólo lectura
        return self._hechizos

    # = == Métodos == = #
    def atacar(self, objetivo):
        # Seleccionar hechizo al azar
        hechizo = random.choice(list(self.hechizos.keys()))

        # Atributo local, almacena valor del hechizo
        danioAtacar = self.hechizos[hechizo]

        # Restar vida del oponente
        objetivo.vida -= danioAtacar

        print(f"El {self.nombre} lanzó el hechizo {hechizo} al {objetivo.nombre}, le ha restado {danioAtacar} puntos de vida")


def combate(psj1, psj2):
    # Mostrar inicio de combate
    turno = 0
    print(f" -- - Comienza el combate entre {psj1.nombre} y {psj2.nombre} - -- ")

    ganador = None
    # Simular turnos de combate mientras estén ambos vivos
    while psj1.vivo and psj2.vivo: # En clase base hay método para determinar si vivo o no (True o False)
        turno += 1
        print(f" -- - Turno {turno} - -- ")

        psj1.atacar(psj2)

        # Si psj2 sigue vivo, mostrar msg de vida
        if psj2.vivo:
            print(f"{psj2.nombre} queda con {psj2.vida} de vida")
            psj2.atacar(psj1)

            # Si psj1 sigue vivo, mostrar msg de vida
            if psj1.vivo:
                print(f"{psj1.nombre} queda con {psj1.vida} de vida")

    # Declarar ganador
    print(" -- - Fin del combate - -- ")
    ganador = psj1 if psj1.vivo else psj2

    print (f"{ganador.nombre} gana con {ganador.vida} de vida restante")

# = == 3.1.7. Simulación y demostración final == = #
# - -- Crear Guerrero con un arma -- - #
# Crear arma
espada = Arma("Espada larga", 20)
guerrero = Guerrero("Arthur", 100, espada) # (Nombre, vida, arma)

# - -- Crear Mago con un diccionario de hechizos -- - #
mago = Mago("Merlin", 80, {
    "Bola de fuego": 18,
    "Rayo": 22,
    "Hielo": 15
}) # (Nombre, Vida, Diccionario de hechizos)

# - -- Invoca a combate (guerrero, mago) -- - #
combate(guerrero, mago)