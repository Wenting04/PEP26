# PROGRAMA 2

#Programa que escriba por pantalla:
#   el booleano True, 
#   2 literales enteros, 
#   2 literales flotantes, 
#   1 cadena de carácteres, 
#   y para cada uno, su tipo de dato

#Python mismo lo sabe identificar sola
#Pero podemos añadir anotaciones para sugerir el tipo -> nombre: str = "Carlos"   o   edad: int = 25

verdad = True
entero1 = 5
entero2 = 10
flotante1 = 10.5
flotante2 = 15.5
cadena = "Hola mundo"

#Para imprimir tipo -> print(   type(nombre)   )
print ("Boolean: " , verdad , "y es un tipo " , type(verdad))
print ("Entero: " , entero1 , " y " , entero2 , "y es un tipo " , type(entero1))
print ("Flotante: " , flotante1 , " y " , flotante2 , "y es un tipo " , type(flotante2))
print ("Cadena: " , cadena , "y es un tipo " , type(cadena))