import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "pythonDB1",
            port = 3306
        )
        print("Conexion establecida", database)

    except Error as e:
        print("Error al conectar a la base de datos.")
        print(e)


    cursor = database.cursor(buffered = True)

    return [database, cursor]