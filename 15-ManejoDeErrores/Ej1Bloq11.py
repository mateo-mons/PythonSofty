listaNum = [3, 5, 4, 2, 7, 8, 1, 6]

print("---- Buscar elemento ----")

try:
    busqueda = int(input('Ingrese número: '))

    comprobar = isinstance(busqueda, int)

    while not comprobar or busqueda <= 0:
        busqueda = int(input('Ingrese número: '))
    else:
        print(f'Numero introducido {busqueda}')

    print(f'Buscando el la lista el numero {busqueda}')


    search = listaNum.index(busqueda)
    print(f'El numero {busqueda} existe en la lista, es el indice: {search + 1}')
except:
    print(f'El numero {busqueda} no esta en la lista')
