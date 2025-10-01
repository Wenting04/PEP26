## PROGRAMA 7

# Pedir cantidad de minutos y muestre horas y min correspondientes

min = int(input("Minutos: "))

#División entera
horas = min // 60
min = min % 60

print("Son ", horas, "h y ", min, "min")