from tkinter import *

ventana = Tk()
#ventana.geometry('700x500')


texto = Label(ventana, text='Bienvenido al programa')
texto.config(
    fg='white',
    bg='black',
    padx=30,
    pady=30,
    font=('Consolas', 20)    
)
texto.pack(side=TOP)

texto = Label(ventana, text='Soy Mateo Monsalve')
texto.config(
    height=3,
    bg='orange',
    font=('Consolas', 18),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text='texto 1')
texto.config(
    height=3,
    fg='black',
    bg='red',
    font=('consolas', 15),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='texto 2')
texto.config(
    height=3,
    fg='red',
    bg='black',
    font=('consolas', 15),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='texto 3')
texto.config(
    height=3,
    fg='blue',
    bg='gray',
    font=('consolas', 15),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()