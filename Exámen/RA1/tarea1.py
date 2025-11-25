minutos = input("Introduce una cantidad de minutos: ")

minutos = int(minutos)

horas = minutos // 60
resto = minutos - (horas * 60)

print("Equivale a ", horas, " horas y ", resto, " minutos")