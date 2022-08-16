# Tkinter -> modulo para crear interfaces graficas de usuario
import os.path
from tkinter import *

class Programa:
    
    def __init__(self):
        self.title = "Master python"
        self.icon = './imagenes/imgProof.ico'
        self.icon_alt = './19-Tkinter/imagenes/imgProof.ico'
        self.size = '770x450'
        self.resizable = False
    
    def cargar(self):
        # ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # titulo de la ventana
        ventana.title(self.title)

        # ARREGLAR RUTA PARA EL ICONO #

        # comprobar si existe un archivo
        #ruta_icono = os.path.abspath(self.icon)

        #if not os.path.isfile(ruta_icono):
        #    ruta_icono = os.path.abspath(self.icon_alt)

        # icono de la ventana
        #ventana.iconbitmap(ruta_icono)

        # mostrar texto en el programa
        #texto = Label(ventana, text=ruta_icono)
        #texto.pack()

        # cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # mostrar ventana hasta que se cierre
        self.ventana.mainloop()

# instanciar programa
programa = Programa()
programa.cargar()
programa.addTexto('Este es un metodo')
programa.mostrar()