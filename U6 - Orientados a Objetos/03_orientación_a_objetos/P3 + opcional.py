# Programa para gestionar "batalla de personajes" #
# = == 3.1.8. Opciones de ampliación == = #
# 1. Añadir mana al mago y coste de hechizos
# 2. Permitir cambiar arma al Guerrero
# 3. Añadir clase Arquero con su forma de atacar
# 4. Guardar y cargar personajes en ficheros JSON
# 5. Guardar y cargar personajes en base de datos
# 6. Modo torneo: todos vs todos #

# Importamos para el método abstracto
from abc import ABC, abstractmethod
import random # Para aleatorio
import json
import sqlite3

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

# 2. Permitir cambiar arma al Guerrero
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

    # para cambio de arma, un setter
    # Setter Arma
    @arma.setter
    def arma(self, nueva_arma):
        self._arma = nueva_arma
        print(f"{self.nombre} cambió de {self._arma.nombre} arma a {nueva_arma.nombre}")

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
# 3.1.8.1. Añadir mana al mago y coste de hechizos
class Mago(Personaje):
    # Constructor
    def __init__(self, nombre, vida, mana, hechizos):
        super().__init__(nombre, vida)
        self._mana = mana
        self._hechizos = hechizos # Diccionario externo
        # Es decir, cuando inicialicemos el Mago, vamos a pasarle el diccionario ya creado
        # Diccionario:
        # Estructura que guarda datos en pares con clave -> valor
        # Ejemplo código:
        #   hechizos = {
        #       "Bola de fuego": {"danio": 18, "coste": 10},
        #       "Rayo": {"danio": 22, "coste": 15},
        #       "Hielo": {"danio": 15, "coste": 8}
        #   }
        # "Rayo" -> Clave
        # {"danio": 22, "coste": 15} -> Valor
        # 
        # Para acceder a un valor en específico:
        # hechizos["Rayo"]["danio"] # 22
        # O
        # hechizo = "Rayo"
        # hechizos[hechizo]["coste"] # 15 #

    # Getter Hechizos
    @property
    def hechizos(self): # Sólo lectura
        return self._hechizos

    # Getter Mana
    @property
    def mana(self): # Sólo lectura
        return self._mana

    # = == Métodos == = #
    def atacar(self, objetivo):
        # Filtrar hechizos que pueda pagar
        hechizos_disponibles = [
            h for h, datos in self._hechizos.items()
            if datos["coste"] <= self.mana
        ]

        # Si no tiene maná suficiente para ningún hechizo
        if not hechizos_disponibles:
            print(f"{self.nombre} no tiene maná suficiente para ningún hechizo, pierde turno")

        # Seleccionar hechizo al azar que pueda costear con su actual mana
        hechizo = random.choice(hechizos_disponibles)

        # Atributo local, almacena valor del hechizo
        hechizoUsar = self.hechizos[hechizo]

        # Restar maná y restar vida
        self.mana -= hechizoUsar["coste"]
        objetivo.vida -= hechizoUsar["danio"]

        print(
            f"{self.nombre} lanza {hechizo} a {objetivo.nombre} "
            f"(Daño: {hechizoUsar['danio']}, Maná restante: {self.mana})"
        )

# 3. Añadir clase Arquero con su forma de atacar
class Arquero(Personaje):
    def __init__(self, nombre, vida, precision):
        super().__init__(nombre, vida)
        self._precision = precision

    # Método para atacar
    def atacar(self, objetivo):
        # Haremos que al apuntar se necesite un rango de puntería
        rango = random.randint(1, 100)

        if (rango <= self._precision): # Si rango entra en precisión
            danio = random.randint(10, 20) # Daño aleatorio
            objetivo.vida -= danio # Restamos
            print(f"{self.nombre} dispara una flecha a {objetivo.nombre}, le quita {danio} de vida")
        else:
            print(f"{self.nombre} falla el disparo")

# = == 3.1.4. Uso correcto de properties en todas las clases == = #
# 3.1.8.1. Asegurarnos de controlar vida de cada psj con setter (en clase Personaje, porque es algo que todos los psj necesitan)
# 3.1.8.2. Arma, Guerrero y Mago deben dar sus atributos personales con @property (osea, atributos que no tenían en la clase base Personaje) #

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
hacha = Arma("Hacha de guerra", 30)

# Crear personaje
guerrero = Guerrero("Arthur", 100, espada) # (Nombre, vida, arma)

# Cambiar arma al personaje
guerrero.arma = hacha

