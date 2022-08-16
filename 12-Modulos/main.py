"""
Los modulos en python son funcionalidades ya hechas para reutilizar.
En la documentacion de python.org se pueden encontrar y consultar.

Podemos conseguir modulos que ya vienen en el lenguaje, modulos en
internet o tambien podemos crear nuestros propios modulos
"""
#   Importar modulo propio  #
#import modulo1
from modulo1 import *

"""print(modulo1.holaMundo('Mateo Monsalve'))
print(modulo1.calculadora(2, 5))"""

print(calculadora(7, 4))

#   Modulo de fechas   #
import datetime

print(datetime.date.today())

fechaCompleta = datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

fechaPersolalizada = fechaCompleta.strftime("%d/%m/%Y, %H:%M:%S")
print('Fecha personalizada ', fechaPersolalizada + '\n')

#   Modulo matematicas  #
import math

print('Raiz cuadrada de 10 es:', math.sqrt(10))
print('Numero pi:', math.pi)
print('Redondear numero hacia arriba:', math.ceil(6.783453))
print('Redondear numero hacia abajo:', math.floor(6.76545))

# Modulo random #
import random
print('numero aleatorio entre 15 y 60: Aleatorio -', random.randint(15, 60))