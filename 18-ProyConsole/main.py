"""
    Asistente de notas con python y mysql
"""

from usuarios import acciones

print("""
    ASISTENTE DE NOTAS
    - registro
    - login
""")

hacer = acciones.Acciones()

accion = input("Que quieres hacer? ")

if accion == "registro":
    hacer.registro()

elif accion == "login":
    hacer.login()
    