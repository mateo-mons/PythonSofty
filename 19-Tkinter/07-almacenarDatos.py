from socket import PACKET_LOOPBACK
from tkinter import *

ventana = Tk()
ventana.geometry('700x400')

ventana.config(
    bd=50
)

def getData():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_almacenado.config(
            bg='gray',
            fg='white'
        )

dato = StringVar()
resultado = StringVar()

Label(ventana, text='Introduce un texto').pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text='Dato almacenado:').pack(anchor=NW)
texto_almacenado = Label(ventana, textvariable=resultado)
texto_almacenado.pack(anchor=NW)

Button(ventana, text='Mostrar', command=getData).pack(anchor=NW)

ventana.mainloop()