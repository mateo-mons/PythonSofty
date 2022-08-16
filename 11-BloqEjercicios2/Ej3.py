"""
Programa que comprueve si una variable esta vacia, y si lo está,
rellenarla con texto en minusculas y mostrarla en mayusculas
"""

texto = " "

if len(texto.strip()) <= 0:
    texto = str(input("Ingresa un texto: "))
    print(texto.upper())
else:
    print(f'La variable tiene contenido {texto}')