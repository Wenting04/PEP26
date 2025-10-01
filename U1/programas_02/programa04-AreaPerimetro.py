## PROGRAMA 4

#Pide altura y base de un triángulo y lo calcula área y perímetro e imprime

base = float(input("Base: "))
altura = float(input("Altura: "))

area = base*altura
perim = 2 * (base + altura)

print("El área del triángulo es de: ", area)
print("El perímetro del triángulo es de: ", perim)