## PROGRAMA 3

# Usar módulos platform y os para mostrar:
# - Procesador donde se ejecuta programa
# - Sistema operativo y versión donde se ejecuta prog
# - Nombre del host donde se ejecuta prog
# - Directorio actual #

import platform
import os

def main():
    print("- -- Info del sistema -- -")

    #Procesador
    print("Procesador:", platform.processor())

    #Sistema operativo y versión
    print("Sistema operativo:", platform.system())
    print("Versión del sistema:", platform.version())

    #Nombre del host (equipo)
    print("Nombre del host:", platform.node())

    #Directorio actual
    print("Directorio actual:", os.getcwd())

main()