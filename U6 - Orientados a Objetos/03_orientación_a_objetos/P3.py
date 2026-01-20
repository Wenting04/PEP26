# Programa para gestionar "batalla de personajes" #

# Importamos para el método abstracto
from abc import ABC, abstractmethod
import random # Para aleatorio

# = == 3.1.1. Clase base (Herencia básica) == = #
class Personaje(ABC): # Si no fuera abstracto simplemente sería class Personaje:
    # Constructor
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida
    # Hemos definido para que los atributos sean privados, 
    #   es decir, en los métodos dentro de esta clase,
    #   para usarlos, debemos de tener el getter Sí o Sí #

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
    @vida.setter # Para tener uun setter debemos tener primero el getter
    def vida(self, nueva_vida): # Nunca debe ser negativo
    #    if ( nueva_vida < 0 ):
    #        raise ValueError("La vida no puede ser negativo")
    #    else:
    #        self.__vida = nueva_vida # Simplemente ponemos por ejemplo vida = nueva y ya se cambia
        self._vida = max(0, nueva_vida) # Delf profe, evita vida negativa

    # Getter VIVO
    @property
    def vivo(self): # Sólo lectura y devuelve True/False
        return self._vida > 0 # Si vida es menor que 0, entonces devuelve False, al contrario, si es más, True

    # Método abstracto
    @abstractmethod
    def atacar(self, objetivo): # Será redefinido por sus subclases
        raise NotImplementedError # O podemos poner pass


# = == 3.1.2. Subclase Guerrero y composición con Arma == = #
# = == Subclases == = #
class Arma: # No hereda de nada
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
        self._arma = arma # No es un num, es un objeto arma
        # Quiere decir, cuando vayamos a crear al Guerrero, antes debemos de crear el objeto arma y meterlo aquí
        # Ejemplo código:
        #   Inicializo arma: espada = Arma("Espada", 10)
        #   Creo guerrero: guerrero = Guerrero("Conan", 100, espada)
        # Esa espada, es un objeto arma donde ya tiene su daño base #

    # Getter Arma
    @property
    def arma(self): # Sólo lectura
        return self._arma

    # = == Métodos == = #

    # Del método abstracto atacar de la clase base/principal
    def atacar(self, objetivo):
        # Objetivo:
        # Es el enemigo/oponente
        # Ejemplo:
        # 1. Ya hemos creado al heroe (su clase tiene sí o sí un método atacar, por abstracto)
        # 2. Creamos guerrero orco
        # 3. Hacemos que heroe ataque al orco
        # 
        # Ejemplo código:
        #   orco = Guerrero("Orco", 80, hacha)
        #   heroe.atacar(orco)
        # Lo que hace: dentro de heroe invoca al método atacar y le pasa el objeto orco #

        # Obtener daño que va a provocar el arma que tiene el actual psj
        # danioAtacar: Variable local del método
        danioAtacar = self._arma.danio + random.randint(0, 5) # Num del 0 al 5
        # Desglosar
        # self.arma -> Consigo el arma del actual personaje (recordemos, es un objeto)
        # .danio -> Propiedad de la clase Arma (tenemos el getter) #

        # Conseguimos la vida del ooponente y le restamos
        objetivo.vida -= danioAtacar # Restar vida del objetivo
        # Otra forma: objetivo.vida = objetivo.vida - danioAtacar

        print(f"El {self.nombre} atacó al {objetivo.nombre}, le ha restado {danioAtacar} puntos de vida")


# = == 3.1.3. Subclase Mago con un diccionario de hechizos == = #
class Mago(Personaje):
    # Constructor
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos # Diccionario externo
        # Es decir, cuando inicialicemos el Mago, vamos a pasarle el diccionario ya creado
        # Diccionario:
        # Estructura que guarda datos en pares con clave -> valor
        # Ejemplo código:
        #   edades = {
        #       "Ana": 20,
        #       "Luis": 25,
        #       "María": 30
        #   }
        # "Ana" -> Clave
        # 20 -> Valor
        # 
        # Para acceder a un valor: edades["ana"] # 20 #

        # Dato extra: tuplas
        # tuplas son listas inmutables, es decir, no se pueden editar los valores
        # Comparar:
        # lista[] -> Sí se puede modificar
        # tupla() -> No se puede modificar #

    # Getter Hechizos
    @property
    def hechizos(self): # Sólo lectura
        return self._hechizos

    # = == Métodos == = #
    def atacar(self, objetivo):
        # Seleccionar hechizo al azar
        # hechizo, atributo local
        #   Almacena una clave aleatoria de todos los hechizos que hay en el diccionario
        hechizo = random.choice(list(self.hechizos.keys()))
        # Desglosar random.choice(list(self.hechizos.keys()))
        # self.hechizos.keys()
        #   Devuelve todas las claves del diccionario: dict_key(["Fuego, "HIelo", "Rayo"])
        #       Pero NO es na lsita, sólo uan vista especial
        #   Y el diccionario puede aparentar así:
        #       self.hechizos{
        #           "Fuego": 20,
        #           "Hielo": 15,
        #           "Rayo": 25
        #       }
        # list(self.hechizos.key())
        #   Convierte esa lista de claves en lista real
        # random.choice(...)
        #   Selecciona un elemento aleatorio de la lista #

        # Atributo local, almacena valor del hechizo
        danioAtacar = self.hechizos[hechizo]
        # self.hechizos[hechizo]
        #   Le paso la clave y esta al ser clave valor, me devuelve su valor #

        # Restar vida del oponente
        objetivo.vida -= danioAtacar

        print(f"El {self.nombre} lanzó el hechizo {hechizo} al {objetivo.nombre}, le ha restado {danioAtacar} puntos de vida")


# = == 3.1.4. Uso correcto de properties en todas las clases == = #
# 1. Asegurarnos de controlar vida de cada psj con setter (en clase Personaje, porque es algo que todos los psj necesitan)
# 2. Arma, Guerrero y Mago deben dar sus atributos personales con @property (osea, atributos que no tenían en la clase base Personaje) #

# = == 3.1.5. Polimorfismo == = #
# En Guerrero:
#   def atacar(self, objetivo):
#       danioAtacar = self._arma.danio + random.randint(0, 5)
#       objetivo.vida -= danioAtacar #
# En Mago:
#   def atacar(self, objetivo):
#       hechizo = random.choice(list(self.hechizos.keys()))
#       danioAtacar = self.hechizos[hechizo]
#       objetivo.vida -= danioAtacar
# Ambos necesitan los mismo parámetros para ejecutarse, por tanto, sin saber que tipo es, es posible su ejecución
# Además, ataca al oponente que le pases siendo este un objeto ya creado, donde obtendremos la vida de este a partir de un getter de su respectiva clase #

# = == 3.1.6. Sistema de combate por turnos == = #
# Todo lo siguiente será fuera de las clases
# Todo lo que esté fuera de las clases equivale a estar en main
# Devuelve msg de ganador y vida restante
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
    # Es decir:
    # if psj1.vivo:
    #   ganador = psj1
    # else:
    #   ganador = psj2 #
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

# Otra forma, crear diccionario y pasarlo:
#   hechizos = {    # Crear diccionario
#       "Bola de fuego": 18,
#       "Rayo": 22,
#       "Hielo": 15
#   }
#   mago = Mago("Merlin", 80, hechizos)

# - -- Invoca a combate (guerrero, mago) -- - #
combate(guerrero, mago)