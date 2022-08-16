from tkinter import *

ventana = Tk()
ventana.title('Marcos ||')
ventana.geometry('700x700')

# MARCOS DE ARRIBA #

marcoPadre = Frame(ventana, width=250, height=250)
marcoPadre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='yellow',
    bd=5,
    relief='solid'
)
marco.pack(side=LEFT)
marco.pack_propagate(False)

texto = Label(marco, text='primer marco')
texto.config(
    bg='yellow',
    height=50,
    width=50,
    anchor=CENTER
)
texto.pack(side=TOP, anchor=CENTER)

marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='green',
    bd=5,
    relief='solid'
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)

texto = Label(marco, text='segundo marco')
texto.config(
    bg='green',
    height=50,
    width=50,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)


# MARCOS DE ABAJO #
marcoPadre = Frame(ventana, width=250, height=250)
marcoPadre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='brown',
    bd=5,
    relief='solid'
)
marco.pack(side=LEFT)
marco.pack_propagate(False)

texto = Label(marco, text='tercer marco')
texto.config(
    bg='brown',
    height=50,
    width=50,
    anchor=CENTER
)
texto.pack(side=TOP, anchor=CENTER)

marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='blue',
    bd=5,
    relief='solid'
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)

texto = Label(marco, text='cuarto marco')
texto.config(
    bg='blue',
    height=50,
    width=50,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)


ventana.mainloop()