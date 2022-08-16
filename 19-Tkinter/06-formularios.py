from tkinter import *

from sqlalchemy import column

ventana = Tk()
ventana.geometry('700x400')
ventana.title('Formularios en Tkinter')

# Encabezado
encabezado = Label(ventana, text='Formularios con Tkinter, Mons')
encabezado.config(
    fg='white',
    bg='darkgray',
    font=('Consolas', 20),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# label para el campo(nombre)
label = Label(ventana, text='Nombre')
label.grid(row=1, column=0, padx=5, pady=5)

# campo de texto(nombre)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, columnspan=6, sticky=W, padx=5, pady=5)
campoTexto.config(justify='left', state='normal')


# label para el campo(apellidos)
label = Label(ventana, text='Apellidos')
label.grid(row=2, column=0, padx=5, pady=5)

# campo de texto(apellidos)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, columnspan=6, sticky=W, padx=5, pady=5)
campoTexto.config(justify='left', state='normal')


# label para el campo(descripción)
label = Label(ventana, text='Descripcion')
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# campo de texto GRANDE(descripcion)
campoGrande = Text(ventana)
campoGrande.config(
    height=5,
    width=30,
    font=('Arial', 12),
    padx=15,
    pady=15
)
campoGrande.grid(row=3, column=1)

# boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text='Enviar')
boton.config(
    padx=15,
    pady=15,
)
boton.grid(row=5, column=1, sticky=W)

ventana.mainloop()