## PROGRAMA 4

# Módulo turtle
#   Biblioteca estándar de Python para crear gráficos y dibujos de manera sencilla
#   Se mueve una "tortuga" virtual por la pantalla
# Se instala por defecto en el intérprete de Python

# Investiga la doc del módulo https://docs.python.org/3/library/turtle.html
# Escribe prog que:
#   1. Dibuje un cuadrado rojo sin rellenar
#   2. Dibuje un cículo verde relleno #

import turtle

# - -- Config inicial -- -
## Crea objeto tortuga para dibujar
t = turtle.Turtle()
t.pensize(3)    #Grosor de línea
t.speed(3)      #Velocidad media

# - -- Dibujar cuadrado rojo sin rellenar -- - 
## Cambia color de trazo
t.color("red")  #Color trazo

# Avanzar x cantidad y luego girar perpendicularmente y así 4 veces (cuadrado)
for i in range(4):
## Hacer avanzar y girar para dibujar el cuadrado
    t.forward(100)  #Avanza 100 unidades
    t.right(90)     #Gira 90 grados

# - -- Dibujar círculo verde relleno -- -
## Permite mover la tortuga sin dejar trazo
t.penup()       #Levanta lápiz para moverse sin dibujar
t.goto(150, 0)  #Mueve tortuga a la derecha para no solapar
t.pendown()     #Vuelve a bajar el lápiz

t.color("green", "lightgreen")  #Contorno verde, relleno verde claro
## Indica inicio y fin de una figura que debe ser rellenada
t.begin_fill()
t.circle(50)    #Dibujar círculo de radio 50
t.end_fill()

# - -- Fin -- -
## Deja ventana abierta hasta que usuario lo cierre
turtle.done()   #Mantiene ventana abierta