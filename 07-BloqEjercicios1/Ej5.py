"""
    - Hacer un programa que muestre los numeros entre dos
    numeros que diga el usuario
"""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
cuenta = n1

if n1 < n2:
    for cuenta in range(n1, (n2 + 1)):
        print(cuenta)
else:
    print("El numero 1 debe ser mayor al 2")