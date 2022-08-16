"""

# Condicional IF

SI se_cumple_esta_condicion:
    ejecutar grupo de instrucciones
SI NO:
    ejecutar otro grupo de instrucciones

if condition:
    instructions
else:
    otras instrucciones


# Operadores de comparacion
== igual
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que

# Operadores logicos
and  Y
or   O
!    negacion
not  NO

"""
"""
# Ejemplo 1
print("----- Ejemplo 1 -----")

# color = "rojo"
color = input("Adivina el color: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es rojo")
else:
    print("Color incorrecto")
"""

print("---------------------------------------")
"""
# Ejemplo 2
print("----- Ejemplo 2 -----")

year = int(input("Ingresa el año: "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")
"""
"""
# Ejemplo 3
print("----- Ejemplo 3 -----")

nombre = "Mateo Monsalve"
ciudad = "Bogota"
continente = "Suramerica"
edad = 22
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Suramerica":
        print("El usuario no es Suramericano")
    else:
        print(f"Es suramericano y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")
"""

"""
# Ejemplo 4
print("----- Ejemplo 4 -----")

dia = int(input("Introduce el numero del dia: "))


if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes") 
    else:
        if dia == 3:
            print("Es miercoles")    
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sabado")
                    else:
                        if dia == 7:
                            print("Es domingo")
                        else:
                            print("numero incorrecto")
     


if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
else:
    print("Fin de semana")

"""


# Ejemplo 5
print("----- Ejemplo 5 -----")

edadMin = 18
edadMax = 65
edadOficial = int(input("Introduce tu edad: "))

if edadOficial >= 18 and edadOficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

"""
# Ejemplo 6
print("----- Ejemplo 6 -----")

pais = "Colombia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")
"""
"""
# Ejemplo 7
print("----- Ejemplo 7 -----")

pais = "Colombia"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")
"""

# Ejemplo 8
print("----- Ejemplo 8 -----")

pais = "China"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")