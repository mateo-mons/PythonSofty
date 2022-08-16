"""
    - Pedir nota de 15 alumnos y sacar por pantalla cuantos han aprobado
    y cuantos han reprobado
"""

contador = 1
aprobados = 0
reprobados = 0

numeroAlumnos = int(input("Numero de alumnos: "))

while contador <= numeroAlumnos:
    nota = int(input(f"Nota de alumno {contador}: "))

    if nota >= 3 and nota <= 5:
        aprobados += 1
    else:
        reprobados += 1

    contador += 1

print(f"\nAlumnos aprobados: {aprobados}")
print(f"\nAlumnos reprobados: {reprobados}")