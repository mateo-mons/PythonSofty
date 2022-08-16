class Carro:
    # Atributos o propiedades, caracteristicas #
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Formula'
    velocidad = 300

    publico = 'Atributo publico'
    __privado = 'Atributo privado'

    # Costructor para inicializacion de objeto #
    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad


    # Metodos, acciones que hace el objeto (funciones) #
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getPrivado(self):
        return self.__privado
    
    def getInfo(self):
        info = '---- Informacion del carro ----'
        info += '\n Color: ' + self.getColor()
        info += '\n Marca: ' + self.getMarca()
        info += '\n Modelo: ' + self.getModelo()
        info += '\n Velocidad: ' + str(self.getVelocidad())
        info += '\n'

        return info

# fin definicion clase