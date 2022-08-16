"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene indice ni orden
"""

personas = {
    "Victor",
    "Mateo",
    "Javier"
}

personas.add("Carlos")
personas.remove("Mateo")

print(type(personas))
print(personas)