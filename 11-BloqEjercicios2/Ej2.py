"""
Escribir un programa qua añada valores a una lista
mientras que su longitud sea menor a 120 y mostrar la lista
- Usar while y for
"""

"""lista = list(range(1, 120))
print(lista)"""

lista1 = []
lista2 = []


def cicloWhile(ls):
    print('---- Ciclo While ----')
    contador = 0 
    while contador < 120:
        ls.append(contador)
        contador += 1
    print(ls)    

def cicloFor(ls):
    print('---- Ciclo For ----')
    for counter in range(0, 120):
        ls.append(counter)
    print(ls)

cicloWhile(lista1)
print('\n')
cicloFor(lista2)