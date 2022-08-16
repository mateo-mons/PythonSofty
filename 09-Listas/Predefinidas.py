cantantes = ['pink floyd', 'metallica', 'the doors']
numeros = [1, 4, 3, 6, 7, 9, 2]

# ORDENAR #
print(numeros)
numeros.sort()
print(numeros)

# AÑADIR ELEMENTOS #
cantantes.append("black sabbath")
cantantes.insert(2,"bathory")
print(cantantes)

# ELIMINAR ELEMENTOS #
cantantes.pop(4)
cantantes.remove('metallica')
print(cantantes)

# DAR VUELTA #
numeros.reverse()
print(numeros)

# BUSCAR DENTRO DE UNA LISTA #
print('bathory' in cantantes)

# CONTAR ELEMENTOS #
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO #
numeros.append(6)
print(numeros)
print(numeros.count(6))

# CONSEGUIR INDICE #
print(cantantes.index('pink floyd'))

# UNIR LISTAS #
cantantes.extend(numeros)
print(cantantes)