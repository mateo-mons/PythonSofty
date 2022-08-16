"""
    - Mostrar tablas de multiplicar del 1 al 10
"""

tablaDel = 1
numeroTabla = 1

for tablaDel in range(1, 11):
    print("-----------------------")
    print(f"Tabla del {tablaDel}")
    for numeroTabla in range(1, 11):
        multiplicacion = tablaDel * numeroTabla
        print(f"{tablaDel} x {numeroTabla} = {multiplicacion}")
    print("\n Tabla finalizada")