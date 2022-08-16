from classCar import Carro

carro1 = Carro('Amarillo', 'Renault', 'Logan', 250)
carro2 = Carro('Verde', 'Lamborghini', 'Orus', 300)
carro3 = Carro('Rojo', 'Ferrari', 'Formula', 500)
carro4 = Carro('Naranja', 'Ford', 'Model T', 50)


print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

# Detectar tipado #
if type(carro4) == Carro:
    print('Es un objeto correcto')
else:
    print('No es un objeto')


# Visibilidad #
print(carro2.publico)
print(carro4.getPrivado())