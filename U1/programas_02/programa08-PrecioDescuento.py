## PROGRAMA 8

# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
#   desea saber cuanto deberá pagar finalmente por su compra.

descuento = float(input("Introduce el porcentaje descuento: "))
precio = float(input("Introduce el precio: "))

descuento = descuento/100
precioFinal = precio * (1 - descuento)

print("Debe pagar: ", precioFinal, "€")