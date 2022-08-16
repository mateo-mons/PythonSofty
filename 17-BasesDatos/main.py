import mysql.connector

# Conexion
database = mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="",
    database="pythonDB"
)

print(database)
# Realizar consultas
cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS pythonMS")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)