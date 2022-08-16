"""
Diccionario:
Tipo de dato que almacena un conjunto de datos.
En forma clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

personas = {
    "nombre": "Mateo",
    "apellidos": "Monsalve",
    "web": "mateo-mons"
}

print(personas["web"])

# LISTA CON DICCIONARIOS #

contactos = [
    {
        'nombre': 'Mateo',
        'email': 'mateo@mateo.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Javier',
        'email': 'javier@javier.com'
    }
]

contactos[0]['nombre'] = "Mateito"
print(contactos[0]['nombre'])

print("\n Listado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("\n")