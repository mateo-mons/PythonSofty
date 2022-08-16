#Capturar excepciones y manejar errores en codigo
#susceptible a fallos/errores

"""
try:
    nombre = input('Nombre: ')

    if len(nombre) > 1:
        nombreUsuario = 'El nombre es ' + nombre

    print(nombreUsuario)
except:
    print('Error, nombre invalido, ingresar nombre nuevamente')
else:
    print('Nombre guardado correctamente')
finally:
    print('Fin de la iteracion')

"""

#   Multiples excepciones   #
"""
try:
    numero = int(input('Introduce un número para elevarlo al cuadrado: '))
    print('El cuadrado del número es: ' + str(numero*numero))
except ValueError:
    print('Dato invalido, introduce un número correcto')
except Exception as error:
    print('Ha ocurrido un error: ', type(error).__name__)
"""

#   Excepciones personalizadas o lanzar excepcion   #

try:
    nombre = input('Introduce nombre: ')
    edad = int(input('Introduce edad: '))

    if edad < 5 or edad > 110:
        raise ValueError('La edad introducida no es real')
    elif len(nombre) <= 1:
        raise ValueError('Nombre incompleto')
    else:
        print(f'Bienvenido, {nombre}')
except ValueError:
    print('Introduce los datos correctamente!!')