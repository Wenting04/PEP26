## PROGRAMA 14

# Debe recibir nº bytes y mostrar por pantalla cuantos GBytes, MBytes, Kbytes y Bytes son
# En decimal y  binario

# Unidad        Sistema decimal (SI)    Sistema binario (EIC)
# 1KB / KiB     --> 1.000 bytes         --> 1.024 bytes
# 1MB / MiB     --> 1.000 KB            --> 1.024 MiB
# 1GB / GiB     --> 1.000 MB            --> 1.024 GiB
# 1TB / TiB     --> 1.000 GB            --> 1.024 TiB
# 1PB / PiB     --> 1.000 TB            --> 1.024 PiB
# 1EB / EiB     --> 1.000 PB            --> 1.024 EiB

# Datos extra:
#   SI lo usan fabricantes de discos, redes y marketing de almacenamiento
#   IEC: lo usan sistemas operativos, memoria RAM, tamaños de archivo#

# Ejemplo de salida:
# 1000000000 bytes en sistema decimal (SI): 1 GB, 0 MB, 0 KB, 0 bytes
# 1000000000 bytes en sistema binario (IEC): 0 GiB, 953 MiB, 690 KiB, 512 bytes
#


bytesTotal = int(input("Introduce nº bytes: "))

# Decimal
GB = bytesTotal // 10**9
resto = bytesTotal % 10**9

MB = resto // 10**6
resto %= 10**6

KB = resto // 10**3
bytesDec = resto % 10**3

# Binario
GiB = bytesTotal // 1024**3
resto = bytesTotal % 1024**3

MiB = resto // 1024**2
resto %= 1024**2

KiB = resto // 1024
bytesBin = resto % 1024

print(bytesTotal, "bytes en sistema decimal (SI): ", GB, "GB", MB, "MB", KB, "KB", bytesDec, "bytes")
print(bytesTotal, "bytes en sistema binario (IEC): ", GiB, "GiB", MiB, "MiB", GiB, "KiB", bytesBin, "bytes")