from tkinter import *

ventana = Tk()
ventana.geometry('700x500')

def pruebas(nombre, apellido, pais):
    return f'Hola {nombre} {apellido} veo que eres de {pais}'

texto = Label(ventana, text='Bienvenido al programa')
texto.config(
    fg='white',
    bg='black',
    padx=30,
    pady=30,
    font=('Consolas', 20)    
)
texto.pack()

texto = Label(ventana, text='Soy Mateo Monsalve')
texto.config(
    height=3,
    bg='orange',
    font=('Consolas', 18),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(anchor=NE)

texto = Label(ventana, text=pruebas(nombre='mateo', apellido='monsalve', pais='Colombia'))
texto.config(
    height=3,
    fg='black',
    bg='red',
    font=('consolas', 15),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(anchor=NW)

ventana.mainloop()