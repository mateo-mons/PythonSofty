#   PROGRAMACION ORIENTADA A OBJETOS    #
"""
Definir una clase (molde para crear mas objetos de ese tipo con
caracteristicas similares)
"""

class Carro:
    # Atributos o propiedades, caracteristicas #
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Formula'
    velocidad = 300

    # Metodos, acciones que hace el objeto (funciones) #
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# fin definicion clase

# Crear objetos / instanciar clase
carro1 = Carro()
print('CARRO 1')

carro1.setColor('amarillo')
carro1.setModelo('Murcielago')

print(carro1.marca, carro1.getModelo(), carro1.getColor())
print('Velocidad actual: ', carro1.getVelocidad())

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frenar()

print('Velocidad nueva: ', carro1.getVelocidad())

print('------------------------')
carro2 = Carro()
print('CARRO 2')

carro2.setColor('verde')
carro2.setModelo('Gallardo')

print(carro2.marca, carro2.getModelo(), carro2.getColor())