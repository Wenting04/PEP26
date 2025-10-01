## PROGRAMA 12

# 1 milla = 1,61 Km
# Pedir num de millas y otro de km
# Muestre el contrario
# Debe estar redondeados a 2 decimales#

millas = float(input("Introduce nº de millas: "))
km = float(input("Introduce nº de kilómetros: "))

millasAKm = millas * 1.61
kmAMillas = km / 1.61

print(millas, "millas son ", millasAKm, "km")
print(km, "km son ", kmAMillas, "millas")