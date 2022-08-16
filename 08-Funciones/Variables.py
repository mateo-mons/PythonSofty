"""
    VARIABLES LOCALES: Se definen dentro de la funcion y no
    se pueden usar fuera de ella, solo estan disponibles dentro.
    A no ser que se haga un return

    VARIABLES GLOBALES: Son las que se declaran fuera de una funcion
     y estan disponibles dentro y fuera de ellas
"""

# variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print("Dentro de la funcion: ")
    print(frase)

    year = 2020
    print(year)

    global website
    website = "monsa.com"
    print("Dentro: ", website)

    return "Dato " + str(year)


print(holaMundo())
print("Fuera: ", website)