from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('700x500')

Label(ventana, text='Hola, soy Mateo').pack()

imagen = Image.open('./imagenes/imgProof4.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()