"""
    - cuanto es el X% de x numero
"""

numero = int(input("Ingrese el numero: "))
porcent = int(input("Ingrese porcentaje que desea saber del numero: "))

porcentaje = ((numero * porcent) / 100)
print(f"El resultado de {porcent}% del numero {numero} es de: {porcentaje}")