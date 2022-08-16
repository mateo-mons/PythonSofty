"""
Crear un script que tenga 4 variables, lista, string, entero 
y boolean. Debe imprimir un mensaje que diga el tipo de dato de 
cada variable. Usar funciones
"""

lista = [1, 2, 3]
string = 'Master Python'
entero = 66
boolean = True


def traduccionTipo(tipo):
    result = None

    if tipo == list:
        result = 'LISTA'
    elif tipo == str:
        result = 'CADENA DE TEXTO'
    elif tipo == int:
        result = 'ENTERO'
    elif tipo == bool:
        result = 'BOOLEANO'
    else:
        result = 'dato diferente'
    
    return result

def tipoDato(dato, tipo):
    test = isinstance(dato, tipo)
    result = None

    if test:
        result = f'El dato es de tipo {traduccionTipo(tipo)}'
    else:
        result = 'El tipo de dato es ERRONEO'

    return result


print(tipoDato(lista, list))
print(tipoDato(string, str))
print(tipoDato(entero, int))
print(tipoDato(boolean, bool))