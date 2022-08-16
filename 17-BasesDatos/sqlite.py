# Importar el modulo
import sqlite3

# Conectar el modulo
conexion = sqlite3.connect('./17-BasesDatos/pruebas.db')

# Creaar consulta
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS Productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO Productos VALUES (null, 'Primer producto', 'Descripcion del producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM Productos")
conexion.commit()

# Insertar muchos registros
productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("Telefono movil", "Exelente estado", 400),
    ("Tarjeta grafica", "Graficos exepcionales", 250),
    ("Monitor acer", "Alta resolucion", 200)
]
cursor.executemany("INSERT INTO Productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute('UPDATE Productos SET precio=1000 WHERE precio=200')

# Listar datos
cursor.execute("SELECT * FROM Productos;")
productos = cursor.fetchall()

for producto in productos:
    print(f'ID producto: {producto[0]}')
    print(f'Titulo: {producto[1]}')
    print(f'Descripcion: {producto[2]}')
    print(f'Precio: ${producto[3]}')
    print('----------------------------')

# Cerrar la conexion
conexion.close()