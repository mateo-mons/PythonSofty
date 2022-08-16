"""
    - Pedir dos numeros al usuario y hacer todas las
    operaciones basicas de una calculadora y mostrar
    por pantalla
"""

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

print("\n---- CALCULADORA ----")
print(f"\nLa suma es {suma}")
print(f"\nLa resta es {resta}")
print(f"\nLa multiplicacion es {multiplicacion}")
print(f"\nLa division es {division}\n")