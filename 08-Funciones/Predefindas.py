nombre = "Mateo Monsalve"

# FUNCIONES GENERALES #
print(type(nombre))

# DETECTAR EL TIPADO #
comprobar = isinstance(nombre, str)
if comprobar:
    print("La variable es un string")
else:
    print("No es cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# LIMPIAR ESPACIOS #
frase = "   mi contenido   "
print(frase)
print(frase.strip())

# ELIMINAR VARIABLES #
year=2020
print(year)
del year
#print(year)

# COMPROBAR VARIABLES VACIAS #
texto = "  ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ",len(texto))

# ENCONTRAR CARACTERES #
frase = "Lok'tar Ogar"
print(frase.find("Ogar"))

# REEMPLAZAR PALABRAS EN UN STRING #
nuevaFrase = frase.replace("Ogar", "perra")
print(nuevaFrase)

#MAYUSCULAS Y MINUSCULAS #
print(nombre)
print(nombre.lower())
print(nombre.upper())