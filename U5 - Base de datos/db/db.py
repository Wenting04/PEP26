# = == Gestión de transacciones (commit y rollback) == = #
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