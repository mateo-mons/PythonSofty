"""
 LISTAS(Arrays)
 Son colecciones o conjuntos de datos/valores, bajo un unico
 nombre.
 Para acceder a esos valores podemos usar indice numerico.
"""

pelicula = "Batman"

# DEFINIR LISTAS #
peliculas = ["Batman", "Spiderman","The Hobbit"]
bandas = list(('Metallica', 'Iron Maiden', 'Lizard Wizard'))
years = list(range(2020, 2050))
variada = ["Maeto", 50, 4.6, True, "platano"]

print(peliculas)
print(bandas)
print(years)
print(variada)

 # INDICES #
pelicula = "Star Wars"
peliculas[0] = "El abogado del diablo"
peliculas[2] = "El señor de los anillos"
print(peliculas)

print(peliculas[2])
print(peliculas[-2])
print(bandas[0:2])
print(peliculas[0:])


# AÑADIR ELEMENTOS A LISTAS #
bandas.append("Black Sabbath")
print(bandas)

# RECORRER LISTAS #
"""NuevaPelicula = ""
while NuevaPelicula != "salir":
    NuevaPelicula = input("Introduce el nombre de la pelicula: ")

    if NuevaPelicula != "salir":
        peliculas.append(NuevaPelicula)

print("\n*******LISTADO PELICULAS*******")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")"""


# LISTAS MULTIDIMENSIONALES #

print("\n------ Listado de contactos -----------")

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'luis',
        'luis@luis.com'
    ],
    [
        'Alejandro',
        'alejandro@alejandro.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])