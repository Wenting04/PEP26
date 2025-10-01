## PROGRAMA 9

# Calcular calificación final si calificación parcial dependiendo de la RA
#   RA1 -> 20%
#   RA1 -> 60%
#   RA1 -> 20%

ra1 = float(input("Nota RA1: "))
ra2 = float(input("Nota RA2: "))
ra3 = float(input("Nota RA3: "))

ra1 = ra1 * 0.2
ra2 = ra2 * 0.6
ra3 = ra3 * 0.2

nota = ra1 + ra2 + ra3
print("Nota final: ", nota)