# - -- Crear Mago con un diccionario de hechizos -- - #
mago = Mago("Merlin", 80, 100, {
    "Bola de fuego": {"danio": 18, "coste": 10},
    "Rayo": {"danio": 22, "coste": 15},
    "Hielo": {"danio": 15, "coste": 8}
}) # (Nombre, Vida, Mana, Diccionario de hechizos)
# Otra forma, crear diccionario y pasarlo:
#   hechizos = {    # Crear diccionario
#       "Bola de fuego": 18,
#       "Rayo": 22,
#       "Hielo": 15
#   }
#   mago = Mago("Merlin", 80, hechizos)

# - -- Invoca a combate (guerrero, mago) -- - #
combate(guerrero, mago)


# 3.1.8.4. Guardar y cargar personajes en ficheros JSON
# import json
# Guardar psj en archivo
def guardar_psj(psj, archivo):
    datos = {
        "tipo": psj.__class__.__name__,
        # psj:
        #   psj es un objeto, ej: guerrero = Guerrero("Arthur", 100, espada)
        # .__class__: devuelve la clase del objeto, ej: guerrero.__class__  # <class '__main__.Guerrero'>
        # . __name__: nombre de la clase como string, ej: guerrero.__class__.__name__  # "Guerrero"
        # Resumen:  tipo te dice si es Guerrero, Mago o Arquero #
        "nombre": psj.nombre,
        "vida": psj.vida
    }

    if isinstance(psj, Guerrero): # Si es Guerrero
        datos["arma"] = {
            "nombre": psj.arma.nombre,
            "danio": psj.arma.danio
        }

    elif isinstance(psj, Mago): # Si es Mago
        datos["mana"] = psj.mana
        datos["hechizos"] = psj.hechizos

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

# Cargar psj
def cargar_psj(archivo):
    with open(archivo) as f:
        datos = json.load(f)

    if datos["tipo"] == "Guerrero":
        arma = Arma(datos["arma"]["nombre"], datos["arma"]["danio"])
        return Guerrero(datos["nombre"], datos["vida"], arma)

    if datos["tipo"] == "Mago":
        return Mago(datos["nombre"], datos["vida"], datos["mana"], datos["hechizos"])


# 3.1.8.5. Guardar y cargar personajes en base de datos
def crear_bd():
    conn = sqlite3.connect("personajes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXIST personajes (
        nombre TEXT,
        tipo TEXT,
        vida INTEGER
    )
    """)

    conn.commit()
    conn.close()

def guardar_bd(psj):
    conn = sqlite3.connect("personajes.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO personajes VALUES (?, ?, ?)",
        (psj.nombre, psj.__class__.__name__, psj.vida)
    )

    conn.commit()
    conn.close()


# 3.1.8.6. Modo torneo: todos vs todos
# Cada psj pelea vs todos los demás 1 vez
def torneo(psj): # Le paso una lista de personajes
    # Crear el diccionario de resultados
    result = {p.nombre: 0 for p in psj}
    # Clave -> nombre del psj
    # Valor -> Num de victorias (empieza por 0)
    # Ejemplo: psj = [Arthur, Merlin, Robin]
    # result = { "Arthur": 0, "Merlin": 0, "Robin": 0}
    # 
    # result = {}
    # for p in psj:
    #   result[p.nombre] = 0    # Empiezan con 0

    for i in range(len(psj)):
        # range(len(psj)) genera índices: 0, 1, 2, ...
        # i representa el índice del primer combatiente
        # psj[i] -> psj A del combate
        for j in range(i + 1, len(psj)):
            # i + 1 -> Evita peleas repetidas (A + B, B + A)    o   consigo misma (A + A)
            # Ej: 
            # i = 0, j = 1 -> 0 vs 1
            # i = 0, j = 2 -> 0 vs 2
            # i = 1, j = 2 -> 1 vs 2 #
            print("\n======================")
            combate(psj[i], psj[j])

            ganador = psj[i] if psj[i].vivo else psj[j]
            # if psj[i].vivo:
            #   ganador = psj[i]
            # else:
            #   ganador = psj[j]
            result[ganador.nombre] += 1 # Suma 1 victoria
            # Accede al diccionario
            # Incrementa cont del ganador -> result["Arthur"] = result["Arthur"] + 1

    print("\n🏆 RESULTADOS DEL TORNEO 🏆")
    for nombre, victorias in result.items(): # Recorrer el diccionario de resultados
        # result.item() devuelve: ("Arthur", 2), ("Merlin", 1), ("Robin", 0)
        print(f"{nombre}: {victorias} victorias")
        # Ej salida: Arthur: 2 victorias     Merlin: 1 victorias     Robin: 0 victorias
