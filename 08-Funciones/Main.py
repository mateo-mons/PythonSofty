"""
    Funcion: Conjunto de instrucciones agrupadas bajo un nombre concreto
    que pueden reutilizarse invocando a la funcion tantas veces como sea necesario

def nombreFuncion(parametros):
    Conjunto de instrucciones

nombreFuncion(miParametro)
"""

"""
# Ejemplo 1
print("---- Ejemplo 1 ----")

# Definicion de funcion
def muestraNombres():
    print("Mateo")
    print("Dani")
    print("Javi")
    print("Virto")
    print("Carl")
    print("Papo")
    print("\n")

# Invocacion de funciones
muestraNombres()
"""

"""
# Ejemplo 2, Parametros
print("---- Ejemplo 2 ----")

def mostrarNombre(nombre):
    print(f"Nombre: {nombre}")

nombre = input("Ingresa tu nombre: ")
mostrarNombre(nombre)
"""

"""
# Ejemplo 3
print("---- Ejemplo 4 ----")

def tabla(num):
    print(f"Tabla de multiplicar del {num}")

    for contador in range(11):
        operacion = num * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

numero = int(input("Ingrese el numero de la tabla que desea saber: "))

tabla(numero)
"""

"""
# Ejemplo 4
print("---- Ejemplo 4 ----")

# Parametros opcionales
def getEmpleado(nombre, id = None):
    print("EMPLEADO")
    print(f"nombre: {nombre}")

    if id != None:
        print(f"id: {id}")

getEmpleado("Mateo", 1093229078)
"""

"""
# Ejemplo 5, return o devolver datos
print("---- Ejemplo 5 ----")

def saludar(nom):
    saludo = f"Hola, saludos {nom}"

    return saludo

print(saludar("Mateo Monsalve"))
"""


# Ejemplo 6
print("---- Ejemplo 6 ----")

def calculadora(n1, n2, basicas = False):
    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    division = n1 / n2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"

    return cadena
print(calculadora(6, 4))


"""
# Ejemplo 7
print("---- Ejemplo 7 ----")

def getNombre(nom):
    texto = f"El nombre es: {nom}"
    return texto

def getApellido(ape):
    texto = f"El apellido es: {ape}"
    return texto

def devuelveTodo(nom, ape):
    texto = getNombre(nom) + "\n" + getApellido(ape)
    return texto

print(devuelveTodo("Mateo", "Monsalve"))
"""

# Ejemplo 8, Funciones Lambda
print("---- Ejemplo 8 ----")

year = lambda year: f"El año es: {year * 2}"

print(year(2034))