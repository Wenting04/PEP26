import random
from abc import ABC, abstractmethod

# -----------------------------------
# CLASE BASE
# -----------------------------------

class Personaje(ABC):
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    # ---- PROPERTIES ----

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        # Evita vida negativa
        self._vida = max(0, valor)

    @property
    def vivo(self):
        return self._vida > 0

    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError


# -----------------------------------
# COMPOSICIÓN
# -----------------------------------

class Arma:
    def __init__(self, nombre, danio):
        self._nombre = nombre
        self._danio = danio

    @property
    def nombre(self):
        return self._nombre

    @property
    def danio(self):
        return self._danio


class Guerrero(Personaje):
    def __init__(self, nombre, vida, arma):
        super().__init__(nombre, vida)
        self._arma = arma

    # ---- PROPERTIES ----

    @property
    def arma(self):
        return self._arma

    # ---- ATAQUE ESPECÍFICO ----

    def atacar(self, objetivo):
        danio = self.arma.danio + random.randint(0, 5)
        objetivo.vida -= danio
        print(f"{self.nombre} golpea con {self.arma.nombre} y causa {danio} de daño.")


# -----------------------------------
# ASOCIACIÓN (diccionario de hechizos)
# -----------------------------------

class Mago(Personaje):
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos  # diccionario externo

    # ---- PROPERTIES ----

    @property
    def hechizos(self):
        return self._hechizos

    # ---- ATAQUE ESPECÍFICO ----

    def atacar(self, objetivo):
        hechizo = random.choice(list(self.hechizos.keys()))
        danio = self.hechizos[hechizo]
        objetivo.vida -= danio
        print(f"{self.nombre} lanza {hechizo} y causa {danio} de daño.")


# -----------------------------------
# SISTEMA DE COMBATE
# -----------------------------------

def combate(a, b):
    turno = 1
    print("\n--- COMIENZA EL COMBATE ---\n")

    while a.vivo and b.vivo:
        print(f"\n--- Turno {turno} ---")

        a.atacar(b)
        print(f"{b.nombre} queda con {b.vida} de vida.")
        if not b.vivo:
            break

        b.atacar(a)
        print(f"{a.nombre} queda con {a.vida} de vida.")

        turno += 1

    print("\n--- FIN DEL COMBATE ---\n")
    vencedor = a if a.vivo else b
    print(f"🏆 {vencedor.nombre} gana con {vencedor.vida} de vida restante.")


# -----------------------------------
# DEMO
# -----------------------------------

espada = Arma("Espada larga", 20)
guerrero = Guerrero("Arthur", 100, espada)

mago = Mago("Merlin", 80, {
    "Bola de fuego": 18,
    "Rayo": 22,
    "Hielo": 15
})

combate(guerrero, mago)
