def holaMundo(name):
    return f'Hola que tal {name}'

def calculadora(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    result = ''

    result += 'suma: ' + str(suma) + '\n'
    result += 'resta: ' + str(resta) + '\n'
    result += 'multiplicacion: ' + str(multi) + '\n'
    result += 'division: ' + str(division) + '\n'

    return result