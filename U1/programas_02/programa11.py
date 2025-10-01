## PROGRAMA 11

# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de N segundos.
# Escribie un programa que determine la hora de llegada a la ciudad B.#

# Cuándo sale
HH = int(input("Hora de salida: "))
MM = int(input("Minutos de salida: "))
SS = int(input("Segundos de salida: "))

# Tiempo que tarda en llegar
N = int(input("Tiempo de viaje en segundos: "))

#Pasar todo a segundos
sTodo = HH * 3600 + MM * 60 + SS

# Calcular hora de llegada -> Cantidad tiempo que tarda + tiempo de salida
t = N + sTodo

h = (t // 3600) % 24
m = (t % 3600) // 60
s = t % 60

#Con zfill para rellenar con ceros si hace falta (1º cambiamos a string para usarlo)
print("El ciclista llegó a las ",
       str(h).zfill(2), "h :", 
       str(m).zfill(2), "m :", 
       str(s).zfill(2), "s :")