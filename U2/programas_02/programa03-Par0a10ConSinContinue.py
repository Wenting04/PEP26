## PROGRAMA 3

# Mostrar pares que hay entre el 0 y el 10
# Resolver de 4 maneras
# Usar bucles for y while sin o con la secuencia continue #

# SIN continue
print("1. For sin continue")
for i in range(0, 11):
    #Si al dividir, el resto es 0, es par
    if i % 2 == 0:
        print(i)


print("2. While sin continue")
cont = 0
while cont < 11:
    if cont % 2 == 0:
        print(cont)
        cont += 1

# Con continue
print("3. For con continue")
for i in range(0, 11):
    #Si al dividir, el resto es 0, es par
    if i % 2 != 0:
        continue
    else:
        print(i)

print("4. While con continue")
cont = 0
while cont < 11:
    if cont % 2 != 0:
        cont += 1
        continue
    else:
        print(cont)
        cont += 1