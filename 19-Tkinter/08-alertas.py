from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry('700x400')

def sacarAlerta():
    MessageBox.showwarning('Alerta', 'Holaaa!!')

Button(ventana, text='Mostrar alerta', command=sacarAlerta()).pack()

def salir(nombre):
    resultado = MessageBox.askquestion('Salir', 'Quieres continuar ejecutando la aplicacion?')

    if resultado != 'yes':
        MessageBox.showinfo('Adios!', f'Bye {nombre}!!!')
        ventana.destroy()

Button(ventana, text='Salir', command=lambda: salir('mons')).pack()

ventana.mainloop()