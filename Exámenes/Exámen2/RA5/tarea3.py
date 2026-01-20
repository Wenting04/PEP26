# Crear venv en la carpeta: python -m venv .venv
# Activarlo: .venv\Scripts\activate
# Descargar pip: python -m pip install mysql-connector-python 

# create DATABASE planetas;
# create user planetas@'localhost' identified by 'planetas';
# create user planetas@'%' identified by 'planetas';
# grant all privileges on planetas.* to planetas@'localhost';
# grant all privileges on planetas.* to planetas@'%';

import mysql.connector
from mysql.connector import Error

# Conectar a la base de datos planetas
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="planetas",
        password="planetas",
        database="planetas",
    )
    print(conexion)
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")

# Crear tabla llamada planetas
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="planetas",
        password="planetas",
        database="planetas",
    )

    cursor = conexion.cursor()
    cursor.execute(
        "CREATE TABLE planetas (" \
            "id INT AUTO_INCREMENT PRIMARY KEY, " \
            "nombre VARCHAR(100) NOT NULL, " \
            "tipo VARCHAR(50), " \
            "lunas INT" \
        ");"
    )

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# Insertar 2 planetas y mostrar num filas insertadas
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="planetas",
        password="planetas",
        database="planetas",
    )

    cursor = conexion.cursor()
    sql = "INSERT INTO planetas (nombre, tipo, lunas) VALUES (%s, %s, %s)"
    val = [
        ("Marte", "Rocoso", 2),
        ("Júpiter", "Gaseoso", 79),
    ]

    cursor.executemany(sql, val)

    conexion.commit()

    print(cursor.rowcount, "filas se han insertado.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# Consultar planeta con id=1
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="planetas",
        password="planetas",
        database="planetas",
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM planetas")

    resultado = cursor.fetchall()

    print(resultado[1])

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")