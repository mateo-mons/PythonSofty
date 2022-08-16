"""
 FOR

 for variable in elemento_iterable (lista, rango)
    BLOQUE DE INSTRUCCIONES
"""

"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Numero ",str(contador))

    resultado = resultado + contador
print(f"El resultado es: {resultado}")

"""

# Ejemplo tablas de multiplicar

print("--------------------------")
print("\n---- Ejemplo ----")

numeroUsuario = int(input("Numero de la tabla a revisar: "))

if (numeroUsuario < 1):
    numeroUsuario = 1

print(f" Tabla del {numeroUsuario}")

for numeroTabla in range(1,11):
    print(f"{numeroUsuario} x {numeroTabla} = {numeroUsuario * numeroTabla}")
else:
    print("Tabla finalizada")