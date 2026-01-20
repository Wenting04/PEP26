# = == Crear conexión == = #
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    print(conexion)
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# = == Ejecutar sentencias SQL == = #
# - -- Crear tabla -- - #
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()
    cursor.execute(
        "CREATE TABLE series (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255) NOT NULL, genero VARCHAR(100));"
    )

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# - -- Insertar filas -- - #
# Insertar 1 fila
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    sql = "INSERT INTO series (titulo, genero) VALUES ('Breaking Bad', 'Drama')"

    cursor.execute(sql)

    conexion.commit()

    print(cursor.rowcount, "fila insertada.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# Insertar varias filas
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()
    sql = "INSERT INTO series (titulo, genero) VALUES (%s, %s)"
    val = [
        ("Stranger Things", "Ciencia ficción"),
        ("The Office", "Comedia"),
        ("Game of Thrones", "Fantasía"),
        ("Sherlock", "Misterio"),
    ]

    cursor.executemany(sql, val)

    conexion.commit()

    print(cursor.rowcount, "filas se han insertado.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# - -- Consultas -- - #
# Método fetchball(): recuera todas las filas de la última sentencia ejecutada
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM series")

    resultado = cursor.fetchall()

    for serie in resultado:
        print(serie)

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")



import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM series WHERE genero = 'Drama'")

    resultado = cursor.fetchall()

    for serie in resultado:
        print(serie)

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# Método fetchone(): recupera sólo la primera fila de la última sentencia ejecutada
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM series")

    resultado = cursor.fetchone() # Sólo lees 1 fila

    print(resultado)

    cursor.close() # Quedan filas sin leer
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# - -- Actualizaciones -- - #
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    sql = "UPDATE series SET genero = 'Comedia' WHERE titulo = 'Friends'"
    cursor.execute(sql)

    conexion.commit()

    print(cursor.rowcount, "fila actualizada.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# - -- Borrados -- - #
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    sql = "DELETE FROM series WHERE genero = 'Comedia'"
    cursor.execute(sql)

    conexion.commit()

    print(cursor.rowcount, "fila actualizada.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# - -- Borrar una tabla -- - #
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()
    sql= "DROP TABLE series"
    cursor.execute(sql)

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")

# = == Gestión de excepciones == = #
import mysql.connector
from mysql.connector import Error

cursor = None
conexion = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    if conexion.is_connected():
        print("Conectado a MySQL")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM series")
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)

except Error as e:
    print(
        f"Error al conectar a MySQL: {e}\n"
        f"Parámetros de conexión: host='localhost', user='series', database='series'"
    )
finally:
    if cursor is not None:
        try:
            cursor.close()
        except Exception as ex:
            print(f"Error al cerrar el cursor: {ex}")
    try:
        if conexion is not None:
            conexion.close()
    except Exception as ex:
        print(f"Error al cerrar la conexión MySQL: {ex}")

# = == Gestión de transacciones (commit y rollback) == = #
# Si hemos hecho el paso anterior, la tabla series no debe de existir, por tanto este paso no funcionará
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )
    cursor = conexion.cursor()

    # Start transaction
    conexion.start_transaction()

    sql = "INSERT INTO series (titulo, genero) VALUES (%s, %s)"
    valores = ('Breaking Bad', 'Drama')

    cursor.execute(sql, valores)

    conexion.commit()
    print("Transaction completed successfully")
except Error as e:
    print("Error durante la transacción:", e)
    if 'conexion' in locals() and conexion.is_connected():
        conexion.rollback()
        print("Transaction rolled back")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()