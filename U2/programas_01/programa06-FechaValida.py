## PROGRAMA 6

# Pide fecha (día, mes y año) y diga si es correcta #

# Importar datetime (hay que importar antes y no después)
import datetime

dia = input("Introduzca día: ")
mes = input("Introduzca mes: ")
anio = input("Introduzca año: ")


if dia == "" or mes == "" or anio == "":
    print("No lo debes dejar vacío")
else:
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    # Probar, si da error, se salta al except
    try:
        datetime.date(anio, mes, dia)
        print(dia, "/", mes, "/", anio)
        print("La fecha introducida es válida")
    except ValueError:
        print("La fecha introducida no es válida")