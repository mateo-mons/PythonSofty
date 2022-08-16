"""
WHILE
Estructura de control que itera o repite la ejecucion de una
serie de instrucciones tantas veces como sea necesario,
hasta cumplirse la condicion

while condicion:
    bloque de instrucciones
    actualizacion de contador
"""

"""
contador = 1

while contador <= 100:
    print(f"Numero: {contador}")
    contador += 1

print("-------------------------")

contador = 1
mostrar = str(0)

while contador <= 100:
    mostrar = mostrar + ", " + str(contador)
    contador += 1
print(mostrar)
"""

print("----------------")

# Ejemplo tablas de multiplicar
print("---- Ejemplo ----")

numeroUsuario = int(input("Inserte numero de la tabla: "))
if numeroUsuario < 1:
    numeroUsuario = 1

print(f"Tabla del {numeroUsuario}")

contador = 1

while contador <= 10:
    print(f"{numeroUsuario} x {contador} = {numeroUsuario * contador}")
    contador += 1
else:
    print("Tabla terminada")
