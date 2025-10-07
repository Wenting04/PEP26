## PROGRAMA 4

# Usar bucles
# Pedir al usuario un nº continuamente
#   hasta que ingrese 45 como salida secreta
#   En tal caso, imprimir: "¡Has dejado el bucle con éxito!"
# 2 versiones:
#   1. Usar concepto condicional normal y break (el bucle no evalúa ninguna condición, bucle infinito)
#   2. No usar break y bucle while controle salida #

# Puedo o directamente en input pasarlo a int o en bucles poner "nº"
print("Bucle sin control con break")
while True:
    num = input("Introduzca un nº (45 como salida): ")

    if num == "45":
        print("Has dejado el bucle con éxito")
        break

print("While controlado sin break")
num = ""

while num != "45":
    num = input("Introduzca un nº (45 como salida): ")

print("Has dejado el bucle con éxito")
