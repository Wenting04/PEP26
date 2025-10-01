## PROGRAMA 10

# Con 1 num de 2 cifras, diseñar algoritmo para obtener num invertido

num = int(input("Introduce número de 2 cifras: "))

decenas = num // 10
unidades = num % 10

numInvert = unidades * 10 + decenas

print("Su invertido: ", numInvert)