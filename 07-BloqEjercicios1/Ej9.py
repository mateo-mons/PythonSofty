"""
    - Hacer un programa que pida numeros al ususario indefinidamente
    hasta meter el numero 111
"""

contador = 1

while contador < 100:
    numero = int(input("Ingrese un numero: "))

    if numero == 111:
        break