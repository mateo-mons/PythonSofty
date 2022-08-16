"""
    - Script que haga los cuadrados de los numeros naturales de los 60 primeros numeros naturales
    resolver con FOR y WHILE
"""

"""
naturales = 1

for naturales in range(1, 61):
    print(f"Cuadrado de {naturales} es", naturales * naturales)
else:
    print("Fin")
"""

naturales = 0

while naturales <= 60:
    print(f"Cuadrado de {naturales} es", naturales * naturales)
    naturales += 1
else:
    print("Fin")