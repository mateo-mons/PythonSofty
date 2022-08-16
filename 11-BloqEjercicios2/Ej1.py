"""
Hacer un programa que tenga una lista de 8 numeros
enteros y que haga lo siguiente:
- recorrer la lista y mostrarla
- hacer funcion que recorra la lista de numeros
  y devuelva un string
- ordenarla y mostrarla
- mostrar su longitud
- buscar un elemento (que el usuario pida por teclado)
"""

listaNum = [3, 5, 4, 2, 7, 8, 1, 6]

def Recorrer(ls):
    elemento = ""
    for elemento in ls:
        print(str(elemento))

    return elemento

def Ordenar(ls):
    ls.sort()
    print(ls)

def Longitud(ls):
    longitud = str(len(ls))
    print("La longitud de la lista es de " + longitud)

def BuscarElemento(ls):
    search = int(input("Ingrese el elemento que desea: "))

    if listaNum.index(search):
        print(f"el numero {search} esta en la lista {ls}")
    else:
        print(f"el numero {search} NO esta en la lista {ls}")
        
    return search

print("---- Recorrer lista y mostrarla ----")
#print(listaNum)
Recorrer(listaNum)
#Recorrer(["mateo", "juan", "pepe"])

print("---- Ordenar elementos ----")
#listaNum.sort()
Ordenar(listaNum)
print(listaNum)

print("---- Longitud ----")
Longitud(listaNum)

print("---- Buscar elemento ----")
BuscarElemento(listaNum)