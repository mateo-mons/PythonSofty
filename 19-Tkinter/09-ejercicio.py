"""
CALCULADORA:
    - dos campos de texto
    - 4 botones para operaciones
    - mostrar el resultado en alertas
"""
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry('700x400')
ventana.title('Ejercicio calculadora')
ventana.config(
    bd=25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

# FUNCIONES DE LAS OPERACIONES #

def sumar():
    resultado.set(float(numero1.get()) + float(numero2.get()))
    mostrarResultado()
    
def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo('Resultado', f'el resultado de la suma es {resultado.get()}')
    numero1.set('')
    numero2.set('')


marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text='Primer numero: ').pack(anchor=NW)
Entry(marco, textvariable=numero1, justify='center').pack(anchor=NW)

Label(marco, text='Segundo numero: ').pack(anchor=NW)
Entry(marco, textvariable=numero2, justify='center').pack(anchor=NW)

Label(marco, text='').pack()

Button(marco, text='Sumar', command=sumar()).pack(side='left')
Button(marco, text='Restar', command=restar()).pack(side='left')
Button(marco, text='Multiplicar', command=multiplicar()).pack(side='left')
Button(marco, text='Dividir', command=dividir()).pack(side='left')

ventana.mainloop()