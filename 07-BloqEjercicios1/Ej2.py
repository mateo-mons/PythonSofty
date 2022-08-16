"""
    - Escribir un script que muestre por pantalla los numeros
    pares del 0 hasta el 120
"""

"""
contador = 0

while contador <= 120:
    print(f"{contador}")
    contador += 2
else:
    print("Terminado")
"""

contador = 1

for contador in range(1,121):
    if contador % 2 == 0:
        print(contador)