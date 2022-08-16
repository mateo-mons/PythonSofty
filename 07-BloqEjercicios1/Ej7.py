"""
    - Hacer un programa que muestre todos los numeros impares entre dos
    numeros pedidos por usuario
"""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1 < n2:
    for contador in range(n1, (n2 + 1)):
        if contador % 2 != 0:
            print(contador)
else:
    print("El numero 1 debe ser mayor al 2")