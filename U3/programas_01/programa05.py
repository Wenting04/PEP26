## PROGRAMA 5

# Crear varias funciones y probar variables en Python (globales, no locales y locales) #

# Global: Fuera de cualqueir función
# Local: Dentro de una función
# No local: Dentro de una función anidada (una función dentro de otra) #

#Global
num1 = "Global"

def externa():
    num2 = "No local (en función externa)"

    def interna():
        num3 = "Local (interna)"

        #Usar nonlocal para modificar num2 (desde f externa)
        nonlocal num2
        num2 = "num2 modificado desde función interna"

        #Modificar global
        global num1
        num1 = "num1 modificado desde f interna"

        print("- -- Dentro de f interna -- -")
        print ("num1 = ", num1)
        print ("num2 = ", num2)
        print ("num3 = ", num3)

    interna()

    print("- -- Dentro de f externa -- -")
    print ("num1 = ", num1)
    print ("num2 = ", num2)
    # print ("num3 = ", num3) --> Da error pq en f externa num3 no existe

def main():
    print("- -- En main (ANTES de llamar f externa) -- -")
    print("num1 = ", num1)

    externa()

    print("- -- En main (DESPUÉS de llamar f externa) -- -")
    print("num1 = ", num1)

    #Aquí num2 y num3 no existen


main()