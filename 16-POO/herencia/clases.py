# Herencia: Es la posibilidad de compartir atributos y metodos
# entre clases y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura 
    edad
    """
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad
    

    def hablar(self):
        return 'estoy hablando'
    
    def caminar(self):
        return 'estoy caminando'

    def dormir(self):
        return 'durmiendo'


class Informatico(Persona):
    def __init__(self):
        self.lenguajes = 'HTML, CSS, JavaScript'
        self.experiencia = 4

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return 'Estoy programando'
    
    def repararPC(self):
        return 'he reparado el ordenador'